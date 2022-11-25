# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:03:28 2022

@author: Ruben
"""
import numpy as np

u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])

print("Matrice ottenuta con outer()")
print(np.outer(u,v))

m=np.eye(4)
for i in range (4):
    for j in range(4):
        m[i,j]=u[i]*v[j]
        
print("\nMatrice ottenuta con cicli for")
print(m)

matrice=np.array([u[i]*v[j] for i in range(4) for j in range(4)]).reshape(4,4)
print("\nMatrice ottenuta con list comprehension")
print(matrice)
print("\nMatrice ottenuta con opreazioni di broadcasting")
print( u[:,np.newaxis]*v )
        
