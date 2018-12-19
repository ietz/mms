import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as spimage


def main():
    img = np.load('lena.npy')

    lmbdas = [1.0, 2.0, 4.0, 6.0]
    a_s = [0.5, 1.0, 2.0, 4.0]
    betas = [0.125, 0.25, 0.5, 1]

    for lmbda in lmbdas:
        fig, axs = plt.subplots(len(a_s), len(betas), figsize=(10, 10))
        fig.suptitle("lambda={}".format(lmbda))

        for ia, a in enumerate(a_s):
            for ibeta, beta in enumerate(betas):
                x = np.arange(-32, 32)
                y = np.arange(-32, 32)
                xv, yv = np.meshgrid(x, y)

                theta = 45*(np.pi/180)

                b = 2**beta
                w0 = 2*np.pi / lmbda
                sgm = (a*(b+1))/(w0*(b-1))
                wx, wy = np.cos(theta)/lmbda, -np.sin(theta)/lmbda

                g = gsin(xv, yv, wx, wy, sgm)

                frq = spimage.convolve(img, g)
                frq += 128

                ax = axs[ibeta][ia]
                ax.imshow(frq, cmap='gray')
                ax.set_title("a={}, beta={}".format(a, beta))

        plt.savefig('lambda_{}.png'.format(lmbda), dpi=300)


def gsin(x, y, wx, wy, sgm):
    return np.sin(wx*x + wy*y) * gauss(x, sgm) * gauss(y, sgm)


def gcos(x, y, wx, wy, w0, sgm):
    gxy = gauss(x, sgm) * gauss(y, sgm)
    nadjusted = np.cos(wx*x + wy*y) * gxy
    a0 = np.sum(nadjusted) / np.sum(gxy)

    return nadjusted - a0 * gxy


def gauss(x, sigma):
    return 1 / np.sqrt(2 * np.pi * sigma**2) * np.exp(-x**2/(2 * sigma**2))


if __name__ == '__main__':
    main()
