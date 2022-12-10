#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:01:01 2022

@author: alessandra
"""

#%% ex08
# Consider a simple random walk process: at each step in time,
# a walker jumps right or left (+1 or -1) with equal probability.
# The goal is to find the typical distance from the origin of many
# random walkers after a given amount of time.

# Hint: create a 2D array where each row represents a walker,
# and each column represents a time step.

# Take 1000 walkers and let them walk for 200 steps
# Use randint to create a 2D array of size  walkers×steps  with values -1 or 1
# Calculate the walking distances for each walker (e.g. by summing the
# elements in each row)
# Take the square of the previously-obtained array (element-wise)
# Compute the mean of the squared distances at each step (i.e. the mean
# along the columns)
# Optional: plot the average distances ( (√distance**2) ) as a function
# of time (step)

import numpy as np
import random
import matplotlib.pyplot as plt

walk = [[random.randrange(-1, 2, 2) for i in range(200)] for j in range(1000)]

walkArr = np.array(walk).reshape(1000,200) # 200 steps (columns) 
print(walkArr)                              # 1000 walkers (rows)

sumWalkRow = walkArr.cumsum(axis=1)
print("\n Walking distance (sum along rows): \n", sumWalkRow)

squareArr = np.square(sumWalkRow)
print("\n Square array \n", squareArr)

meanArr = np.average(squareArr, axis=0)
print("\n Mean Array \n", meanArr)

avgDist = np.sqrt(meanArr)
timeStep = np.arange(200)

plt.scatter(timeStep, avgDist, marker = ".", zorder = 1, color = "g")
plt.xlabel('Step')
plt.ylabel('Average distance')
plt.title('Plot of avg dist vs step')
# plt.legend() 
plt.show()