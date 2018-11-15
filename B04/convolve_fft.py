import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt


def main():
    input_start, input_end = -2.5*np.pi, 2.5*np.pi
    step_size = (input_end - input_start) / 5000

    s_cos = np.cos(np.arange(input_start, input_end, step_size))
    s_rect = np.ones(round(1/step_size))

    n = len(s_cos) + len(s_rect) - 1
    con = np.convolve(s_rect, s_cos)
    con_fft = ifft(fft(s_rect, n=n) * fft(s_cos, n=n))

    xs = np.arange(input_start, input_start + n*step_size, step_size)
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.plot(xs, con, label="Convolution in TD", linewidth=5)
    ax.plot(xs, con_fft, dashes=[5, 5], label="Multiplication in FD", linewidth=5)
    ax.legend(loc='upper left')
    fig.show()
    # fig.savefig('convolve_fft.png', dpi=300)


if __name__ == '__main__':
    main()
