# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:11:02 2022

@author: Umut Berk Cakmakci
"""

# 03ex_numberRepr_es01
"""
print("\n03ex_es01 answer:\n--------------------------------------------------")

b = str("b")
d = str("d")
h = str("h")

y = input("enter your number: ")
x = str(input("enter your output type-b-d-h: "))

try:
    value = int(y, 10)  
except:
    try:
        value = int(y, 2)
    except:
        try:
            value = int(y, 16)
        except:
            print("please enter a valid number!")

if(x==b):
    print("the new value is:",bin(value))
elif(x==h):
    print("the new value is:",hex(value))
else:
    print("the new value is:",int(value))
"""

# 03ex_numberRepr_es02
"""
print("\n03ex_es02 answer:\n--------------------------------------------------")

def convert_func(val):
        try:
            sign = int(val[0])          # segno, 1 bit
            exp = int(val[1:9],2)       # esponente, 8 bits
            mant = int("1"+val[9:], 2)  # mantissa, len(val)-9 bits
            return (-1)**sign * mant /( 1<<( len(val)-9 - (exp-127) ))
            
        except:
            print("ERROR!")

num1 = "110000101011000000000000" 
num2 = "110000011010010011"
print("Single precision floating point in decimal representation \nfor number 1:", convert_func(num1), "\nfor number 2:", convert_func(num2)) 
"""

# 03ex_numberRepr_es03
"""
print("\n03ex_es03 answer:\n--------------------------------------------------")

import sys

overflow=0
res=0

while(True):
    try:
        res=2**overflow
        overflow=overflow+0.001
    except OverflowError:
        break

print("\nReal overflow value: ", sys.float_info.max)
print("Overflow value: ", 2**(overflow-0.001))

underflow=0
res2=0

while(True):
    try:
        res2=1/(2**underflow)
        underflow=underflow+0.001
    except:
        break

print("\nReal underflow value: ", sys.float_info.min)
print("Underflow value: ", 1/(2**(underflow-0.001)))
"""

# 03ex_numberRepr_es04
"""
print("\n03ex_es04 answer:\n--------------------------------------------------")

delta = 1
z=0
while delta > 1e-20:
    if 1 + delta == 1:
        print('1 +', delta, "  = 1")
        flag = delta/0.1
        break
    else:
        print('1 +', delta, "  != 1")
    z+=1
    delta=delta*0.1
print("The machine precision for floating point numbers is up to ", z, "th digit after the point.")
"""

# 03ex_numberRepr_es05
"""
print("\n03ex_es05 answer:\n--------------------------------------------------")

import math

a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

s11 = ((b**2)-(4*a*c))
s1 = math.sqrt(abs(s11))
print("\n03ex_es05_part-a")
if a==0:
    print("Please enter valid input for a!")

else: 
    if s11 < 0:
        x1 = ((-1)*b)/(2*a)
        x2 = ((-1)*b)/(2*a)
        print("x1  :", x1, " + i", s1/(2*a), "\nx2  :", x2, " - i", s1/(2*a))
    
    else:
        x1 = ((-1)*b + s1)/(2*a)
        x2 = ((-1)*b - s1)/(2*a)
        print("x1  :", x1, "\nx2  :", x2)

print("\n03ex_es05_part-b")
x11 = ((-1)*b + s1)*((-1)*b + s1)/(2*a)*((-1)*b + s1)
x22 = ((-1)*b - s1)*((-1)*b - s1)/(2*a)*((-1)*b - s1)
print("x1' :", x11, "\nx2' :", x22)

#print("\nThe results (x1,x2) and (x1',x2') are different from each other,"+
#      " because the Python does the operations in order. If we don't introduce "+
#      "multiplication in the denominator to python as a whole, it will only do "+
#      "the division operation in the first order, while the other operation will "+
#      "behave like the multiplication operation. If we provide transaction integrity "+
#      "with a parenthesis, we will eliminate the problem.")

# the results (x1,x2) and (x1',x2') are different from each other, 
# because the Python does the operations in order. 
# If we don't introduce multiplication in the denominator to python as a whole, 
# it will only do the division operation in the first order, 
# while the other operation will behave like the multiplication operation. 
# If we provide transaction integrity with a parenthesis, we will eliminate the problem.


x11 = (((-1)*b + s1)*((-1)*b + s1))/((2*a)*((-1)*b + s1))
x22 = (((-1)*b - s1)*((-1)*b - s1))/((2*a)*((-1)*b - s1))
print("\nx1'':", x11, "\nx2'':", x22)
"""

# 03ex_numberRepr_es06
"""
print("\n03ex_es06 answer:\n--------------------------------------------------")
print("\nEx03_es06_part-a:\n")

def f(x):   
    return (x*(x-1))

def deriv_f(x, delta):
    return (f(x+delta)-f(x))/delta

print("The result of the derivative for delta=10^-2 is : ",deriv_f(1, 10**-2))

# In the floating point displays, there might be some arithmetical errors.
# The reason is that decimal values are stored as formulas and have no precise representation.

print("\nEx03_es06_part-b:\n")

print("The result for delta=10^-4 is : ", deriv_f(1, 10**-4))
print("The result for delta=10^-6 is : ", deriv_f(1, 10**-6))
print("The result for delta=10^-8 is : ", deriv_f(1, 10**-8))
print("The result for delta=10^-10 is: ", deriv_f(1, 10**-10))
print("The result for delta=10^-12 is: ", deriv_f(1, 10**-12))
print("The result for delta=10^-14 is: ", deriv_f(1, 10**-14))

# at one point at 10^-8, we got the best accurate point. 
# before and after that, the result is worse than 10^-8.
# in floating points, up to 8th digits are meaningful. 
"""

# 03ex_numberRepr_es07
"""
print("\n03ex_es07 answer:\n--------------------------------------------------")

import math
import timeit

def delta_x(N):
    return (x2-x1)/N

def integrate(x,N):
    n=0
    A= 0.0
    j = abs ((x2-x1)/delta_x(N))
    i = int (j)
    while n < i:
        delta_A = math.sqrt(1-x**2)*delta_x(N)
        x = x + delta_x(N)
        A = A + delta_A
        n = n+1
    return A

x1, x2 = -1, 1
N1, N2 = 100, 10000

print("\nEx03_es07_part-a:\n")
print("True result              :", math.pi/2)
print("Integral result for N=100:", integrate(x1,N1))

# The calculated result is 0.01 less than the true result. This result is obtained
# in 100 iterations. If we do more iterations, that we will get much closer results
# to the true value. 

time=0
flagTmp=True

while(time < 1):

    time = timeit.timeit(stmt='integrate(x1, N2)', globals=globals(), number=1)

    if(time<0.5):
        N2=N2+1000000
    if(time<0.8):
        N2=N2+100000
    if (time<0.9):
        N2=N2+10000
    else:
        N2=N2+100

print("\nEx03_es06_part-b:\n")
print("True result                    :", math.pi/2)
print("Integral result for N=", N2, ":", integrate(x1,N2))
print("final N value:", N2)
print(time, "s")

# When we do it more than 1M iterations, we almost got the same result, less than 1 second. 
# If we keep doing the iterations for 1 minute, I think we can get the exact same result. 
"""


