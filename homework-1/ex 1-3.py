# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:17:23 2022

@author: gozde
"""

import math

def EuclideanDistance(u,v):
    z = math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
    print (z)

x = (5,0)
y = (0,12)

EuclideanDistance(x, y)
