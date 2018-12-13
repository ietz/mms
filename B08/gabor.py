import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as spimage


def main():
    print("")



def gcos(x, y, wx, wy, b):
    return np.sin(wx*x + wy*y) * gauss(x, sigma(wx, b)) * gauss(y, sigma(wy, b))


def sigma(w0, b, a=1.0):
    return (a*(b+1))/(w0*(b-1))


def kernel(x, lmbda, beta, a=1.0):
    w0 = 2*np.pi / lmbda
    b = np.power(2, beta)
    sigma = (a*lmbda*(b+1)) / (2*np.pi*(b-1))
    return gauss(x, sigma)


def gauss(x, sigma):
    return 1 / np.sqrt(2 * np.pi * sigma**2) * np.exp(-x**2/(2 * sigma**2))


img = np.load('lena.npy')


x = np.arange(-15, 15)  # img.shape[0])
y = np.arange(-15, 15)  # img.shape[1])
xv, yv = np.meshgrid(x, y)

g = gcos(xv, yv, 0.5, 0.5, 3)
plt.imshow(g)
plt.show()

frq = spimage.convolve(img, g)
frq += 128

plt.imshow(frq, cmap='gray')
plt.show()


if __name__ == '__main__':
    main()
