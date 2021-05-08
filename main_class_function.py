import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

import os


class ReadCoefficientsFromFile:
    # filename of the form *.dar
    # cara velocity of sim m / s (default 5)
    # cara length of sim m (default 2)
    def __init__(self, filename, U=5, L=2):
        self.df = np.loadtxt(filename, comments="#")
        self.n_steady_state = 500

        # extract useful cols
        self.evolution_coefficient = {
            "time": [self.df[i][0] for i in range(len(self.df))],
            "$C_d$": [self.df[i][1] for i in range(len(self.df))],
            "$C_l$": [self.df[i][3] for i in range(len(self.df))],
        }

        # compute Fourier transformation
        ft = ReadCoefficientsFromFile.fourier_transformation
        t = self.evolution_coefficient["time"][self.n_steady_state:]

        # dict of the form (fourier transform t, fourier transform coeff)
        self.ft_coef = {
            "$C_d$": ft(t, self.evolution_coefficient["$C_d$"][self.n_steady_state:]),
            "$C_l$": ft(t, self.evolution_coefficient["$C_l$"][self.n_steady_state:])
        }

        # dominant frequency
        get_dominant_frequency = ReadCoefficientsFromFile.get_max_frequency

        self.dominant_frequency = {
            "$C_d$": get_dominant_frequency(*self.ft_coef["$C_d$"]),
            "$C_l$": get_dominant_frequency(*self.ft_coef["$C_l$"])
        }

        # conclude nb of St
        self.nb_St = self.dominant_frequency["$C_l$"] * L / U

        self.mean_coef = {
            "$C_d$": np.mean(self.evolution_coefficient["$C_d$"][self.n_steady_state:]),
            "$C_l$": np.mean(self.evolution_coefficient["$C_l$"][self.n_steady_state:])
        }

        return

    # plot Fourier transformation
    def plot_spec(self):
        # nombre de coefficient
        n = 2

        fig, axs = plt.subplots(1, n)

        i = 0
        for coef in self.ft_coef.keys():
            axs[i].loglog(*self.ft_coef[coef])

            axs[i].set_title("spectrum of {0} (Re = 1090)".format(coef))
            axs[i].set_xlabel('f (Hz)')
            axs[i].set_ylabel("amplitude")

            i += 1

        plt.tight_layout()

        plt.savefig("screenshots/example_fourier_transformation.png")
        plt.show()
        return

    # make a plot of the evolution of the two coefficients
    def plot(self):
        # nombre de coefficient
        n = 2

        # plot coefficients
        t = self.evolution_coefficient["time"]

        fig, axs = plt.subplots(1, n)

        i = 0
        for coef in self.evolution_coefficient.keys():
            # don t consider time
            if coef == "time":
                continue

            axs[i].plot(t[self.n_steady_state:], self.evolution_coefficient[coef][self.n_steady_state:])

            axs[i].set_title(coef)
            axs[i].set_xlabel('$t \ (s)$')

            i += 1

        axs[0].set_ylim(0, 65)
        axs[1].set_ylim(-50, 50)

        plt.tight_layout()

        plt.show()
        return

    # to access directly by name
    def __getitem__(self, item):
        return self.evolution_coefficient[item]

    # for FFT
    @staticmethod
    # return fourier: x and amplitude fourier y
    def fourier_transformation(x, y):
        yf = 2 / len(x) * np.abs(fft(y))
        xf = fftfreq(len(x), x[1] - x[0])

        return xf, yf

    # determine the vec with the max norm
    @staticmethod
    # for scalars this behave like np.max
    def get_max_vector(arr, norm=lambda x: x):
        # check array is not empty
        if len(arr) == 0:
            raise Exception("Empty array")

        # init
        max_vec = arr[0]
        max = norm(max_vec)

        # find max
        for current_vec in arr:
            current_norm = norm(current_vec)
            if current_norm > max:
                max = current_norm
                max_vec = np.array(current_vec)

        return max_vec

    @staticmethod
    def get_max_frequency(freq, amp):
        max_freq, max_amp = freq[0], amp[0]

        for i in range(len(freq)):
            if amp[i] > max_amp:
                max_freq = freq[i]
                max_amp = amp[i]

        return max_freq


# gather all simulations in a dic of form { Re: simulation }
# files must be named as R***.dat
DIRECTORY_NAME = "simulation_outputs/"


def build_dict_simulations(directory_path=DIRECTORY_NAME):
    # get files paths
    arr_file_path = os.listdir(directory_path)

    # create dict of simulations
    dict_simulations = {}

    for file_path in arr_file_path:
        # split to get R*** then keep numeric part
        Re = int(file_path.split(".")[0][1:])

        # add content of file to dict
        dict_simulations[Re] = ReadCoefficientsFromFile(filename=DIRECTORY_NAME + file_path)

    # sort dict according to Re
    dict_simulations = {key: val for key, val in sorted(dict_simulations.items())}

    return dict_simulations
