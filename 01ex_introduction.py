#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `01ex_introduction.py`.
# 
# In case you need multiple files, name them `01ex_introduction_es01.py`, `01ex_introduction_es02.py` and so on. 
# 
# The exercises need to run without errors in `python3`.

# 1\. **The HelloWorld replacement**
# 
# a) Write a program that:
# - prints the numbers from 1 to 100
# - but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
# - for numbers which are multiples of both three and five print "`HelloWorld`".
# 
# b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

# In[1]:


a=[]
for i in range (0,100):
    if (i+1)%15 == 0:
        a.append("HelloWorld")       
    elif (i+1)%5 == 0:
        a.append("World") 
    elif (i+1)%3 == 0:
        a.append("Hello")
    else :
        a.append(i+1)
        
print(a) 

for i in range (0,100,1):
    if a[i]=="Hello":
        a[i]="Python"
        print(a[i])
    elif a[i]=="World":
        a[i]="Works"
        print(a[i])
    elif a[i]=="HelloWorld":
        a[i]="PythonWorks"
        print(a[i])
    else : 
        print(a[i]) 

b = tuple(a)

print(b)


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[2]:


x = input('type a value for x\n')
y = input('type a value for y\n')
x,y = y,x
print ("x = ", x, " y = ", y)


# 3\. **Computing the distance**
# 
# Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.
# 
# Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# In[3]:


import math

def Euclidean(a,b,c,d):
    d = math.sqrt(((c-a)**2) + ((d-b)**2))
    return print('Euclidean Distance =', d)

u = (int(input('x1 = ')), int(input('y1 = ')))
v = (int(input('x2 = ')), int(input('y2 = ')))
Euclidean(u[0],u[1],v[0],v[1])


# ##### 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The strings are in the cell below.

# In[4]:


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
a = str.lower(s1)
length = len(a)
print(a)
counting = {}
for i in range (0,length):
    c = a.count(a[i])
    counting[a[i]] = c
print(counting)    
a = s2 
a = str.lower(a)
length = len(a)
print(a)
counting = {}
for i in range (0,length):
    c = a.count(a[i])
    counting[a[i]] = c
print(counting)  
    
    


# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers in the list:

# In[5]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
length = len(l)
d = []
for i in range (0,length):
    new = l.count(l[i])
    if new == 1 : 
        d.append(l[i])
    else :
        pass
countOf_d = len(d)    
d.sort()
print ("No. of unique numbers =",countOf_d,"\n", d)        
    


# Do the same exploiting only the Python data structures.

# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[6]:


D = ()
A = int(input('Enter an int value = '))
B = str(input('Enter a str value = '))
C = float(input('Enter a float value = '))

try:
    D = A+B
    print(D)    
except:
    print ("Not possible to add", A, "and", B)
try:
    D = B+C
    print(D)
except:
    print ("Not possible to add", B, "and", C)  
try:
    D = A+C
    print(D)
except:
    print ("Not possible to add", A, "and", C)    


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[7]:


a = []
for x in range (0,10):
    x = x*x*x
    a.append(x)
    
print(a)    


# In[8]:


x = [a**3 for a in range(0,10)]
print(x) 


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# In[9]:


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


# In[10]:


print([(i,j) for i in range(0,3) for j in range(0,4)])


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[11]:


A = ([(a,b,c) for a in range(1,101,2) for b in range(2,101,2) for c in range(1,100) if (a**2 +b**2 == c**2)])
print(A)


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[12]:


import numpy as np
import math as m 

N = int(input('Number of elements\n'))
x = (np.random.rand(N)*10)
print(x)

a=0
for i in range (0,5):
    p = x[i]
    a += p**2
a = m.sqrt(a) 
x = x/a 
print (x)    
b=0
for i in range (0,5):
    b += x[i]**2
print(b)


# ##### 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[13]:


a = 0  #initialisation
b = 1  #initialisation
d = [a,b] #initialisation
for i in range (1,19):
    c = a+b
    d.append(c)
    a = b
    b = c
print(d)    


# In[ ]:




