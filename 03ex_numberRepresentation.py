#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Number representation
'''Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex). 
Determine the input type in the function, and pass another argument to choose the output representation.'''

def convert (argument):
    if argument == 1:
        print(bin(number)[2:])
    elif argument == 2:
        print (number)
    elif argument == 3:
        print(hex(number)[2:])
number = int(input("Please enter a number: ")) 
argument = int(input('choose the output type: 1=bin, 2=dec, 3=hex: '))
print(number, "is a", type(number))
temp = convert(argument)  


# In[ ]:


#2. 32-bit floating point number
'''Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) 
into a single precision floating point in decimal representation. Interpret the various bits as sign, 
fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.'''

x = input()

if x[0] == 0:
    sign = 1
else:
    sign = -1

exponent = int('0b' + x[1:9],2)
mantissa = int('0b' + x[9:],2)/(2**23)
print (sign*(1+mantissa)*2**(exponent-127))


# In[ ]:


#3. Underflow and overflow
'''Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point 
numbers on your computer.
Hint: define two variables initialized to 1, and halve/double them for a sufficient amount of times to 
exceed the under/over-flow limits.'''
from tabulate import tabulate
N=1100
Underflow = 1
Overflow = 1
factor = 2
for i in range(N):
    Underflow= float(Underflow/2)
    Overflow= float (Overflow*2)
    print (i,"\t\t",Underflow,"\t\t",Overflow)


# In[ ]:


#4. Machine precision
'''Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers
Hint: define a new variable by adding an increasingly smaller value and check when the addition starts to have no 
effect on the number.'''


from tabulate import tabulate
N=50
number=1
add=0.001
for i in range(N):
    number += add / 2
    add=add/2
    print (number)
    
    


# In[ ]:


#5. Quadratic solution
#a

from math import sqrt
a = 0.001
b = 1000
c = 0.001


sol1 = (- b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
sol2 = (- b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print('The solution are:',sol1,sol2)
#b 
sol3 = ((- b - sqrt(b ** 2 - 4 * a * c)) * (- b - sqrt(b ** 2 - 4 * a * c))) / ((2 * a) * (- b - sqrt(b ** 2 - 4 * a * c)))
sol4 = ((- b + sqrt(b ** 2 - 4 * a * c)) * (- b + sqrt(b ** 2 - 4 * a * c))) / ((2 * a) * (- b + sqrt(b ** 2 - 4 * a * c)))
print('The solution are:',sol3,sol4)
#c
#The answers are the same 


# In[ ]:


#6. The derivative
'''Write a program that implements the function  𝑓(𝑥)=𝑥(𝑥−1)'''
def f(x):
    result = x * (x - 1)
    return result
def d(f, x, k):
    result_der = (f(x+k)-f(x))/k
    return result_der

print(d(f, 1, 10**(-2)))
print ("calculating analytically the result is 1")
print ("""type of the values is the reason. If we use float -  calculations involving numbers with more 
than those decimal places involved do not yield the correct result, simply because the binary 
representation of those numbers does not allow to store them with sufficient accuracy.""")
print(d(f, 1, 10**(-4)))
print(d(f, 1, 10**(-6)))
print(d(f, 1, 10**(-8)))
print(d(f, 1, 10**(-10)))
print(d(f, 1, 10**(-12)))
print(d(f, 1, 10**(-14)))
print ("""precision error varies along the parabola plot""")


# In[ ]:


#7. Integral of a semicircle
"""Consider the integral of the semicircle of radius 1:"""
from math import sqrt

def integral(N):
    integral = 0
    x = -1
    for i in range (N):
        x += 1/N
        integral = integral + (sqrt(1 - x**2))*2/N
    return integral
       
integral(100)
print ('integral with  𝑁=100')
print(integral(100))
print ("the result is not accurate")
print ('time for integral with  𝑁=100:')
get_ipython().run_line_magic('timeit', 'integral(100)')
print(" 𝑁 can be increased 35000 times if the computation needs to be run in less than a second")
print(integral(3500000))
get_ipython().run_line_magic('timeit', 'integral (3500000)')
print ('for 1 minute calculation we need to do 3500000*60 iterations')
get_ipython().run_line_magic('timeit', 'integral(210000000)')
    


# In[ ]:




