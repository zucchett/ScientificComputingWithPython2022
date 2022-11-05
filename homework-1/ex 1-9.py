# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 23:54:51 2022

@author: gozde
"""

pythagorean = []
m = 2
c = 0
while (c < 100):
  for n in range(1, m+1):
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n
    if (c > 100):
        break
    if (a==0 or b==0 or c==0):
        break
    
    pythagorean.append((a,b,c))
    
  m = m + 1

print(tuple(pythagorean))