#Zuccolo Giada, matr. 2055702
# EXE 6
from sympy import *

def function_f(x):
    return (x * (x - 1))

def calculate_delta(x):
    return (10**-x)
x = 1
expo = 2
lim = limit((function_f(x + calculate_delta(expo)) - function_f(x)) /
            calculate_delta(expo), x, 0)
print("PART a)\n Result of lim = ", round(lim, 4))

print("PART b)")
c=0
while c<6:
    expo = expo+2
    lim = limit((function_f(x + calculate_delta(expo)) - function_f(x)) / calculate_delta(expo), x, 0)
    print("Delta = 10^-"+str(expo)+"\t-> result of lim = "+str(lim))
    c+=1
