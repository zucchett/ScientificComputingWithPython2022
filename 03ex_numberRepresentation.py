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

# In[45]:


def conversion(x, y, z):
    if x == 'dec':
        if z == 'hex':
            print("the Hexadecimal representation of the number is ", hex(int(y)))
        elif z == 'bin':
            print("the Binary representation of the number is ", bin(int(y)))
        else:
            print(y)
    elif x == 'bin':
        if z == 'hex':
            print("the Hexadecimal representation of the number is ", hex(int(y,2)))
        elif z == 'dec':
            print("the Decimal representation of the number is ", int(y,2)) 
        else:
            print(y)
    elif x == 'hex':
        if z == 'dec':
            print("the Decimal representation of the number is ", int(y,16))
        elif z == 'bin':
            print("the Binary representation of the number is = ", bin(int(y,16)))
        else:
            print(y)    
    else:
        print('check inputs')
                
number = (input('enter a binary, hexadecimal or decimal number = '))
numberType = (input('enter the above number"s types as dec, hex or bin = '))
convertTo = (input('The type you want to convert to (hex,bin,dec) = '))
conversion(numberType, number, convertTo)


# In[42]:


number = int(input('enter a binary, hexadecimal or decimal number a = '))

n_hex = hex(number)
n_bin = bin(number)
print('hex value of a is = ', n_hex)
print('bin value of a is = ', n_bin)


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# 3\. **Underflow and overflow**
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[149]:


import sys
print(sys.float_info.max)
print(sys.float_info.min)
def doubling(c):
    for i in range(0, 1023): #The machine gives an error at range 0 to 1024
        c = c*2
    return float(c)   

def halving(d):
    for i in range(0,1074): #The program returns 0 when at a range from 0 to 1075
        d = d/2
    return d  

doubling(1)
halving(1)


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[ ]:





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

# In[148]:


import math as m 
def quadratic(a,b,c):
    a1 = (-b+(m.sqrt((b**2)-(4*a*c))))/(2*a)
    a2 = (-b-(m.sqrt((b**2)-(4*a*c))))/(2*a)    
    return a1, a2

def quadratic1(a,b,c):
    a1 = (-b+(m.sqrt((b**2)-(4*a*c))))/(2*a)
    a2 = (-b-(m.sqrt((b**2)-(4*a*c))))/(2*a)    
    b1 = a1*(-b+(m.sqrt((b**2)-(4*a*c))))
    b2 = a1*(-b-(m.sqrt((b**2)-(4*a*c))))
    b3 = a2*(-b+(m.sqrt((b**2)-(4*a*c))))
    b4 = a2*(-b-(m.sqrt((b**2)-(4*a*c))))
    print(b1, b2, b3, b4)
 

quadratic1(0.001, 1000, 0.001)
quadratic(0.001, 1000, 0.001)


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

# In[143]:


import math 
def f(x):
    return x*(x-1)

def f1(x):
    i = 0.01
    a = (f(x+i) - f(x))/i
    print (a)
    
a = 1e-2    
for i in range (0,7):
    p = 2*i
    b = (1e-2)**p
    f1(float(b))
    


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

# In[129]:


import math 
I = pi/2
N=100
h=2/N
b=0

for i in range(1,N+1):
    x = -1+(h*i)
    y = sqrt(1-(x**2))
    x = 1+(h*i)
    a = h*y
    b = b+a
print(b)

