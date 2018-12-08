import numpy as np
import matplotlib.pyplot as plt


def main():
    ks = [1, 2, 3]
    x = np.linspace(-6, 6, 5000)

    fig, axs = plt.subplots(len(ks), 1, figsize=(6, 6))
    axs = axs.ravel()

    for i, k in enumerate(ks):
        ax = axs[i]
        ax.set_title("l={}".format(2*k+1))

        s_reconstructed = np.zeros_like(x)
        for offset in np.arange(-k, k+1):
            sinc = np.sinc(x + offset)
            s_reconstructed += sinc
            ax.plot(x, sinc, '--')

        s = np.ones_like(x)

        ax.plot(x, s)
        ax.plot(x, s_reconstructed, linewidth=2)
        ax.grid(True, which='both', linestyle='dashed')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

    plt.show()


if __name__ == '__main__':
    main()
