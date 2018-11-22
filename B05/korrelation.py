import numpy as np
import matplotlib.pyplot as plt


def main():
    fig, axs = plt.subplots(5, 1, figsize=(6, 6))
    axs = axs.ravel()

    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    sinA = np.sin(x)

    for i, delta in enumerate(np.arange(5) * np.pi/4):
        sinB = np.sin(x-delta)

        prod = sinA * sinB

        axs[i].plot(x, sinA, '--')
        axs[i].plot(x, sinB, '--')
        axs[i].plot(x, prod)

    fig.show()


if __name__ == '__main__':
    main()
