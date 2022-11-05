# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 08:48:21 2022

@author: gozde
"""

import math

under_flow = 1
for i in range(1500):
    x = under_flow / 2
    if x == 0:
        print("Underflow: ", under_flow)
        break
    else:
        under_flow = x

over_flow = 1.0
for i in range(10000):
    x = over_flow * 2
    if x == math.inf:
        print("Overflow: ", over_flow)
        break
    else:
        over_flow = x