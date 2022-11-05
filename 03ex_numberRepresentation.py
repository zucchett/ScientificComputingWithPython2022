#!/usr/bin/env python
# coding: utf-8

# # 03ex_numberRepresentation 

# In[1]:


# 1. Number representation

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


# In[5]:


# 2. 32-bit floating point number

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
    ind = int_str.index('1')
    exp_str = bin((len(int_str) - ind - 1) + 127)[2:]
    mant_str = int_str[ind + 1 : ] + fraction_str
    mant_str = mant_str + ('0' * (23 - len(mant_str)))
    return sign_bit, exp_str, mant_str

floatingPoint(-2.250000)


# In[7]:


# 3. Underflow and overflow

import sys
import numpy as np
print(sys.float_info)

a = np.array([2**31-1], dtype=int)   
a[0]+1


# In[8]:


# 4. Machine precision

small_variable = 1.
big_variable = 1.
while small_variable + big_variable > big_variable:
    #gets smaller and smaller till it doesnt
    big_variable+=small_variable
    small_variable=small_variable/2
    
print(small_variable)
print(big_variable)


# In[9]:


# 5. Quadratic solution

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


# In[11]:


# 6. The derivative

#6A
def f(x):
    return x*(x-1)

print("derivative definition with 𝛿=10^-2:-----> "+str((f(1+10**-2)-f(1))/10**-2))

#solving this analytically the answer should be 1.0
#the answers will not agree because in order make it as close as possible
# 𝛿 needs to aproach 0


#6B
for i in range(-2,-16,-2):
    print(f"For 𝛿=10^{i} :  "+str((f(1+10**i)-f(1))/10**i))
#looks like accuracy scales the most accurate value to 𝛿= 10^-8 
# after that accuracy decreases


# In[12]:


# 7. Integral of a semicircle

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
print("****************************************")



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
print("***********************************")


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
print("************************************")



#7B
#There is 20 times difference 
#i can't be sure because the value is already close real value after 1 second of iteration here is the comparison
print("Difference time iterated (1 second) vs. Real value(pi/2) :"+ str(math.pi/2 - timed_val_1_sec))
print("Difference time iterated (60 second) vs. Real value(pi/2) :"+ str(math.pi/2 - timed_val_60_sec))

print("Accuracy 1 second: %" + str(timed_val_1_sec/(math.pi/2)*100))
print("Accuracy 60 second: %" + str(timed_val_60_sec/(math.pi/2)*100))


# In[ ]:




