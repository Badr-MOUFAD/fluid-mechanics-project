import numpy as np
import matplotlib.pyplot as plt


# read data
data_Cd = np.loadtxt("experience_data/cylinder_drag.dat", comments="#").T
data_St = np.loadtxt("experience_data/cylinder_circle_strouhal.dat", comments="#").T


# Cd
# plot with log scale within x
plt.semilogx(data_Cd[0], data_Cd[1])

# title, x and y labels
plt.title("Real experience: Evolution of $C_d$ as function of Re")

plt.xlabel("Re")
plt.ylabel("$C_d$")

# save then show plot
plt.savefig("screenshots/real_experience_cd.png")

plt.show()


# St
# plot with log scale within x
plt.semilogx(data_St[0], data_St[1])

# title, x and y labels
plt.title("Real experience: Evolution of $S_t$ as function of Re")

plt.xlabel("Re")
plt.ylabel("$S_t$")

# save then show plot
plt.savefig("screenshots/real_experience_st.png")

plt.show()
