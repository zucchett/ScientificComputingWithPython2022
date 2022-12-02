import numpy as np
import math
import matplotlib.pyplot as plt

array = np.linspace(0,2*math.pi,100)
print("\n 0-2*math.pi arrey:\n ",array)

N_array = array[::10]
print("\n element_10th:\n",N_array)

reverse_N_array =N_array[::-1]
print("\n Reversed elements_10th:\n",reverse_N_array)

x_x = np.abs(np.sin(array)-np.cos(array)) < 0.1
print("\n Extracted elemens :","\n",array[x_x])

plt.scatter(array[x_x], np.sin(array[x_x]))
plt.plot(array, np.sin(array), array, np.cos(array))