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

# In[15]:


def numberConverter(a,outRep):
    if type(a) == int:
        if outRep == "bin":
            return (bin(a))
        elif outRep == "hex":
            return (hex(a))
        elif outRep == "dec":
            return (int (a))
        else:
            print ("you should choose between bin , hex ,dec")
    else:
        try:
            a= int (a,2)
            if outRep == "bin":
                return (bin(a))
            elif outRep == "hex":
                return (hex(a))
            elif outRep == "dec":
                return (int (a))
            else:
                print ("you should choose between bin , hex ,dec")
        except:
            a= int (a,16)
            if outRep == "bin":
                return (bin(a))
            elif outRep == "hex":
                return (hex(a))
            elif outRep == "dec":
                return (int (a))
            else:
                print ("you should choose between bin , hex ,dec")

a = 412
a_bin = bin (a)
a_hex = hex (a)
print (numberConverter (a,"bin"))
print (numberConverter (a_hex,"dec"))


# 2\. **32-bit floating point number**
# 
# Write a function that converts a 32 bit binary string (for example, `110000101011000000000000`) into a single precision floating point in decimal representation. Interpret the various bits as sign, fractional part of the mantissa and exponent, according to the IEEE 754 reccommendations.

# In[32]:


def binToFloat(a):
    if int(a[0])==1:
        sign = -1
    else:
        sign = 1
    e = int (a[1:9],2)
    f = a[9:32]
    s=1
    count = 1
    for i in f:
        j = int (i)
        s += j/(2**count)
        count +=1
    ans = sign*s*2**(e-127)
    return (ans)
a = "110000101011000000000000"
b= binToFloat(a)
print (b)


# In[ ]:





# 3\. **Underflow and overflow**
# 
# Write a program to determine the underflow and overflow limits (within a factor of 2) for floating point numbers on your computer. 
# 
# *Hint*: define two variables initialized to 1, and halve/double them for a sufficient amount of times to exceed the under/over-flow limits.

# In[48]:


a=1
for c in range (1024):
    a = a*2
    print ("%2d"%c,"\t\t","%2.5e"%a)


# In[55]:


b=1
for c in range (3000):
    if b==0:
        break
    else:
        b = b/2
    print ("%2d"%c,"\t\t","%2.5e"%b)


# 4\. **Machine precision**
# 
# Similarly to the previous exercise, write a program to determine the machine precision for floating point numbers.
# 
# *Hint*: define a new variable by adding an increasingly smaller value and check when the addition starts to have no effect on the number.

# In[54]:


a=0
b=100
for c in range (1031):
    if b==0 :
        break
    else:
        a=a+ 1/b
        b= b/2
        print ("%2d"%c,"\t\t","%2.5e"%a,"\t\t","%2.5e"%b)


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

# In[59]:


import math
def quadSol (a,b,c):
    if a == 0:
        print ("cant solve it for a = 0")
        return 0
    else:
        s1= (-b - (math.sqrt(b**2 - 4*a*c)))/2*a
        s2= (-b + (math.sqrt(b**2 - 4*a*c)))/2*a
        s= [s1,s2]
        return s
a= 0.001
b=1000
c=0.001
s= quadSol (a,b,c)
print (s)


# In[61]:


def quadSol2 (a,b,c):
    if a == 0:
        print ("cant solve it for a = 0")
        return 0
    else:
        s1= ((-b - (math.sqrt(b**2 - 4*a*c)))**2)/(2*a*(-b - (math.sqrt(b**2 - 4*a*c))))
        s2= ((-b + (math.sqrt(b**2 - 4*a*c)))**2)/(2*a*(-b + (math.sqrt(b**2 - 4*a*c))))
        s= [s1,s2]
        return s
a= 0.001
b=1000
c=0.001
s= quadSol2 (a,b,c)
print (s)


# In[ ]:


#i think this happened beceause 
#we are multypling a very smal number (almost zero)
#with a very smal number twice, wich make an underflow 
#or in the second part a very big number with a very big number
#which make overflow


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

# In[65]:


def fun(x):
    y=x*(x-1)
    return y
def derFun(d):
    z = (fun(1+d)-fun(1))/d
    return z
for i in [2,4,6,8,10,12,14,16]:
    print (derFun(10**-i))


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

# In[88]:


import math
N=6
s= 2/N
for i in range(1,N):
    s= s+ 2*(math.sqrt (1-1/i**2))/N
print (s)


# In[ ]:




