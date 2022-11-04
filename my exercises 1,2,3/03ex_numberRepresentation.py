#!/usr/bin/env python
# coding: utf-8

# # Exercise 3: Number representation
# # Duy Tommy Tran
# 
# #### Importing library

# In[1]:


import math


# #### 1. Number representation

# In[2]:


def isbin(x):
    if str(x)[0:2] == '0b':    # The value is in binary if it starts with 0b
        return True
    else:
        return False

def ishex(x):
    if str(x)[0:2] == '0x':    # The value is in hexadecimal if it starts with 0x
        return True
    else: 
        return False

def convert(x, rep):
    if isbin(x) or ishex(x):
        to_int = int(bin(x), 2)*isbin(x) + int(hex(x), 16)*ishex(x)
    else:
        to_int = int(x)
    
    if rep == 'bin':
        return bin(to_int)
    elif rep == 'hex':
        return hex(to_int)
    else:
        return to_int

print(convert(0x14, 'dec'))
print(convert(0b10011, 'hex'))
print(convert(25, 'bin'))


# #### 2. 32-bit floating point number

# In[3]:


def to_singlePrecisionFloatingPoint(binary):
    sign = binary[0]           # Slice the array to get the wanted bits
    exponent = binary[1:9]
    mantissa = binary[9:]
    
    # Sign
    s = int(sign)
    
    # Exponent
    e = int(exponent, 2)
    bias = 127
    
    # Mantissa
    f = 0
    for i in range(len(mantissa)):
        f += int(mantissa[i])/2**(i+1)
    
    return ((-1)**s) * (1+f) * 2**(e-bias)


# In[4]:


to_singlePrecisionFloatingPoint('110000101011000000000000')


# #### 3. Underflow and overflow

# In[5]:


a = 1.0
while a < math.inf:
    overflow = a
    a *= 2
print(f'Overflow: {overflow}')

b = 1.0
while b > 0:
    underflow = b
    b /= 2
print(f'Underflow: {underflow}')


# #### 4. Machine precision

# In[6]:


a = 1.0
b = 1.0
k = 0

while True:
    add = 10**(-k)
    print(k, b+add)
    if a == b+add:
        print('No effect')
        break
    k += 1


# #### 5. Quadratic solution

# In[7]:


def quadratic1(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/2*a, (-b-math.sqrt(b**2-4*a*c))/2*a


# #### 5.a)

# In[8]:


a = 0.001
b = 1000
c = 0.001

print(quadratic1(a,b,c))


# #### 5.b)
# 
# $$
# \frac{2c}{-b \mp \sqrt{b^2-4ac}}
# $$

# In[9]:


def quadratic2(a,b,c):
    return (2*c)/(-b-math.sqrt(b**2-4*a*c)), (2*c)/(-b+math.sqrt(b**2-4*a*c))


# In[10]:


print(quadratic2(a,b,c))


# At the first solution, the first root is wrong while the second root is quite precise. A similar case for the second solution where the first root is precise while the second root is wrong. This is a problem that comes from subtracting two nearly equal numbers, and we lose the precision.
# 
# We can get a better solution by combining the two formulas, where we avoid subtracting two nearly equal numbers.

# #### 5.c)

# In[11]:


def quadratic_improved(a,b,c):
    return (2*c)/(-b-math.sqrt(b**2-4*a*c)), (-b-math.sqrt(b**2-4*a*c))/2*a


# In[12]:


print(quadratic_improved(a,b,c))


# #### 6. The derivative

# In[13]:


def f(x):
    return x*(x-1)


# #### 6.a)

# In[14]:


def derivative(f, x, delta):
    return (f(x+delta) - f(x))/delta


# In[15]:


delta = 1e-2
x = 1

derivative(f, x, delta)


# Calculating the derivative value analytically gives $f'(1) = 1$. This is different from the program because $\delta$ is too large, and has to move towards $0$.

# #### 6.b)

# In[16]:


delta = [1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

for i in delta:
    print(f"delta = {i} yields derivative f'(1) = {derivative(f,x,i)}")


# A small $\delta$ that approaches $0$ gives a value that is closer to the analytically found value, but when $\delta$ gets too small it will converge towards $0$.

# #### 7. Integral of a semicircle
# #### 7.a)

# In[17]:


def f(x):
    return math.sqrt(1-x**2)

def integral(f, N):
    I = 0
    h = 2/N
    
    for k in range(N):
        x = -1 + 2*k/N
        y_k = f(x)
        I += h*y_k
    return I

integral(f, 100)


# The result is close to the true value.
# 
# #### 7.b)

# In[18]:


for i in range(2, 8):
    print(f'N = {10**i}: I = {integral(f, 10**i)}')
    get_ipython().run_line_magic('timeit', 'integral(f, 10**i)')


# N can be increased to $10^6$ if the computation needs to run in less than a second. The longer we run the program, the longer the computer gets to do bigger computations that can give us a solution closer to the true value.
