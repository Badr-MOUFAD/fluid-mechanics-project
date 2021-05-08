import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

from main_class_function import build_dict_simulations


# gather simulation in a dict
dict_simulation = build_dict_simulations()


# init setups

# plots
init_grid = {
    "x": (0, 40),
    "y": (0, 100)
}

fig, axs = plt.subplots(1, 2, subplot_kw=dict(autoscale_on=False, xlim=init_grid["x"]))

# y axis limit
axs[0].set_ylim(0, 100)
axs[1].set_ylim(-50, 50)

# Cd plot
Cd, = axs[0].plot([], [])
Cl, = axs[1].plot([], [])


# labeling
axs[0].set_xlabel("time")
axs[0].set_title("$C_d$")

axs[1].set_xlabel("time")
axs[1].set_title("$C_l$")

# to display elapsed time
Re_template = 'Re = %.0f'
Re_text_Cd = axs[0].text(0.05, 0.9, '', transform=axs[0].transAxes)
Re_text_Cl = axs[1].text(0.05, 0.9, '', transform=axs[1].transAxes)

# steady state
n_steady = 500

def fun_animation(i_frame):
    Re = i_frame

    new_Cd = dict_simulation[Re]["$C_d$"][n_steady:]
    new_Cl = dict_simulation[Re]["$C_l$"][n_steady:]
    new_time = dict_simulation[Re]["time"][n_steady:]

    Cd.set_data(new_time, new_Cd)
    Cl.set_data(new_time, new_Cl)

    # update Re
    Re_text_Cd.set_text(Re_template % Re)
    Re_text_Cl.set_text(Re_template % Re)

    return Cd, Cl, Re_text_Cd, Re_text_Cl


# run animation
interval = 500
anim = FuncAnimation(fig, fun_animation, dict_simulation.keys(), interval=interval, repeat=True)

# show animation
plt.tight_layout()

# save animation
# anim.save('screenshots/animation_Cd_Cl.gif', writer='Pillow', fps=60)

plt.show()
