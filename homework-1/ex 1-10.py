# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:04:32 2022

@author: gozde
"""

import math
def normalize(vector):
    sqrsum = sum([i*i for i in vector])
    return tuple([i/math.sqrt(sqrsum) for i in vector])

print(normalize((17,15,19)))