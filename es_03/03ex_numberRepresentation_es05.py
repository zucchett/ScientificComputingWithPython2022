# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:46:02 2022

@author: Federico
"""

import math

def q_solution_1(a,b,c):
    x_1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x = [x_1,x_2]
    return x

def q_solution_2(a,b,c):
    x_1 = 2*c/(-b + math.sqrt(b**2 - 4*a*c))
    x_2 = 2*c/(-b - math.sqrt(b**2 - 4*a*c))
    x = [x_1,x_2]
    return x

print("direct formula", q_solution_1(0.001,1000,0.001))
print("alternative way", q_solution_2(0.001,1000,0.001))


"""
In the first method x_2 has at the numerator the difference of two numbers that are very close
This problem is solved in the second method, which shows anyway a similar problem for x_1 (this time at the denominator)
One can combine the two methods, giving accurate results for both solution (for this choice of (a,b,c))
"""

def q_solution(a,b,c):
    x_1 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = 2*c/(-b - math.sqrt(b**2 - 4*a*c))
    x= [x_1,x_2]
    return x

print("better way", q_solution(0.001,1000,0.001))
