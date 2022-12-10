#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:24:26 2022

@author: alessandra
"""

#%% ex04
# Use np.linspace to create an array of 100 numbers between  0  and
#  2pi (inclusive).

# Extract every 10th element using the slice notation
# Reverse the array using the slice notation
# Extract elements where the absolute difference between the sin and cos
# functions evaluated for that element is <0.1 
# Optional: make a plot showing the sin and cos functions and indicate
# where they are close

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.,2.*np.pi,100)
print(" Array of 100 numbers between 0 and 2pi",'\n', x)

slice_x  = x[::10]
print("Extract every 10th element: ", '\n', slice_x)

reverse_x = x[::-1]
print("Reverse array: ",'\n', reverse_x)

mask = np.abs(np.cos(x)-np.sin(x))<0.1
masked_x = x[mask]
print("Extract elements (fancy indexing): ",'\n', masked_x)


sin_f = np.sin(x)
cos_f = np.cos(x)

x_0 = [np.pi/4., 5.*np.pi/4.]
y_0 = [np.cos(np.pi/4.),np.cos(5.*np.pi/4.)]

plt.plot(x,sin_f,x,cos_f, zorder = -1)
plt.scatter(x_0, y_0, marker = (5,2), zorder = 1, color = "g")
plt.xlabel('x values from 0 to 2pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 2pi')
plt.legend(['sin(x)', 'cos(x)']) 
plt.show()
