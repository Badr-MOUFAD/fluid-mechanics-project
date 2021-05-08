import matplotlib.pyplot as plt

from main_class_function import build_dict_simulations


# gather all sim in a dic of form { Re: simulation }
dict_simulation = build_dict_simulations()


Cd_mean = [sim.mean_coef["$C_d$"] for sim in dict_simulation.values()]
Cl_mean = [sim.mean_coef["$C_l$"] for sim in dict_simulation.values()]
arr_Re = dict_simulation.keys()

# init sub plot
fig, axs = plt.subplots(1, 2)

axs[1].set_ylim(-5, 5)

# plot curves
axs[0].semilogx(arr_Re, Cd_mean)
axs[1].semilogx(arr_Re, Cl_mean)

# set labels
axs[0].set_xlabel("$Re$")
axs[1].set_xlabel("$Re$")

axs[0].set_ylabel("$C_d$")
axs[1].set_ylabel("$C_l$")

# set titles
axs[0].set_title("Evolution of $C_d$ as function of Re")
axs[1].set_title("Evolution of $C_l$ as function of Re")

plt.tight_layout()

# save then show plot
# plt.savefig("screenshots/plot_mean_coef.png")
plt.show()
