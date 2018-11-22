import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 2 * np.pi * 120, 2000)
    signal = np.sin(x)
    noise = np.random.normal(0, 1, x.shape[0])
    signalnoise = signal + noise

    spectrum = fft(signalnoise)
    correlation = [autocorrelate(signalnoise, k) for k in range(0, signalnoise.shape[0])]

    plot("FFT Spectrum", np.absolute(spectrum.imag))
    plot("Autocorrelation Sequence", correlation)
    plot("Autocorrelation FFT Spectrum", np.absolute(fft(correlation)))


def plot(title, values):
    plt.plot(np.absolute(values))
    plt.gca().set_title(title)
    plt.show()


def autocorrelate(x, k):
    return np.correlate(x, np.roll(x, k))[0]


if __name__ == '__main__':
    main()
