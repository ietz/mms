import numpy as np
from matplotlib import pyplot as plt

p = 1000
x = np.linspace(-1, 1, p)
f = np.sign(x)

plt.plot(x, f, color='blue', linewidth=2)

result = np.zeros_like(x)
n = 100
for k in range(1, n, 2):
    result = result + 4 / np.pi * np.sin(k * np.pi * x) / k

plt.plot(x, result, color='red')
plt.show()
