import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt


N = 2000
n_T = 120
F_s = N/n_T


def main():
    x = np.linspace(0, 2 * np.pi * n_T, N)
    s = np.sin(x)

    for D in [3, 5, 7, 8, 9, 10, 12]:
        fig, axs = plt.subplots(2, 1)
        fig.set_size_inches(10, 4)

        x_down = downsample(x, D)

        # Ohne Tiefpassfilter
        s_down = downsample(s, D)
        s_reconstructed = interpolate(s_down, D)

        axs[0].axhline(y=0, color='0.2')
        axs[0].plot(x, s, '--', color="C1", label='original')
        axs[0].stem(x_down, s_down, color="C2", label='downsampled')
        axs[0].plot(x, s_reconstructed, color="C3", label='reconstructed')
        axs[0].legend(loc='upper right')
        axs[0].set_xlim(0, 100)
        axs[0].set_ylim(-1.2, 1.2)
        axs[0].set_title('without lowpass')


        # Mit Tiefpassfilter
        s_filtered = lowpass(s, D)
        s_filtered_down = downsample(s_filtered, D)
        s_filtered_reconstructed = interpolate(s_filtered_down, D)

        axs[1].axhline(y=0, color='0.2')
        axs[1].plot(x, s, '--', color="C1", label='original')
        axs[1].plot(x, s_filtered, color="C4", label='lowpassed')
        axs[1].stem(x_down, s_filtered_down, color="C2", label='downsampled')
        axs[1].plot(x, s_filtered_reconstructed, color="C3", label='reconstructed')
        axs[1].legend(loc='upper right')
        axs[1].set_xlim(0, 100)
        axs[1].set_ylim(-1.2, 1.2)
        axs[1].set_title('with lowpass')

        plt.show()


def lowpass(s, D):
    return ifft(fft(s) * lowpass_freq(D))


def interpolate(s_down, D):
    return ifft(freq_extend(fft(s_down*D)))


def downsample(s, D):
    return s[::D]


def lowpass_freq(D):
    n_down = int(np.floor(N/D))
    return freq_extend(np.ones(n_down))


def freq_extend(f):
    n_front = int(np.ceil(len(f)/2))
    fill_len = np.zeros(N - len(f))
    return np.concatenate((f[:n_front+1], fill_len, f[n_front+1:]), axis=None)


if __name__ == '__main__':
    main()
