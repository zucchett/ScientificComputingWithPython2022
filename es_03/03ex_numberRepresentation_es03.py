# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:53:45 2022

@author: Federico
"""

under = 1.
over = 1.

while (under != 0): 
    under = under/2 
    if (under != 0):
        #print(under)
        u_limit = under
    if (under == 0):
        print("Reached underflow limit =", u_limit)
        
while (over != float("inf")):
    over = float(over*2)
    if (over != float("inf")):
        #print(over)
        o_limit = over
    if (over == float("inf")):
        print("Reached overflow limit =", o_limit)