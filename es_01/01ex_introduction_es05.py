# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:37:31 2022

@author: Federico
"""

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
unique=0
a=[]
i=0
while i<len(l):
    if l.count(l[i])==1:
        unique+=1; i+=1
        a.append(l[i])
    else: i+=1
print("The number of unique elements of the list is:",unique)
print("And the list of these elements is:",a)