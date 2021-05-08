import matplotlib.pyplot as plt

from main_class_function import build_dict_simulations


# gather all sim in a dic of form { Re: simulation }
dict_simulation = build_dict_simulations()


Cd_mean = [sim.dominant_frequency["$C_d$"] for sim in dict_simulation.values()]
Cl_mean = [sim.dominant_frequency["$C_l$"] for sim in dict_simulation.values()]
arr_Re = dict_simulation.keys()

# init sub plot
fig, axs = plt.subplots(1, 2)

axs[1].set_ylim(-0.1, 1)

# plot curves
axs[0].semilogx(arr_Re, Cd_mean)
axs[1].semilogx(arr_Re, Cl_mean)

# set labels
axs[0].set_xlabel("$Re$")
axs[1].set_xlabel("$Re$")

axs[0].set_ylabel("frequency of $C_d$ (Hz)")
axs[1].set_ylabel("frequency of $C_l$ (Hz)")

# set titles
axs[0].set_title("$C_d$ dominant $f$ as function of Re")
axs[1].set_title("$C_l$ dominant $f$ as function of Re")

plt.tight_layout()

# save then show plot
# plt.savefig("screenshots/plot_freq_coef.png")
plt.show()
