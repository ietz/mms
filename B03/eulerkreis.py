import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, ax = plt.subplots()

    for n in [1, 5, 10, 50, 100]:
        basis = 1 + 1j*np.pi/n
        pts = basis**np.arange(n+1)
        ax.plot(pts.real, pts.imag, label='n={}'.format(n))

    ax.set_aspect('equal', 'datalim')
    ax.grid(True, which='both', linestyle='dashed')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.legend(loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()
