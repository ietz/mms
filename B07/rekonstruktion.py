import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axs = plt.subplots(3, 1, figsize=(6, 6))
    axs = axs.ravel()



    zeichne(1)
    zeichne(2)
    zeichne(3)


def zeichne(k):
    plt.gcf().set_size_inches(10, 3)

    x = np.linspace(-6, 6, 5000)
    fR = np.zeros_like(x)

    for offset in np.arange(-k, k+1):
        sinc = np.sinc(x + offset)
        fR += sinc
        plt.plot(x, sinc, '--')

    s = np.ones_like(x)
    plt.plot(x, s)

    plt.plot(x, fR)
    plt.show()


if __name__ == '__main__':
    main()
