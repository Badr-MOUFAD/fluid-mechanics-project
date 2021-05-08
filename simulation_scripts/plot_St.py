import matplotlib.pyplot as plt

from main_class_function import build_dict_simulations


# gather all sim in a dic of form { Re: simulation }
dict_simulation = build_dict_simulations()

# construct St
arr_St = [sim.nb_St for sim in dict_simulation.values()]
arr_Re = dict_simulation.keys()

# plot graph
plt.semilogx(arr_Re, arr_St, lable="simulation")

# title and labels
plt.title("Evolution of $S_t$ as function of Re")
plt.xlabel("Re")
plt.ylabel("$S_t$")


# save then show plot
# plt.savefig("screenshots/plot_St.png")
plt.show()
