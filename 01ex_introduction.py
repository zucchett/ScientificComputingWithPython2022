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


A=list (range(1,101))
for i in range (0,100):
    if A[i]%5==0 and A[i]%3==0:
        A[i]="HelloWorld"
    elif A[i]%5 == 0:
            A[i]= "World"
    elif A[i]%3 == 0:
            A[i]= "Hello"
print (A)


# In[2]:


for i in range (0,100):
    if A[i]=="Hello":
        A[i]="Python"
    elif A[i]== "World":
          A[i]= "Works"
A= tuple(A)
print(A)


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[3]:


x=input("insert x:")
y= input ("insert y:")
x,y =y,x
print ("new x is:")
print (x)
print ("new y is:")
print (y)


# In[ ]:





# In[4]:


import math

def euclideanDistance (u1,u2):
    ed = math.sqrt ((u1[0]-u2[0])**2 + (u1[1]-u2[1])**2)
    return ed
i=(12,0)
w=(0,16)
r= euclideanDistance (i,w)
print (r)


# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The strings are in the cell below.

# In[5]:


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
def numberOfxCharacter (sTr,x):
    A= sTr[:]
    A = A.lower()
    x = x.lower()
    counter = 0
    for i in A:
        if i==x:
            counter = counter + 1
    return counter
print (numberOfxCharacter(s1,"W"))
print (numberOfxCharacter(s2,"T")) 


# In[ ]:





# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers in the list:

# In[6]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

length = len(l)
uni = []
for i in range (0,length):
    for j in range (0,length): 
        if (i == j):
            pass
        elif l[i]==l[j]:
            break
        elif j == length - 1:
            uni.append(l[i])
        else:
            pass
uni.sort()
print ("the unique numbers in l are:")
print (uni)
print ("the number of unique numbers in l is:" )
print (len(uni))


# Do the same exploiting only the Python data structures.

# In[7]:


uni = []
for i in l:
    if l.count (i)== 1:
        uni.append(i)
    else:
        pass
uni.sort()
print (uni)
print (len(uni))


# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[8]:


var1 = input ("insert variable:")
var2 = input ("insert variable:")
try:
    var3= float (var1)
    var4= float (var2)
    if (type (var3)== type (var4)):
        varOut = var3 + var4
        print (varOut)
except:
    varOut = var1 + var2
    print (varOut)


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[9]:


cubes =[]
for i in range(11):
    cubes.append(i**3)
print (cubes)

compcubes = [x**3 for x in range(11)]
print (compcubes)


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# In[10]:


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)
b = [(x,y) for x in range(3) for y in range(4)]
print (b)


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[11]:


import math
a= [c**2 for c in range (5,100)]
Pythagorean = []
for i in range (3,100):
    for j in range (i+1,100):
        if i**2 + j**2 in a:
            z= int (math.sqrt (i**2 + j**2))
            Pythagorean.append((i,j,z))
        else:
            pass
print (Pythagorean)


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[12]:


def Normalizer (A):
    V= 0.0
    for x in A:
        V= V + x**2
    S= math.sqrt(V)
    B = [x/S for x in A]
    return B
y =[5.1,-4.2,3.3,-2.4,1.5]
y2 = Normalizer(y)
result = 0
for x in y2:
    result = result +x**2
print (y2)
print (result)


# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[15]:


A = [0,1]
for x in range (2,20):
    A.append(A[x-1]+A[x-2])
print (A)
print (len (A))


# In[ ]:




