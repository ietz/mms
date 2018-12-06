import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt


def main():
    N = 2000
    nT = 120

    x = np.linspace(0, 2 * np.pi * nT, N)
    s = np.sin(x)

    for i in [1, 3, 5, 7, 8, 9, 10, 12]:
        xD = x[::i]
        sD = s[::i]

        plt.gcf().set_size_inches(10, 3)
        #plt.plot(x, s)
        plt.plot(xD, sD)
        plt.show()


if __name__ == '__main__':
    main()
