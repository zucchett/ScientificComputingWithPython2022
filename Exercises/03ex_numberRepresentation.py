#!/usr/bin/env python
# coding: utf-8

# # Exercise 3 - hannafalch_nastby

# In[ ]:


import math
import numpy as np
import matplotlib.pyplot as plt


# ## 1. Number representation
# 
# Write a function that converts numbers among the bin, dec, and hex representations (bin<->dec<->hex).
# Determine the input type in the function, and pass another argument to choose the output representation.

# In[38]:


def conversion(inp, outp):
    if inp[1] == 'b':
        number = 2
    elif inp[1] == 'x':
        number = 16
    else:
        number = 10
    
    if outp == 'dec':
        return float(int(inp, base = number))
    elif outp == 'hex':
        return hex(int(inp, base = number))
    elif outp == 'bin':
        return bin(int(inp, base = number))


# In[43]:


print("Conversion from decimal to binary: 12 =", conversion('12', 'bin'))
print("Conversion from decimal to hexadecimal: 12 =",conversion('12', 'hex'))

print("Conversion from binary to decimal: 0b10111 =",conversion('0b10111', 'dec'))
print("Conversion from binary to hexadecimal: 0b10111 =",conversion('0b10111', 'hex'))

print("Conversion from hexadecimal to decimal: 0x39 =",conversion('0x39', 'dec'))
print("Conversion from hexadecimal to binary: 0x39 =",conversion('0x39', 'bin'))


# ## 2. 32-bit floating point number
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[92]:


def bitConverter(inp):
    bias = 127
    
    #check sign
    if inp[0] == '0':
        sign = '+'
    else:
        sign = '-'
        
    #check fractional part
    frac = int(inp[1:9], 2)
    mantissa = 2**(frac-bias)
    
    #check exponent
    exp = inp[9:]
    e = 1    
    for i in range(len(exp)):
        if exp[i] == '1':
            e += 2**-(i+1)

    number = float(sign + str(e * mantissa))
    return number
    


# In[97]:


print(bitConverter('10000011111000000000000000000000'))
print(bitConverter('110000101011000000000000'))


# ## 3. Underflow and overflow
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[106]:


def Underflow():
    var = 1.0
    while var != 0:
        prev = var
        var /= 2
        #print(var)
    return prev
print("The underflow-limit is: ", Underflow())


# In[243]:


def Overflow():
    var = 1.0
    while (var < np.inf):
        prev = var
        var *= 2
    return prev
print("The overflow-limit is: ", Overflow())


# ## 4. Machine precision
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[245]:


def machinePrecision():
    var = 0
    prev = 1
    count = 1
    while (var != prev):
        prev = var 
        var += 2**-count
        print(abs(prev-var))
        count += 2
    return prev
machinePrecision()


# In[246]:


#The machine is precise up to 10**-16


# ## 5. Quadratic solution
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

# In[154]:


def quadraticSolA(a, b, c):
    
    sol1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    sol2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    
    return sol1, sol2


# In[155]:


quadraticSolA(0.001,1000,0.001)


# In[160]:


def quadraticSolB(a,b,c):
    root = math.sqrt(b**2-4*a*c)

    #sol1 = ((-b + math.sqrt(b**2-4*a*c))*(-b - math.sqrt(b**2-4*a*c))) / ((2*a)*(-b - math.sqrt(b**2-4*a*c)))
    #sol2 = ((-b - math.sqrt(b**2-4*a*c))*(-b + math.sqrt(b**2-4*a*c))) / ((2*a)*(-b + math.sqrt(b**2-4*a*c)))
    sol1 = (2*c) / (-b - math.sqrt(b**2-4*a*c))
    sol2 = (2*c) / (-b + math.sqrt(b**2-4*a*c))
    return sol1, sol2


# In[161]:


quadraticSolB(0.001,1000,0.001)


# In[164]:


#In this case the first root is more accurate than in a), whilst the second root is less accurate.
#This is becuse we are subrtracting nearly equal numbers, and the machine looses precision
#In a) we are subtracting to nearly equal numbers in the first solution, while in b) we are doing it in the second solution.


# In[162]:


def quadraticSolC(a,b,c):
    sol1 = (2*c) / (-b - math.sqrt(b**2-4*a*c))
    sol2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return sol1, sol2


# In[163]:


quadraticSolC(0.001,1000,0.001)


# ## 6. The derivative
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

# In[168]:


def func(x):
    return x*(x-1)


# a)

# In[172]:


def derivative(f, x, d):
    return((f(x+d) - f(x))/d)
derivative(func, 1, 10**-2)


# In[170]:


#The answer is not tha same as the analytical one, becouse we are subracting two nearly equal numbers,
#and also dividing two small numbers, both of witch cause a loss of precision


# b)

# In[236]:


deltaList = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
precList = []
for i in deltaList:
    print("For delta =", i)
    print("The integral is: ", derivative(func, 1, i))
    prec = abs(1-derivative(func, 1, i))
    print("The precision is: ", prec)
    precList.append(prec)


# In[239]:


#The precision gets better and is best for 𝛿 = 10**-8, but then it gets worse again
#This is shown in the plot below:
 
    
import matplotlib.pyplot as plt

plt.plot(precList)
plt.show()


# ## 7. Integral of a semicircle
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

# a)

# In[209]:


import numpy as np

def funkI(x):
    return np.sqrt(1-x**2)


def riemannIntegral(N):
    I = 0
    for n in range(N):
        I += funkI(-1+(2/N)*n)
    return I*(2/N)

riemannIntegral(100)


# In[210]:


#This value is smaller than the true value.


# b)

# In[230]:


import timeit
timeRie = 0
N = 10000
while  N <= 1000000:
    get_ipython().run_line_magic('timeit', 'timeRie = riemannIntegral(N)')
    N+=100000
    print("With N equals: ", N)
#%timeit timeRec = [fibRec(n) for n in range(20)]


# In[ ]:


#We see that N can be eincreased by a lot, up to about 1000000 while the computation still runs for less than a second.
#By running it for a minute we can have a very big N which will make the computation more accurate, as the integral becomes more accurate.

