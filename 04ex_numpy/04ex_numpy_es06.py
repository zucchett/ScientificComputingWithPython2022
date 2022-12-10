#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:50:31 2022

@author: alessandra
"""

#%% ex06
# Use broadcasting to create a grid of distances.

# Route 66 crosses the following cities in the US: Chicago, Springfield,
# Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque,
# Flagstaff, Los Angeles.

# The corresponding positions in miles are:
# 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448

# Build a 2D grid of distances among each city along Route 66
# Convert the distances in km

import numpy as np

a = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
b = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

#grid = np.array([np.abs(a[i]-b[j]) for i in range(len(a)) for j in range(len(b))]).reshape(10,10)
grid = np.abs(a.reshape(10,1)-b)
print("2D grid with distances in miles: ",'\n', grid,'\n')

gridKm = (np.array(grid)*1.60934).reshape(10,10)
print("2D grid with distances in km: ",'\n',gridKm)
