import numpy as np
import matplotlib.pyplot as plt

from main_class_function import build_dict_simulations


# read data experience
data_Cd = np.loadtxt("experience_data/cylinder_drag.dat", comments="#").T

# read data simulation
# gather all sim in a dic of form { Re: simulation }
dict_simulation = build_dict_simulations()

# construct St
arr_Cd = [sim.mean_coef["$C_d$"] for sim in dict_simulation.values()]
arr_Re = dict_simulation.keys()


# St
# plot with log scale within x
plt.semilogx(data_Cd[0], data_Cd[1], label="Real experience")
plt.semilogx(arr_Re, arr_Cd, label="simulation")

# title, x and y labels, legend
plt.title("Evolution of $C_d$ as a function of Re")
plt.legend()

plt.xlabel("Re")
plt.ylabel("$C_d$")

# save then show plot
plt.savefig("screenshots/comparaison_cd.png")

plt.show()
