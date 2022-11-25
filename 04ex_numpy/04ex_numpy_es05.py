# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:02:41 2022

@author: Ruben
"""

import numpy as np

m = np.arange(1,11)*(np.arange(1,11)[:,np.newaxis])
print(m)
trace=0
for i in range(10):
    trace += m[i,i]

print(trace)

anti_id=np.flip(np.identity(10, bool),0)
print(m[anti_id])

idd=np.identity(9)

np.append(idd, np.zeros(9)[:,np.newaxis], axis=1)
np.append(idd, np.zeros(10), axis=0)
#print(np.r_[np.zeros(10), mid ])
