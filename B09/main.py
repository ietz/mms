import numpy as np
import matplotlib.pyplot as plt


def main(n=10000):
    under_c_count = 0
    probability_history = []

    for i in range(n):
        b = np.random.randint(3)
        c = np.random.randint(3)
        # remaining = [0, 1, 2]
        # remaining.remove(b)
        # if c in remaining:
        #     remaining.remove(c)
        # uncovered = np.random.choice(remaining)
        if c == b:
            under_c_count += 1

        probability_history.append(under_c_count / (i+1))

    print("Wins by switching: {}".format(n - under_c_count))
    print("Wins by staying:   {}".format(under_c_count))

    plt.plot(probability_history)
    plt.show()


if __name__ == '__main__':
    main()
