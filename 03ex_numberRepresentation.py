# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:35:30 2022

@author: 10
"""
import math
import time
import numpy as np
#%%QUESTION 1
def conversion(number,n): # number =>the type of the representation #n=> selecting the representation
    
    if n == 1: # for decimal numbers conversion
        a_bin = bin(number)
        a_hex = hex(number)
        print ( "binary rep of number is" ,a_bin, " and hex rep of number is",a_hex)
    elif n == 2: # for hexadecimal numbers conversion
        a_dec = number
        a_bin = bin(number)
        print(  "decimal rep of number is",a_dec, "bin rep of number is", a_bin)
    elif n == 3: # for binary numbers conversion
        a_dec = number
        a_hex = hex(number)
        print(  "decimal rep of number is",a_dec, "hexrep of number is", a_hex)
       

conversion(16,1) # select 1 for decimal to bin and hex
conversion(0x19,2) # select 2 for hex to dec and bin
conversion(0b10010,3) # select 3 for bin to dec and hex

#%%QUESTION 2

def convert_number(mantissa_str):
    
    mantissa = 0 # firstly the mantissa is 0
    power_of_two = -1
 
 
    for i in mantissa_str:
 
        mantissa += (int(i) * pow(2, power_of_two)) # as explained during the class this is 
                                                    #the formula used for  the mantissa
        power_of_two -= 1 #in order to have 2^-1,2^-2.. as in formula
         
    return (mantissa + 1) # adding 1 to obtain (mantissa = 1.f = 1 + ...)
 

    bin_32_str = '1100000000010000000100000000000' #THE STRING THAT WILL BE CONVERTED
 
    sign= int(bin_32_str[0])
    exponent = int(bin_32_str[1 : 9], 2)
    exponent_unbiased = exponent - 127
    mantissa_frc = bin_32_str[10 : ]
 
    mantissa = convert_number(mantissa_frc) # converting the 23 bits for the real dec. number representation
    
    #according to the formula of => (-1)^s * (1*f) * (2^(e-bias))
    decimal_rep = pow(-1, sign) * mantissa * pow(2, exponent_unbiased)
 
    # Printing the obtained
    # Real value of floating
    # Point Representation.
    print("The float value of the given IEEE-754 representation is :",decimal_rep)

#%% QUESTION 3
ower= 1 
under_1=1
r=1500
def over(n,r):
    for i in range(r):
        n= n*2
        print(i, "//" , "%0.5e"%n) # I put %0.5e because when the multiplying occured the result goes
                                    # to long and cannot be interpreted as float point. So, no overflow occurs.
                                    #thats why I added this argument. It goes until 1022 iterations

def under(n,r):
    for i in range(r):
        n=n/2
        print(i, "//" ,  n)      # It goes until 1073 iteration

over(ower,r)
under(under_1,r)


    
#%% QUESTION 4
number =0
power = 0
for i in range(1,500):
    number = number + pow(2,power)
    power += -1 
    print(i,number)
# the summation has no effect after the 53th iteration. The iteration is started from 1 . So considering the
#double precision it is 2^-52. It can be concluded from the result.

#%% QUESTION 5

import cmath
#%%
def quadratic(a,b,c):
    x_1=0
    x_2=0
    x_1 = (-b + math.sqrt((b**2)-(4*a*c))) / (2*a)
    x_2 = (-b - math.sqrt((b**2)-(4*a*c))) / (2*a)
    return x_1,x_2

#A)
a=0.001
b=1000
c=0.001
quadratic(a,b,c)

#B)
def quadratic_B(a,b,c):
    x_1=0
    x_2=0
    x_1 = ((-b + math.sqrt((b**2)-(4*a*c)))* (-b + math.sqrt((b**2)-(4*a*c)))) / ((2*a)*(-b + math.sqrt((b**2)-(4*a*c))))
    x_1_2= ((-b + math.sqrt((b**2)-(4*a*c)))*(-b - math.sqrt((b**2)-(4*a*c)))) / ((2*a)*(-b - math.sqrt((b**2)-(4*a*c))))
    x_2 = ((-b - math.sqrt((b**2)-(4*a*c))) * (-b - math.sqrt((b**2)-(4*a*c)))) / ((2*a)*(-b - math.sqrt((b**2)-(4*a*c))))
    x_2_2 = ((-b - math.sqrt((b**2)-(4*a*c))) *(-b + math.sqrt((b**2)-(4*a*c)))) / ((2*a)*(-b + math.sqrt((b**2)-(4*a*c)))) 
    print(x_1,x_1_2, "\n ",x_2,x_2_2)

quadratic_B(a,b,c)
#there is a difference between the 2nd roots x_2 and x_2_2. 
# Floats have limited number of meaningful decimal places, 
# considering fractional part of the mantissa: 6-7 decimal places for singles, 
# 15-16 for doubles. 
# involving numbers with more than those decimal  do not yield the correct result, simply because the binary representation of 
# those numbers does not allow to store them with sufficient accuracy.
#%%
#C)
a_2=1
b_2=3
c_2=2
def all_case(a,b,c):
    x_1=0
    x_2=0
    delta = (b**2) -(4*a*c)
    
    if delta>0:  
        x_1 = (-b + math.sqrt(delta)) / (2*a)
        x_2 = (-b - math.sqrt(delta)) / (2*a)
        print(x_1,x_2)
    if delta ==0:
        x_1= -b/(2*a)
        print(x_1)
    if delta<0:
        x_1 = (-b + cmath.sqrt(delta)) / (2*a)  #there will be no real root so , cmath library used for complex roots
        x_2 = (-b - cmath.sqrt(delta)) / (2*a)
        print(x_1,x_2, "there are no real root, just complex ")

all_case(a_2,b_2,c_2)

#%%QUESTION 6
import numpy as np

#a)
def f(x):
    return x*(x-1)

def derivative(func , x, delta ):
    return (func(x+delta)-func(x))/delta

derivative(f,1,10**-2)

#Analytically the true answer is 1. However the computed answer is 1.010000000000001
#The solution changed with gradually as the input changed.Which shows small pertubations in the input result in small effects in the output
#Which means this is a well-conditioned function.
###--------

#b) 
def derivative_b(func , x, delta ):
    for i in range(delta,-16,-2):
        delt=(10**i)    
        print(10,'^',i, " /// ",(func(x+delt)-func(x))/delt)

derivative_b(f,1,-2)

# while the delta is decreased , the value is approximate to the real answer and accuracy increases. until 10^-10 it aproximates to 1
#and then it approximates to the 0.

#%%QUESTION 7
#definitions
a=-1 
b=1
n=100
h= 2/n
x_1 = np.linspace(a, b, n) # definin the range for the function

#A)
I=0
for i in range(1,n+1):
   I+= h*(math.sqrt(1-x_1[i-1]**2))
print(I)

#There is a slight difference between the real and the obtained value

#B)
tim=0
n_2=100
while tim<1:
    start_time=time.time()
    n_2*=10
    I_second=0
    x_2 = np.linspace(a, b, n_2)
    for i in range(1,n_2+1):
        I_second+= (2/n_2)*(math.sqrt(1-x_2[i-1]**2))
    last_time = time.time()
    tim = last_time-start_time
print(I_second)
print(  "The an can be increased as" ,  n_2  , " to be run less than a second ")

# After the running, it can be seen that the result is converged and closer to the true value.
#N is can be large as N=10000000. 
#If we run this program about 1 minute , result will be more closer to the true value but the time
#for the progress is too large.
