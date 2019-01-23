import numpy as np
import matplotlib.pyplot as plt


def main():
    global out

    Ls = [32, 256, 1024]

    fig, axs = plt.subplots(len(Ls), 1, figsize=(6, 6))
    axs = axs.ravel()

    for i, L in enumerate(Ls):
        signals = np.random.randn(1000, L)
        X = np.fft.rfft(signals)
        Per = np.abs(X)**2 / L

        ax = axs[i]
        ax.set_title("L={}".format(L))
        ax.plot(np.var(Per, 0))
        ax.grid(True, which='both', linestyle='dashed')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

    plt.show()


if __name__ == '__main__':
    main()
