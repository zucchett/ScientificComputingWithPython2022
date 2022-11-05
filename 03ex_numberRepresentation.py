#!/usr/bin/env python
# coding: utf-8

# Ceren Yılmaz Gülten Exercise 3

# In[80]:


# 1. Number Representation 

def function(num,num_type):
    if num_type == 1:
        num_hex = hex(num)
        num_bin = bin(num)
        print("Hex conversion:\t",num_hex,"\t","Binary conversion:\t",num_bin)
    elif num_type == 2:
        num_bin = bin(num)
        num_dec = num #int(num,16)
        print("Binary conversion:\t",num_bin,"\t","Decimal conversion:\t",num_dec)
    elif num_type == 3:
        num_dec = num #int(num,2)
        num_hex = hex(num)
        print("Hex conversion:\t",num_hex,"\t","Decimal conversion:\t",num_dec)
        
function(16,1)
function(0x10,2)
function(0b1000101,3)

    


# In[48]:


# 2. 32-bit floating point number

a = '11000000100100001000101000000010'

def convert_int(mantissa):
    # the formula of the mantissa part 
    # the count is for after the point part. So, it needs to be decrease as a power of 2. 
    # power of come from the binary to decimal binary is in base 2 
    # the power will be start from the left to right since its after the point 
    count = -1
    mantissa_i = 0
 
    for i in mantissa:
        
        mantissa_i += (int(i) * pow(2, count))

        count -= 1
    # return with plus one because in the formula of mantissa there is a constant plus 1. 
    return (mantissa_i + 1)
# seperate the part of the binary number to sign,exponent and mantissa 

sign = int(a[0],2)
exponent = a[1:9]
exponent_int = int(a[1:9],2)
mantissa = a[9:32]

# seperated form of the binary number 
print("Sign |  Exponent |  Mantissa \n")
print(sign," | ",exponent, " | ", mantissa, "\n")

# 32 bit bias is 127 for single bias it is 1023 for double bias, unbiased the exponent part 

exponent_format = exponent_int - 127


mantissa_i = convert_int(mantissa)

# the formula of single precision floating point 

decimal_a = pow(-1, sign) * mantissa_i * pow(2, exponent_format)

print("Decimal Representation: ",decimal_a)


# In[35]:


# 3. Underflow and overflow 
over_flow = 1 
under_flow = 1 
# underflow error can be observed as number is equals zero 
def underFlow(n):
    for i in range(1100):
        n /= 2 
        print(i," ",n)
# overflow error can be observed as number is equals inf or program can give directly overflow error 
def overFlow(n):
    for i in range(1500):
        n *= 2
        print(i, " ", "%e"%n) 
        #%e is using to get a floating point number not integer. 
        # Because if it is not floating point it will print all the numbers and not give a overflow error. 
        
        
underFlow(under_flow)
print("\n Over Flow: \n\n")
overFlow(over_flow)

    


# In[13]:


# 4. Machine precision

a = 1
power = 0
# it runs for 100 results and each iteration the power will be decrease (ex. 2^0, 2^-1, 2^-2)
for i in range(1,100):
    # in each addition it will add 2^power. 
    a = a + pow(2,power)
    power -=1 
    print(i, "\t", a)
# when the results are printed after 52th iteration no changes observed. 
# At the same time in 64- bit double precision is equals the 2^(-52).


# In[148]:


# 5. Quadratic solution

import math 
# complex math module
import cmath
# a.

def solution(a,b,c):
    
    x_plus = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a) 
    
    x_minus= (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
    
    print("Solution 1:\t\t", x_plus)
              
    print("Solution 2: \t\t", x_minus)



# b.

def solution_b(a,b,c):
    
    
    x_plus = ((-b + math.sqrt((b**2)-(4*a*c)))*(-b + math.sqrt((b**2)-(4*a*c)))/((2*a)*(-b + math.sqrt((b**2)-(4*a*c)))))
    
    x_plusminus = ((-b + math.sqrt((b**2)-(4*a*c)))*(-b - math.sqrt((b**2)-(4*a*c)))/((2*a)*(-b - math.sqrt((b**2)-(4*a*c)))))
    
    x_minusplus = ((-b - math.sqrt((b**2)-(4*a*c)))*(-b + math.sqrt((b**2)-(4*a*c))))/((2*a)*(-b + math.sqrt((b**2)-(4*a*c))))
                                                       
    x_minus = ((-b - math.sqrt((b**2)-(4*a*c)))*(-b - math.sqrt((b**2)-(4*a*c))))/((2*a)*(-b - math.sqrt((b**2)-(4*a*c))))
    
    print("\nSolution 1b:\t\t\t\t", x_plus)
    
    print("\nSolution 1b-multiple with minus delta:\t", x_plusminus)
              
    print("Solution 2b: \t\t\t\t", x_minus)
    
    print("Solution 2b-multiple with plus delta: \t", x_minusplus)
    
    # there is some little difference between x_minuses. the reason of this is accuracy and perils of calculations with floats. 
    # computer not allows store with correct accuracy of these numbers binary representation. 

# c. 

def solution_c(a,b,c):
    determinant = b**2 - (4*a*c)
    
    if determinant==0:
        
        x = (-b) /(2*a)
        print("Number of roots 1 and root=\t", x)
        
    elif determinant>0:
        
        x_plus = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a) 
    
        x_minus= (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)
        
        print("Number of roots 2 and roots are:\n")
    
        print("Solution 1c:\t\t", x_plus)
              
        print("Solution 2c: \t\t", x_minus)
        
    else:
        
        x_plus = (-b + cmath.sqrt((b**2)-(4*a*c)))/(2*a) 
    
        x_minus= (-b - cmath.sqrt((b**2)-(4*a*c)))/(2*a)
        
        print("\nNo real roots.Number of roots 2 and roots are:\n")
    
        print("Solution 1c:\t\t", x_plus)
              
        print("Solution 2c: \t\t", x_minus)
        
        
     
solution(0.001,1000,0.001)
solution_b(0.001,1000,0.001)
solution_c(1,4,5)


# In[144]:


# 6.The derivative
from sympy import* 

# with analytical calculation derivative of the f function will be 2x-1. At x=1 point, the result will be 1. 
# When the result is calculated with derivative definition limit formula, the result is changes according to delta. 
# in the formula, delta is added to function, this condition gives small perturbation and gives well-condition function. 
# so, even delta = 10^-2 gives different result from the real answer. 
def f(x):
    
    a = x*(x-1)
    return a

def derivative(x):
    z = 10**(-2)
    exp = (f(x + z) - f(x)) / z 
    df = limit(exp,z,0)
    print("Derivative result for delta = 10^2: \t",df,"\n")
    
derivative(1)   

# with delta value is decreased, the accuracy is increased at first. After at one point, the accuracy start to decrease again. 
print("Derivative for different delta values:\n")
delta = [10**(-2),10**(-4),10**(-6),10**(-8),10**(-10),10**(-12),10**(-14)]

def derivative_accuracy(x):
    
    for i in delta:
        exp = (f(x + i) - f(x)) / i 
        df = limit(exp,i,0)
        print(i,"\t\t",df)

derivative_accuracy(1)


# In[50]:


# 7. Integral of a semicircle
import math
import numpy as np
import time

#a)
a = 1 
b = -1 
n = 100
x = np.linspace(a,b,n)
sum = 0
for z in range(1,n+1):
    
        sum += (2/n)*(math.sqrt(1-(x[z-1]**2)))
        #lim = limit(sum,z,oo)    
print("Result of n=100:\t",sum,"\n" )

# there is a slight difference. 
# since we get the n= 100 and we get 100 number betwwen 1 and -1 this can be change the result a lit bit
#b) 
a = 1 
b = -1 

n = 100
t=0
while t<1:
    start=time.time()
    n*=10
    x = np.linspace(a,b,n)
    sum = 0
    for z in range(1,n+1):

            sum += (2/n)*(math.sqrt(1-(x[z-1]**2)))
            #lim = limit(sum,z,oo)  
    end = time.time()
    t = end-start

print("Until 1 second:\t",sum) # when the n increased the answer closed to the real answer 
print("\n How much loop :\t",n)

# if we run until 1 minutes it approach more to real answer, but memory can be crash since the n will be really large. 

