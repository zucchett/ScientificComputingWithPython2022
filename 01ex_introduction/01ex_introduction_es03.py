#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:45:35 2022

@author: alessandra
"""

#%%es03
import math

u = (3,4)
v = (1,2)

def distance(u,v): # calculate euclidean distance
    return math.sqrt((u[0]-v[0])**2.+(u[1]-v[1])**2.) 

print(distance(u,v))