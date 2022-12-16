from matplotlib import pyplot as plt
import numpy as np
import math

x = np.linspace(0,2*np.pi, num = 100)
print("This is matrix x:\n", x)
print("These are 10th elements:\n", x[9:100:10])
print("This is reversed x:\n", x[::-1])

sin = np.sin(x)
cos = np.cos(x)
j=  abs(abs(sin) - abs(cos))
mask = (j<.1)
print("These are extracted elements:\n", x[mask])


plt.scatter(x = x, y= sin, marker= "o", label = "Sin")
plt.scatter(x = x, y= cos, marker= "*", label = "Cos")
plt.legend()
plt.show()
