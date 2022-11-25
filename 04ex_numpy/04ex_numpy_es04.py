# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:21:09 2022

@author: Ruben
"""

import numpy as np
import math
import matplotlib.pyplot as plt

array=np.linspace(0, 2*math.pi, 100)

sliced=array[::10]
reverse=sliced[:,np.newaxis]
mask=(abs( np.sin(array)- np.cos(array)) < 0.1)
filtered=array[mask]

print(array)
print("\n")
print(reverse)
print(sliced)
print("\n")
print(filtered)

plt.plot(array, np.sin(array))
plt.plot(array, np.cos(array))