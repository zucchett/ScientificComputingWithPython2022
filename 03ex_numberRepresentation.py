#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, exercises have to be solved by creating a dedicated `.py` file (or files) called `03ex_numberRepresentation.py`.
# 
# In case you need multiple files, name them `03ex_numberRepresentation_es01.py`, `03ex_numberRepresentation_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `03ex_numberRepresentation`. 
# 
# The exercises need to run without errors with `python3`.

# 1\. **Number representation**
# 
# Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.

# In[9]:


a = int(input("Enter a decimal number: "))

print(type(a))
a_bin = bin(a)
print('Binary representation of', a, ':', a_bin)

a_hex = hex(a)
print('Hexadecimal representation of', a, ':', a_hex)

print("")


print("Enter a binary number: ", end="")
b = input()
print(type(b))

b1 = int(b, 2)
b_hex = hex(b1)
print("Hexadecimal representation of",b, ":" ,b_hex)


b_dec = int(b, 2)
print("Decimal representation of", b, ":" ,b_dec)


print("")

print("Enter a hexadecimal number: ", end="")
c = input()
print(type(c))

c_dec = int(c, 16)
print("Decimal representation of", c, ":" ,c_dec)

c_bin = bin(c_dec)

print("Binary representation of", c, ":" ,c_bin)


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[10]:



def binaryOfFraction(fraction):
    binary = str()
    while (fraction):
        fraction *= 2
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
        else:
            int_part = 0
            
        binary += str(int_part)

    return binary

def floatingPoint(real_no):
    sign_bit = 0

    if(real_no < 0):
        sign_bit = 1


    real_no = abs(real_no)


    int_str = bin(int(real_no))[2 : ]

    fraction_str = binaryOfFraction(real_no - int(real_no))

    ind = int_str.index('1')

    exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ]

    mant_str = int_str[ind + 1 : ] + fraction_str

    mant_str = mant_str + ('0' * (23 - len(mant_str)))

    return sign_bit, exp_str, mant_str


if __name__ == "__main__":

    sign_bit, exp_str, mant_str = floatingPoint(110000101011000000000000)

    ieee_32 = str(sign_bit) + '|' + exp_str + '|' + mant_str

    print("IEEE 754 representation of 110000101011000000000000 is :")
    print(ieee_32)

       
        


def convertToInt(mantissa_str):

    power_count = -1

    mantissa_int = 0

    for i in mantissa_str:

        mantissa_int += (int(i) * pow(2, power_count))

        power_count -= 1

    return (mantissa_int + 1)

if __name__ == "__main__":

    ieee_32 = '0|11001011|0111010010110001111000001111100001111111110111001110001010000011000000000000'

    sign_bit = int(ieee_32[0])

    exponent_bias = int(ieee_32[2 : 10], 2)

    exponent_unbias = exponent_bias - 127
    
    mantissa_str = ieee_32[11 : ]

    mantissa_int = convertToInt(mantissa_str)

    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias)

    print("The float value of the given IEEE-754 representation is :",real_no)


# 3\. **Underflow and overflow**
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[11]:


print(" LOWEST IS  1.11254e-308 "
 "HIGHEST IS  8.98847e+307\n")
N = 1500
undflow = 1
ovflow = 1

for i in range(N):
    undflow = undflow / 2
    ovflow  = ovflow  * 2
    print(i,"\t\t","%1.5e"%undflow,"\t\t","%1.5e"%ovflow)


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[12]:


N = 20
var = 5
fac = 1e-1

for i in range(N):
    var = var + fac
    fac = fac * 1e-1
    print(i,"\t\t",var)
    
print("after 14th step there is no effect on the number") 


# 5\. **Quadratic solution**
# 
# Write a function that takes in input three parameters $a$, $b$ and $c$ and prints out the two solutions to the quadratic equation $ax^2+bx+c=0$ using the standard formula:
# $$
# x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
# $$
# 
# (a) use the function to compute the solution for $a=0.001$, $b=1000$ and $c=0.001$
# 
# (b) re-express the standard solution formula by multiplying the numerator and the denominator by $-b\mp\sqrt{b^2-4ac}$ and again find the solution for $a=0.001$, $b=1000$ and $c=0.001$. How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
# 
# (c) write a function that computes the roots of a quadratic equation accurately in all cases

# In[13]:


import math 
"""
## a)
a= float(input("enter number 'a'"))
print(a)
b = float(input("enter number 'b'"))
print(b)
c = float(input("enter number 'c'"))
print(c)
"""
a = 0.001
b = 1000
c = 0.001
d = float((b**2) - (4*a*c)) 
sol1 = (-b - math.sqrt(d))/(2*a)  
sol2 = (-b+math.sqrt(d))/(2*a)  
print('a) The solution are {0} and {1}'.format(sol1,sol2)) 

## b) The result was the same

d = float((b**2) - (4*a*c))  
factor = (-b - math.sqrt(d))
sol1 = ((-b - math.sqrt(d)) *factor) /((2*a) * factor)  
sol2 = ((-b+math.sqrt(d))* factor)/((2*a) *factor)

print('b) The solution are {0} and {1}'.format(sol1,sol2)) 

## c)

def quadratic(d):
    
    if d > 0:
        num_roots = 2
        x1 = (((-b) + math.sqrt(d))/(2*a))     
        x2 = (((-b) - math.sqrt(d))/(2*a))
        print("c) There are 2 roots: %f and %f" % (x1, x2))
    elif d == 0:
        num_roots = 1
        x = (-b) / 2*a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")
        exit()
        
d = float((b**2) - (4*a*c)) 
quadratic(d)


# 6\. **The derivative**
# 
# Write a program that implements the function $f(x)=x(x−1)$
# 
# (a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:
# 
# $$
# \frac{{\rm d}f}{{\rm d}x} = \lim_{\delta\to0} \frac{f(x+\delta)-f(x)}{\delta}
# $$
# 
# with $\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer your program gives. The two will not agree perfectly. Why?
# 
# (b) Repeat the calculation for $\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the accuracy scale with $\delta$?

# In[14]:


from sympy import *
import math
x = Symbol('x')
f = x*(x-1)
f_prime = f.diff(x)
print(f_prime)
f_prime = lambdify(x, f_prime)
print("Result of the function with python derivative imp. : ", f_prime(1))

# a) They are not agreeing perfectly because we are not using a h value small enough to ignore

def f(x):
    return x*(x-1)

def derive(function, value):
    h = 1e-2
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom

    return float("%f" % slope)
print("Result of the function with h 0.01 derivative imp. : ", derive(f, 1))

# b) The results gets more accurete when the h value get closer to 0

def f(x):
    return x*(x-1)

def derive2(function, value,h):
   # h = 1e-4
   #  h = 1e-6 
   # h = 1e-8
   # h = 1e-10
   # h = 1e-12
   # h = 1e-14
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    return float("%f" % slope)
h = 1e-2
for i in range(0,6):
    h = h * 1e-2
    print("Result of the function with h ","%.14f" % h ," derivative imp. : ", derive2(f, 1,h))
   


# 7\. **Integral of a semicircle**
# 
# Consider the integral of the semicircle of radius 1:
# $$
# I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
# $$
# which is known to be $I=\frac{\pi}{2}=1.57079632679...$.
# 
# Alternatively we can use the Riemann definition of the integral:
# $$
# I=\lim_{N\to\infty} \sum_{k=1}^{N} h y_k 
# $$
# 
# with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where
# $y_k$ is the value of the function at the $k-$th slice.
# 
# (a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?
# 
# (b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in running it for 1 minute? Use `timeit` to measure the time.
