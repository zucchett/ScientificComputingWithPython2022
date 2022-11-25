# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:46:18 2022

@author: Ruben
"""

import numpy as np

m= np.random.rand(10,2)*3
print(m)
print("\n\n")
mask=(m < 0.3)
m[mask]=0
print(m)