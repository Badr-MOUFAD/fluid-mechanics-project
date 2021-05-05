import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

from main_class_function import ReadCoefficientsFromFile


# get files paths
DIRECTORY_NAME = "simulations_outputs/"
arr_file_path = os.listdir(DIRECTORY_NAME)

# create dict of simulations
dict_simulation = {}

for file_path in arr_file_path:
    # split to get R*** then keep numeric part
    Re = int(file_path.split(".")[0][1:])

    # add content of file to dict
    dict_simulation[Re] = ReadCoefficientsFromFile(filename=DIRECTORY_NAME + file_path)

# sort dict according to Re
dict_simulation = {key: val for key, val in sorted(dict_simulation.items())}


# init setups

# plots
init_grid = {
    "x": (0, 40),
    "y": (0, 100)
}

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=init_grid["x"], ylim=init_grid["y"])
#ax.set_aspect('equal')
ax.grid()


# Cd plot
Cd, = ax.plot([], [])

# to display elapsed time
Re_template = 'Re = %.0f'
Re_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

# steady state
n_steady = 500

def fun_animation(i_frame):
    Re = i_frame

    new_Cd = dict_simulation[Re]["$C_d$"][n_steady:]
    new_time = dict_simulation[Re]["time"][n_steady:]

    print(Re)

    Cd.set_data(new_time, new_Cd)

    # update Re
    Re_text.set_text(Re_template % Re)

    return Cd, Re_text


# run animation
interval = 300
anim = FuncAnimation(fig, fun_animation, dict_simulation.keys(), interval=interval, repeat=True)

plt.show()
