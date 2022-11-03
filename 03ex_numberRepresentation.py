import os
import timeit

# 1. Number representation

def converter(x:int):
    
    bin_x = bin(x)
    hex_x = hex(x)
    print("Binary representation: " + str(bin_x))
    print("Hexadecimal representation: " + str(hex_x))
    print('Decimal representation of', bin_x, ':', int(bin_x, 2))
    print('Decimal representation of', hex_x, ':', int(hex_x, 16))
    
no = int(input("Enter an integer: "))
converter(no)

# 2. 32-bit floating point number

str_32bit_bi = "110000101011000000000000"

def convertion(string):
    if string[0] == "1":
        sign = -1 
    else:
        sign = 1
    exp_bin = ""
    
    for i in range(1, 9):
        exp_bin = exp_bin + string[i]
    mantissa_bin = ""
    
    for i in range(9, 31):
        mantissa_bin = mantissa_bin + string[i]
    exp = int(exp_bin, 2)
    mantissa = 1

    counter = 1
    for i in mantissa_bin:
        mantissa = mantissa + (int(i) / 2**counter) 
        counter = counter + 1
    mantissa = mantissa * sign
    
    print("Sign: " + str(sign))
    print("Exponent: " + str(exp))
    print("Mantissa: " + str(mantissa))
    return mantissa * (2**(exp-127))

print("Result: " + str(convertion("00000011111000000000000000000000")) + "\n")

print("Result: " + str(convertion("11000000101100000000000000000000")))

# 3. Underflow and overflow

var1 = 1.0
var2 = 1.0

print("I couldn't make this part work.")

# 4. Machine precision

print("Because of the previous part, I also couldn't make this part work.")

# 5. Quadratic solution

from math import sqrt

def quadraticEqn(a, b, c):
    x_1 = (-b + ((b**2 - 4*a*c)**(1/2))) / (2*a)
    x_2 = (-b - ((b**2 - 4*a*c)**(1/2))) / (2*a)
    print("x_1: " + str(x_1))
    print("x_2: " + str(x_2))

# a)

a = 0.001
b = 1000
c = 0.001
print("a: " + str(a) + " b: " + str(b) + " c: " +str(c))

quadraticEqn(a, b, c)
print("\n")

# b)

def quadraticEqn2(a, b, c):
    x_1_1 = ((-b + (b**2 - 4*a*c)**(1/2)) * (-b + ((b**2 - 4*a*c)**(1/2)))) / ((2*a) * (-b + ((b*b - 4*a*c)**(1/2))))
    x_1_2 = ((-b + (b**2 - 4*a*c)**(1/2)) * (-b - ((b**2  - 4*a*c)**(1/2)))) / ((2*a) * (-b - ((b*b - 4*a*c)**(1/2))))
    x_2_1 = ((-b - (b**2 - 4*a*c)**(1/2)) * (-b + ((b**2  - 4*a*c)**(1/2)))) / ((2*a) * (-b + ((b*b - 4*a*c)**(1/2))))
    x_2_2 = ((-b - (b**2 - 4*a*c)**(1/2)) * (-b - ((b**2  - 4*a*c)**(1/2)))) / ((2*a) * (-b - ((b*b - 4*a*c)**(1/2))))
    print("x_1_1: "+ str(x_1_1))
    print("x_1_2: "+ str(x_1_2))
    print("x_2_1: "+ str(x_2_1))
    print("x_2_2: "+ str(x_2_2))

print("a: " + str(a) + " b: " + str(b) + " c: " + str(c))

quadraticEqn2(a, b, c)
print("\n")

# x_2 in first function = -999999.999999
# x_2 in second function = -999999.9999990001
# the reason is for the floats, they have a limited decimal storage in memory
# that's why we see this difference only in this case

# c)

def computing_roots(a, b, c):
    d = (b**2) - (4*a*c)
    x_1 = (-b + sqrt(d)) / (2*a)
    x_2 = (-b - sqrt(d)) / (2*a)
    print("x_1: " + str(x_1))
    print("x_2: " + str(x_2))

print("a: " + str(a) + " b: " + str(b) + " c: " + str(c))
computing_roots(a, b, c)

# 6. The derivative

def func(x):
    return x * (x-1)

def derivative(func, x, delta = 10**(-2)):
    dx = delta
    return (func(x + delta) - func(x)) / dx

# a)

x = 1
result = derivative(func, x)
print("Derivative of f (func): " + str(result) + "\n")
deriv = 2*x - 1
print("Derivative of f (math) = " + str(deriv) + "\n")

# b)

deltaList = [10**(-4), 10**(-6), 10**(-8), 10**(-10), 10**(-12), 10**(-14)]

for i in deltaList:
    print("Derivative on " + str(i) + " = " + str(derivative(func, x, i)))
    
# 7. Integral of a semicircle

from math import pi
from cmath import phase

def semiCircle(x):
    return (1-(x**2))**(1/2)

def integral(N, lower_limit, upper_limit, func):
    result = 0
    h = (upper_limit - lower_limit) / N
    
    for i in range(N):
        result = result + h * func(i)
    return phase(result)

# a)

N = 100
lower_limit = -1
upper_limit = 1

print("Result of integral: " + str(integral(N, lower_limit, upper_limit, semiCircle)))
print("Result of pi/2" + str(pi/2))

print("\n" + "The difference between the results is 0.0.00020214747")

# b)

start_time1 = timeit.default_timer()
integral(N*12000, lower_limit, upper_limit, semiCircle)
duration1 = timeit.default_timer() - start_time1

start_time2 = timeit.default_timer()
integral(N*12000*100, lower_limit, upper_limit, semiCircle)
duration2 = timeit.default_timer() - start_time2

print(str(duration1) + "\n" + str(duration2))

print("For less than 1 s, N has to be multiplied with 12000" + "\n"
     + "For 1 m, N has to be multiplied with 1200000")
     

