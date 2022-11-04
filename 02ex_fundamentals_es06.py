# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:53:38 2022

@author: Ruben
"""

def square(x):
    return x**2

def cube(y):
    return y**3

def six_pow(z):
    return square(cube(z))

a=2

print(six_pow(a))


"""
x = input("Inserisci un numero: ")
print("la sesta potenza è ", six_pow(x))
"""