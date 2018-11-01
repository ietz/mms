import numpy as np
from scipy.io import wavfile

duration_s = 3


def main():
    make_signal([400], sampling_rate=12000)
    for frequencies in [[400], [630], [800], [400, 630], [400, 800], [400, 405]]:
        make_signal(frequencies)


def make_signal(frequencies, sampling_rate=6000):
    sampling_points = np.linspace(0, duration_s, sampling_rate*duration_s)
    signal = np.mean(list(map(lambda f: np.cos(2*np.pi*sampling_points*f), frequencies)), axis=0)
    filename = "signal_{}_{}.wav".format(str(sampling_rate), '_'.join(map(str, frequencies)))
    wavfile.write(filename, sampling_rate, signal)


if __name__ == '__main__':
    main()
