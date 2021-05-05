import numpy as np
from main_class_function import ReadCoefficientsFromFile


# create simulation object
sim = ReadCoefficientsFromFile(filename="simulations_outputs/R1090.dat")

sim.plot_spec()
