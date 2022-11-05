# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 12:44:26 2022

@author: Ruben
"""

d = [(a,b,c)
     for c in range(1,100)
     for a in range(1,100)
     for b in range(1,100)
         if a**2+b**2==c**2
     ]


e=tuple(d)

print(e)