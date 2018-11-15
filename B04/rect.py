import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axs = plt.subplots(4, 1, figsize=(6, 6))
    axs = axs.ravel()

    for i, n in enumerate([2, 3, 4, 5]):
        xs, ys = rconv(n)
        axs[i].plot(xs, ys, linewidth=2)
        axs[i].set_xlim(-3.5, 3.5)
        axs[i].set_ylim(0, 1.1)
        axs[i].set_title("n={}".format(n))

    fig.tight_layout()
    fig.show()
    # fig.savefig('rect.png', dpi=300)


def rconv(n, a=100):
    s = np.ones(a)/a

    for i in range(n-1):
        s = np.convolve(s, s)

    xs = np.arange(-len(s)/a/2, len(s)/a/2, 1/a)
    return xs, s*a


if __name__ == '__main__':
    main()
