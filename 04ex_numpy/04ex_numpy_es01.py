# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:25:48 2022

@author: Ruben
"""

import numpy as np

m = np.arange(12).reshape((3,4))
f=m.flatten()
print(m)
print("\n")
print(f)
print("\n")
for i in range(m.shape[1]):
    print("media sulla %d esima colonna è %.2f" %(i+1, m[:,i].mean()))
print("\n")
i=0
for i in range(m.shape[0]):
    print("media sulla %d esima riga è %.2f" %(i+1, m[i].mean()))
i=0
print("\nLa media di tutti gli elementi è ", f.mean())