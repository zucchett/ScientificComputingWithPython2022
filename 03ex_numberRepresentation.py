#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''1. Number representation

Write a function that converts numbers among the bin, dec, and 
hex representations (bin<->dec<->hex). Determine the input type in the function, 
and pass another argument to choose the output representation.'''

#60 = 0b111100 = 0x3c
x = input()

def converter(x):
    if x[0] == '0' and x[1] == 'b':
        x = int(x, 2)
        print('Input number is in binary representation')
        print('Decimal representation of input number is:     ', x)
        print('Hexadecimal representation of input number is: ', hex(x))
    elif x[0] == '0' and x[1] == 'x':
        x = int(x, 16)
        print('Input number is in hexadecimal representation')
        print('Decimal representation of input number is:     ', x)
        print('Binary representation of input number is:      ', bin(x))
    else:
        x = int(x)
        print('Input number is in decimal representation')
        print('Hexadecimal representation of input number is:     ', hex(x))
        print('Binary representation of input number is:          ', bin(x))

converter(x)


# In[ ]:


'''2. 32-bit floating point number

Write a function that converts a 32 bit binary string (for example, 110000101011000000000000) 
into a single precision floating point in decimal representation. 
Interpret the various bits as sign, fractional part of the mantissa and exponent, 
according to the IEEE 754 reccommendations.'''

x = input()
def converter_32_bit(x):
    if x[0] == 0:
        sign = 1
    else:
        sign = -1

    exponent = int('0b' + x[1:9], 2)
    mantissa = int('0b' + x[9:], 2) / (2 ** 23)

    print('Decimal representation of input number is: ', sign * (1 + mantissa) * 2**(exponent - 127))

converter_32_bit(x)


# In[ ]:


'''3. Underflow and overflow

Write a program to determine the underflow and overflow limits 
(within a factor of 2) for floating point numbers on your computer.

Hint: define two variables initialized to 1, and halve/double them for a sufficient 
amount of times to exceed the under/over-flow limits.'''

from tabulate import tabulate
import math

overflow = 1
underflow = 1
list_1 = []
for i in range(1100):
    overflow = float(overflow * 2)
    underflow = float(underflow / 2)
    list_1.append([i, overflow, underflow])
  
 
col_names = ["i","overflow","undeflow"]
  
print(tabulate(list_1, headers = col_names))


# In[ ]:


#the underflow number is 8.98847e+307 and the overflow number is 4.94066e-324


# In[ ]:


'''4. Machine precision

Similarly to the previous exercise, write a program to determine 
the machine precision for floating point numbers.

Hint: define a new variable by adding an increasingly smaller value 
and check when the addition starts to have no effect on the number.'''

m_prec = 1; 

while True:
    m_prec = m_prec / 2
    n = 1 + m_prec
    if n == 1:
        print('Precision = ', m_prec)
        break


# In[ ]:


'''5. Quadratic solution

Write a function that takes in input three parameters  𝑎 ,  𝑏  and  𝑐  and prints out the 
two solutions to the quadratic equation  𝑎𝑥2+𝑏𝑥+𝑐=0  using the standard formula.
 
(a) use the function to compute the solution for  𝑎=0.001 ,  𝑏=1000  and  𝑐=0.001 
(b) re-express the standard solution formula by multiplying the numerator and the denominator by  
and again find the solution for  𝑎=0.001 ,  𝑏=1000  and  𝑐=0.001 . 
How does it compare with what has been previously obtained, and why? (add the answer to a Python comment)
(c) write a function that computes the roots of a quadratic equation accurately in all cases'''


def sol1(a, b, c):
    x1 = (- b - math.sqrt(b**2 - 4 * a * c))/(2 * a)
    x2 = (- b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
    return x1, x2

def sol2(a, b, c):
    x1 = (- b - math.sqrt(b**2 - 4 * a * c)) * (- b - math.sqrt(b**2 - 4 * a * c)) / (2 * a) * (- b - math.sqrt(b**2 - 4 * a * c))
    x2 = (- b + math.sqrt(b**2 - 4 * a * c)) * (- b + math.sqrt(b**2 - 4 * a * c)) / (2 * a) * (- b + math.sqrt(b**2 - 4 * a * c))
    return x1, x2

x11, x12 = sol1(0.001,1000,0.001)
print(x11, x12)
x21, x22 = sol2(0.001,1000,0.001)
print(x21, x22)
print('Results are the same: ', sol1(0.001, 1000, 0.001) == sol2(0.001, 1000, 0.001))
print(x11.hex(),x12.hex())
print(x21.hex(),x22.hex())
#the results are not the same because of order of operations. Need to add brackets to complete operations in correct order

def sol3(a, b, c):
    x1 = ((- b - math.sqrt(b**2 - 4 * a * c)) * (- b - math.sqrt(b**2 - 4 * a * c))) / ((2 * a) * (- b - math.sqrt(b**2 - 4 * a * c)))
    x2 = ((- b + math.sqrt(b**2 - 4 * a * c)) * (- b + math.sqrt(b**2 - 4 * a * c))) / ((2 * a) * (- b + math.sqrt(b**2 - 4 * a * c)))
    return x1, x2
print('\n After adding the brackets:')

x31, x32 = sol3(0.001,1000,0.001)
print(x31, x32)
print('Results are the same: ', sol1(0.001, 1000, 0.001) == sol3(0.001, 1000, 0.001))
print(x11.hex(), x12.hex())
print(x31.hex(), x32.hex())


# In[ ]:


'''6. Write a program that implements the function  𝑓(𝑥)=𝑥(𝑥−1) 
(a) Calculate the derivative of the function at the point  𝑥=1  using the derivative definition
with  𝛿=10−2 . Calculate the true value of the same derivative analytically 
and compare it with the answer your program gives. The two will not agree perfectly. Why?
(b) Repeat the calculation for  𝛿=10−4,10−6,10−8,10−10,10−12  and  10−14 . How does the accuracy scale with  𝛿 ?'''

#Analyticaly:
from sympy import diff, symbols
x, y = symbols('x y')
print('Derivative f(x) = x * (x - 1) = ', diff(x * (x - 1)))
print('Derivative f(1) = 1.0')


# In[ ]:


#Now try to calculate it using Python
def func(x):
    res = x * (x - 1)
    return res

def deriv(func, x, d):
    deriv = (func(x + d) - func(x)) / d
    return deriv

print(deriv(func, 1, 1e-2))
print('Results are the same: ', 1 == deriv(func, 1, 1e-2))
'''In my opinion it happens because Python is not able to opperate with limits, and we only can use small numbers
to calculate it. But because my computer is able to opperate with small numbers like 10**-2 etc,
it counts accurate result using formula of derivative.'''
print(deriv(func, 1, 1e-4))
print(deriv(func, 1, 1e-6))
print(deriv(func, 1, 1e-8))
print(deriv(func, 1, 1e-10))
print(deriv(func, 1, 1e-12))
print(deriv(func, 1, 1e-14))

print(deriv(func, 1, 1e-8) - 1 < 1 - deriv(func, 1, 1e-14)) #check which result is better
'''If we talk about accuracy using different variables of delta, the best result we got at the 10**-8,
and we can notice that accuracy changing like graph of our function (parabola graph). It happens because after
10**-8 accuracy started to decrease'''
'''But if we use small number like 10**-16 (which cannot be counted by my computer), 
Python returns 0 which is mistake'''
print(deriv(func, 1, 1e-16))


# In[ ]:


'''7. Integral of a semicircle

Consider the integral of the semicircle of radius 1:
𝐼=∫1−1(⎯⎯√1−𝑥2)d𝑥
 
which is known to be  𝐼=𝜋/2=1.57079632679... .

Alternatively we can use the Riemann definition of the integral:
𝐼=lim𝑁→∞∑𝑘=1𝑁ℎ𝑦𝑘
 
with  ℎ=2/𝑁  the width of each of the  𝑁  slices the domain is divided into 
and where  𝑦𝑘  is the value of the function at the  𝑘− th slice.
(a) Write a program to compute the integral with  𝑁=100 . How does the result compare to the true value?'''

def y(x):
    y = (1 - x**2)**(1/2)
    return y

def integral(n):
    k = -1
    integral = 0
    for i in range(n):
        k += 1/n
        integral += y(k)*(2/n)
    return(integral)
print('Result using N = 100: ', integral(100))
print('          Pi/2 =    : ', math.pi / 2)

#As we can see results do not match completely, so we can increase the number of parts N.
#But the accuracy depends on goal that we want to achive. For some cases this result is appropriate.'''


# In[ ]:


'''(b) How much can  𝑁  be increased if the computation needs to be run in less than a second? 
What is the gain in running it for 1 minute? Use timeit to measure the time.'''

print(math.pi/2)
m = 2000000 #it is number of N for 1 second
#m = 2000000 * 60 #it is number of N for 1 minute, uncomment to check
print(integral(m))
get_ipython().run_line_magic('timeit', 'integral(m)')

'''This is result for N = 2000000 (1s run):
pi/2 = 1.5707963267948966
res  = 1.570796826556323
1.03 s ± 2.02 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

This is result for N = 2000000*60 (1m run):
pi/2 = 1.5707963267948966
res  = 1.5707963363146518
1min 1s ± 128 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
as we can see, increasing a number of iteration by 60 times
allowed us only increase an accuracy only by 1 more significant digit'''


# In[ ]:




