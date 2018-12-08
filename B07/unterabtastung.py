import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt


def main():
    N = 2000
    n_T = 120
    # F = 1
    F_s = N/n_T

    x = np.linspace(0, 2 * np.pi * n_T, N)
    s = np.sin(x)

    for D in [1, 3, 5, 7, 8, 9, 10, 12]:
        # Fs/D >= 2*Fmax
        # Fmax <= Fs/(2*D)
        f_cutoff = F_s/(2*D)

        x_down = downsample(x, D)
        s_filtered = lowpass(s, D)
        s_down = downsample(s_filtered, D)

        s_reconstructed = interpolate(s_down, D)[:2000]

        plt.gcf().set_size_inches(10, 3)
        plt.gca().set_xlim(0, 100)
        plt.plot(x, s, label='original')
        plt.plot(x, s_reconstructed, label='reconstructed')
        plt.plot(x_down, s_down, label='downsampled')
        plt.legend(loc='upper right')
        plt.show()


def lowpass(s, D):
    conv_filter = low(D)
    return np.convolve(s, conv_filter, mode='same')


def interpolate(s_down, D):
    s = upsample(s_down, D)
    conv_filter = low(D)
    return np.convolve(s, conv_filter, mode='same')


def downsample(s, D):
    return s[::D]


def upsample(s, D):
    s_up = np.zeros(len(s)*D)
    for i in range(len(s)):
        s_up[i*D] = s[i]
    return s_up


def low(D):
    ns = np.arange(-1000, 1000)
    return np.where(ns != 0, np.sinc(ns/D), 1)


if __name__ == '__main__':
    main()
