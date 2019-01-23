import numpy as np
from matplotlib import pyplot as plt


def main():
    M = 10000
    N = 10
    samples = 0.5 * (np.random.randn(M, N)**2 + np.random.randn(M, N)**2)

    hist = []

    for i in range(2, N+1):
        hist.append(1/np.mean(samples[:, :i]))

    plt.plot(hist)
    plt.show()


if __name__ == '__main__':
    main()
