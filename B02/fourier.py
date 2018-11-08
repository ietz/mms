import numpy as np
from matplotlib import pyplot as plt


def main():
    p = 50001
    x = np.linspace(-1, 1, p)
    f = np.sign(x)

    plt.figure(figsize=(5, 4))
    plt.plot(x, f, linewidth=1, zorder=100, label="target")

    for n in [1, 5, 10, 100]:
        g = approximate(x, n)
        plt.plot(x, g, linewidth=1, label='n={}'.format(n))
        print('n={:02d} has {} intersections'.format(n, len(get_intersections(x, f, g))))

    plt.legend(loc='upper left')
    plt.show()


def approximate(x, n):
    result = np.zeros_like(x)
    for k in range(1, n, 2):
        result = result + 4 / np.pi * np.sin(k * np.pi * x) / k
    return result


def get_intersections(x, f, g):
    return list(map(lambda i: x[i], np.where(np.diff(np.signbit(f - g)))[0]))


if __name__ == '__main__':
    main()
