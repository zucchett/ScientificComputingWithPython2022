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

# In[7]:


#a)

list1=[]
for i in range(1,101):
    if i%15 == 0: #if divided by 15 
        i = "HelloWorld"  
    elif i%5 == 0:  #if divided by 5
        i = "World"
    elif i%3==0: #if divided by 3
            i="Hello"
    list1.append(i)     
    
print(list1)


# In[8]:


#b)

for x in range(1,100):
    if list1[x] == "Hello":
        list1[x] ="Python"
    elif list1[x] == "World":
         list1[x] ="Works"
    elif list1[x] == "HelloWorld":
         list1[x] ="PythonWorks"        

list_2_tuple2= tuple(list1)
    
    
print(list_2_tuple2)
print(type(list_2_tuple2))


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[9]:


x= input("Enter a value for x: ")
y= input("Enter a value for y: ")

x, y = y, x
print("x= ", x)
print("y= ", y)


# 3\. **Computing the distance**
# 
# Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.
# 
# Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# In[10]:


import math
def euc_dis(u,v):
    euclideandistance = math.sqrt( ((u[0]-v[0])**2)+((u[1]-v[1])**2) )
    return(euclideandistance)

print ("u = (a, b)")
print ("v = (c, d)")

a= int(input("Enter a value for a: "))
b= int(input("Enter a value for b: "))
c= int(input("Enter a value for c: "))
d= int(input("Enter a value for d: "))

u = (a, b)
v = (c, d)

print(type(u))
print(type(v))

print("Eucledian distance between u and v is: ", euc_dis(u,v))


# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The strings are in the cell below.

# In[11]:


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


# In[12]:


def solve(string):
    string = string.lower()
    output = {}
    for i in string:
        keys = output.keys()
        if i not in keys:
            output[i] = 1
        else:
            output[i] += 1
    return output
s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
print("Number of times each character occurs in s1: ", solve(s1))
print('')
print("Number of times each character occurs in s2: ",solve(s2))


# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers in the list:

# In[13]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# In[14]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
l1 = []
count = 0
for i in l:
    if i not in l1:
        count = count + 1
        l1.append(i)
print("List of unique numbers: ", l1)
print("Number of unique numbers: ", count)


# Do the same exploiting only the Python data structures.

# In[15]:


l_2 = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]  
count2 = 0
l2 = []
for item2 in l_2:
    if item2 not in l2:
        count2 += 1
        l2.append(item2)
print("List of unique numbers: ", l2)
print("Number of unique numbers: ", count2)


# 6\. **Casting**
# 
# Write a program that:
# 0* reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[16]:


first_var = input("Enter the first variable for addition: ")
second_var = input("Enter the first variable for addition: ")

try:
    sum_two = float(first_var)+float(second_var)
    print(sum_two)
except:
    print("Addition is not possible")


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[17]:


#a) a for loop
cubes= []
for i in range(11):
    cubes.append(i*i*i)
print(cubes)


# In[18]:


#b) a list comprehension
cubes = [i * i * i for i in range(11)]
print(cubes)


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# In[19]:


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


# In[20]:


a= [(i, j) for i in range(3) for j in range(4)]
print(a)


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[23]:


def pythagoreanTriplets(limits) :
    c, m = 0, 2
    list1=[ ]
    while c < limits :
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            if c > limits :
                break
            
            list1.append(a)
            list1.append(b)
            list1.append(c)
        m = m + 1
        
    to_tup = tuple(list1)
    print(type(to_tup))
    print(to_tup)


limit = 99
pythagoreanTriplets(limit)


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[24]:


import numpy as np

vector = (5,10,5,20)
extra =vector/np.linalg.norm(vector)
print(extra) 
checking = np.sqrt(sum([ex**2 for ex in extra]))
print(checking) 


# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[25]:


fib = 20
n = 0
n1 = 0
n2 = 1
count = 0
while (count<fib):
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    count +=1

