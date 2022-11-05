# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:35:32 2022

@author: Federico
"""

import math
u_x=float(input("Insert u_x"))
u_y=float(input("Insert u_y"))
v_x=float(input("Insert v_x"))
v_y=float(input("Insert v_y"))
d=math.sqrt((u_x-v_x)**2+(u_y-v_y)**2)
print(d)