import numpy as np

a = np.linspace(0, 2*np.pi, 100)
print(a, '\n')
b = a[9::10]
print(b, '\n')
c = a[::-1]
print(c, '\n')
mask = np.absolute(np.sin(a) - np.cos(a)) < 0.1
d = a[mask]
print(d, '\n')

import matplotlib.pyplot as plt
i = np.where(mask)     # Finding where sin and cos are close.
plt.plot(a, np.sin(a), '-bD', markevery=i[0].tolist(), label = 'sin')
plt.plot(a, np.cos(a), '-gD', markevery=i[0].tolist(), label = 'cos')
plt.plot(a, np.absolute(np.sin(a) - np.cos(a)), '-rD', markevery=i[0].tolist(), label = 'abs(sin-cos)')
plt.legend()
plt.grid()
plt.axis([0, np.pi*2, -1.1, 1.5])