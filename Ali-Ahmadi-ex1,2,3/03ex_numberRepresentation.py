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

# In[8]:


def bin_dec_hex(inpu):
    if int(inpu):
        integer = int(inpu)
        
    if bin(inpu):
        bin_ = bin(inpu) 
        
    if hex(inpu):
        hex_ = hex(inpu)
        
    return (bin_,integer,hex_)

#needs just 1 input int hex or dec


print(bin_dec_hex(1999))
print(bin_dec_hex(0b10101110))


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[9]:


# Function to convert a fraction to binary form.
def binaryOfFraction(fraction):

    # Declaring an empty variable to store binary bits.
    binary = str()
    
    # Multiplying and subtracting fraction until it becomes Zero.
    while (fraction):

        # Multiplying fraction by 2.
        fraction = fraction*2

        # Storing Integer Part of Fraction in int_part.
        if (fraction >= 1):
            int_part = 1
            fraction -= 1
        else:
            int_part = 0

        # Adding int_part to binary after every iteration.
        binary += str(int_part)

    # Returning the binary string.
    return binary

# Function to get sign bit, exp bits and mantissa bits, from given real number.
def floatingPoint(real_no):

# Setting Sign bit 0 as default.
    sign_bit = 0

# Sign bit will set to 1 if its negative.
    if(real_no < 0):
        sign_bit = 1

# converting it to absolute value because we already know sign value
    real_no = abs(real_no)

    # converting integer part to binary
    int_str = bin(int(real_no))[2:]

    # function for converting fraction part of real no to Binary.
    fraction_str = binaryOfFraction(real_no - int(real_no))

    # Getting the index where it was high for the first
    # Time in binary repres
    # of Integer part of real no.
    ind = int_str.index('1')

# The Exponent is the no.
# By which we have right
# Shifted the decimal and
# it is given below.
# Also converting it to bias
# exp by adding 127.
    exp_str = bin((len(int_str) - ind - 1) + 127)[2:]

# getting mantissa string
# By adding int_str and fraction_str.
# the zeroes in MSB of int_str
# have no significance so they
# are ignored by slicing.
    mant_str = int_str[ind + 1 : ] + fraction_str

# Adding Zeroes in LSB of
# mantissa string so as to make
# it's length of 23 bits.
    mant_str = mant_str + ('0' * (23 - len(mant_str)))

# Returning the sign, Exp
# and Mantissa Bit strings.
    return sign_bit, exp_str, mant_str

floatingPoint(-2.250000)


# 3\. **Underflow and overflow**
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[10]:


import sys
import numpy as np
print(sys.float_info)
#In python, integers have arbitrary precision 
#and therefore we can represent an 
#arbitrarily large range of integers (only limited by memory available).



#i use np.array because it use C-style fixed-precision integers
a = np.array([2**31-1], dtype=int)
    
a[0]+1


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[11]:


small_variable = 1.
big_variable = 1.
while small_variable + big_variable > big_variable:
    #gets smaller and smaller till it doesnt
    big_variable+=small_variable
    small_variable=small_variable/2
    
print(small_variable)
print(big_variable)


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

# In[12]:


import math
import cmath

def solution(a,b,c):
    dis = b * b - 4 * a * c    
    ans1 = (-b-math.sqrt(dis))/(2 * a)
    ans2 = (-b + math.sqrt(dis))/(2 * a)
    return (ans1,ans2)
    
##A a=0.001; b = 1000; c=0.001

#but this one returns a domain error since square root cant be negative.
#we need complex numbers to solve every cases
#import cmath 
def solution_v2(a,b,c):
    dis = b * b - 4 * a * c     
    ans1 = (-b-cmath.sqrt(dis))/(2*a)
    ans2 = (-b+cmath.sqrt(dis))/(2*a)
    return (ans1,ans2)

try:
    print(solution(1000,152,61))
except:
    print("Math Domain Error No Real number solutions(Discriminant is negative). Try complex function")

print(solution_v2(1000,152,61))


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

# In[13]:


#6A
def f(x):
    return x*(x-1)

print("derivative definition with 𝛿=10^-2:-----> "+str((f(1+10**-2)-f(1))/10**-2))

#solving this analytically the answer should be 1.0
#the answers will not agree because in order make it as close as possible
# 𝛿 needs to aproach 0


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

# In[23]:


def riemannint(function,a,b,n):
    #total val initialized as 0
    sumval = 0
    #h is the width of each rectangle in the function
    #n is the slice number
    # a and b is the integral range
    
    h = (b-a)/n
    for i in range(0,n-1):
        #for every slice we will compute the total rectangle areas
        current_x = a+i*h
        #summed up
        sumval    = sumval + function(current_x) * h
    return sumval

def f_circle(x):
    #circle equation y is alone
    return (1-x**2)**(1/2)

a = riemannint(f_circle,-1,1,100)



##7A

import math
n_100 = riemannint(f_circle,-1,1,100)
print("Difference of 100 sliced val vs. Real value(pi/2) :"+ str(math.pi/2 - n_100))



import time
from time import process_time, sleep


start = process_time() #started the counter
end = start + 1 #this is just for the while loop
time = 1 #time that you want to iterate
n = 100 #initialized slice number
while time >= end-start:
    timed_val_1_sec = riemannint(f_circle,-1,1,n)
    n += 1000
    end = process_time()
    
print("Value of Integral: " + str(timed_val_1_sec))
print("Total time: " + str(end-start) +" seconds.")
print("Total slices: "+str(n))


start = process_time() #started the counter
end = start + 1 #this is just for the while loop
time = 60 #time that you want to iterate
n = 100 #initialized slice number
while time >= end-start:
    timed_val_60_sec = riemannint(f_circle,-1,1,n)
    n += 1000
    end = process_time()
    
print("Value of Integral: " + str(timed_val_60_sec))
print("Total time: " + str(end-start) +" seconds.")
print("Total slices: "+str(n))



# In[16]:


#7B
#There is 20 times difference 
#i can't be sure because the value is already close real value after 1 second of iteration here is the comparison
print("Difference time iterated (1 second) vs. Real value(pi/2) :"+ str(math.pi/2 - timed_val_1_sec))
print("Difference time iterated (60 second) vs. Real value(pi/2) :"+ str(math.pi/2 - timed_val_60_sec))

print("Accuracy 1 second: %" + str(timed_val_1_sec/(math.pi/2)*100))
print("Accuracy 60 second: %" + str(timed_val_60_sec/(math.pi/2)*100))

