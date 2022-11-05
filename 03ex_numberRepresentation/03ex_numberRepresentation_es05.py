#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 16:03:16 2022

@author: alessandra
"""

#%% es05

import numpy as np

def quadSol_a(a, b, c):
    x_p = (- b + np.sqrt(b ** 2. - 4. * a * c))/(2. * a)
    x_n = (- b - np.sqrt(b ** 2. - 4. * a * c))/(2. * a)
    return [x_p, x_n]

print("Solutions [1st method]: ", quadSol_a(0.001, 1000, 0.001))

def quadSol_b(a, b, c):
    """ Multiply & divide x_p for negative numerator,
        multiply & divide x_n for positive numerator """
    x_p = (- b + np.sqrt(b ** 2. - 4. * a * c))/(2. * a)*(- b - np.sqrt(b ** 2. - 4. * a * c))/(- b - np.sqrt(b ** 2. - 4. * a * c))
    x_n = (- b - np.sqrt(b ** 2. - 4. * a * c))/(2. * a)*(- b + np.sqrt(b ** 2. - 4. * a * c))/(- b + np.sqrt(b ** 2. - 4. * a * c))
    #return (- b - np.sqrt(b ** 2. - 4. * a * c))/(- b - np.sqrt(b ** 2. - 4. * a * c)), (- b + np.sqrt(b ** 2. - 4. * a * c))/(- b + np.sqrt(b ** 2. - 4. * a * c))
    return [x_p, x_n]

print("Solutions [2nd method]: ", quadSol_b(0.001, 1000, 0.001))

print("#####")
print("""The results are different because of the problems that occur in
      python when doing calculations with floats and when doing operations
      with small and big numbers (associative does not necessarily hold
                                  and distributive law does not hold)""")
print("""For the final method take the solution with plus sign from the 2nd method
      and the solution with minus sign from the 1st method to avoid doing
      operations with small and big numbers""")
print("#####")


def quadSol(a, b, c):
    # x_p = 4.*a*c/(2.*a*(-b-np.sqrt(b**2.-4.*a*c)))
    x_p = (- b + np.sqrt(b ** 2. - 4. * a * c))/(2. * a)*(- b - np.sqrt(b ** 2. - 4. * a * c))/(- b - np.sqrt(b ** 2. - 4. * a * c))
    x_n = (- b - np.sqrt(b ** 2. - 4. * a * c))/(2. * a)
    return [x_p, x_n]

print("Solutions [final method]: ", quadSol(0.001, 1000, 0.001))
    

