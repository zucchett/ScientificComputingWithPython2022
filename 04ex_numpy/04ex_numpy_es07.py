# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:32:08 2022

@author: Ruben
"""

import numpy as np

num=np.arange(99)

mask=np.ones(99)

for i in range (99):
    for j in range(2,i):
        if i % j == 0:
            mask[i]=0
          
mask_bool=np.array(mask, bool) 
         
print(num[mask_bool])

