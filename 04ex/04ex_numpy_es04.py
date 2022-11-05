# Trigonometric functions

import numpy as np
import math as m
import matplotlib.pyplot as plt

a = np.linspace(0, 2*m.pi, 100)

a10 = a[9::10]
arev = a[::-1]

mask = (abs(np.sin(a)-np.cos(a)) < 0.1)
afil = a[mask]

print("Original array:")
print(str(a) + "\n")
print("Every 10th element:")
print(str(a10) + "\n")
print("Reversed array:")
print(str(arev) + "\n")
print("Elements such that |sin(x)-cos(x)|<0.1:")
print(str(afil) + "\n")

plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.show()

print("The two functions are indeed very close around the filtered region (x~0.8 and x~3.8)")
