import numpy as np
import matplotlib.pyplot as plt

from main_class_function import build_dict_simulations


# read data experience
data_St = np.loadtxt("experience_data/cylinder_circle_strouhal.dat", comments="#").T

# read data simulation
# gather all sim in a dic of form { Re: simulation }
dict_simulation = build_dict_simulations()

# construct St
arr_St = [sim.nb_St for sim in dict_simulation.values()]
arr_Re = dict_simulation.keys()


# St
# plot with log scale within x
plt.semilogx(data_St[0], data_St[1], label="Real experience")
plt.semilogx(arr_Re, arr_St, label="simulation")

# title, x and y labels, legend
plt.title("Evolution of $S_t$ as a function of Re")
plt.legend()

plt.xlabel("Re")
plt.ylabel("$S_t$")

# save then show plot
# plt.savefig("screenshots/comparaison_St.png")

plt.show()
