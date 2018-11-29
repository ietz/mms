import numpy as np
from numpy.fft import fft, fft2
import matplotlib.pyplot as plt


def main():
    T = 1000

    s = np.array(list(c + np.cos(np.linspace(0, 100*np.pi, T)) for c in np.cos(np.linspace(0, 100*np.pi, T))))

    plt.imshow(s)
    plt.show()

    F2 = fft2d(s)
    plt.imshow(np.abs(F2))
    plt.show()

    plt.imshow(diag())
    plt.show()


def diag():
    return np.array(list(list(0 if x < y else 255 for x in np.arange(0, 20)) for y in np.arange(0, 20)))


def fft2d(s):
    return fft(fft(s))


if __name__ == '__main__':
    main()
