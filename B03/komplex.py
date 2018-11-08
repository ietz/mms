import math
import numpy as np


def main():
    mache_aufgaben(1+1j*math.sqrt(3), 1-1j)
    mache_aufgaben(2+3j, 3-5j)
    mache_aufgaben(4-5j, 4+5j)
    mache_aufgaben(1j, -2-4j)


def mache_aufgaben(x, y):
    print('x = {: .4f}, y = {: .4f}'.format(x, y))
    print(' x + y = {: .4f}'.format(x+y))
    print(' x - y = {: .4f}'.format(x-y))
    print(' x * y = {: .4f}'.format(x*y))
    print(' x / y = {: .4f}'.format(x/y))
    print('x\' * y = {: .4f}'.format(np.conj(x) * y))
    print('x / y\' = {: .4f}'.format(x / np.conj(y)))
    print(end='\n\n')


if __name__ == '__main__':
    main()
