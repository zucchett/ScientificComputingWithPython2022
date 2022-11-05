#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''1. The HelloWorld replacement

a) Write a program that:
prints the numbers from 1 to 100
but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
for numbers which are multiples of both three and five print "HelloWorld".
'''
hello_world_list = []
print('Hello World + Numbers:')
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('HelloWorld')#print number/text
        hello_world_list.insert(i, "HelloWorld")#create new element in HelloWorldList
    elif i % 3 == 0:
        print('Hello')
        hello_world_list.insert(i, "Hello")
    elif i % 5 == 0:
        print('World')
        hello_world_list.insert(i, "World")
    else:
        print(i)
        hello_world_list.insert(i, i)

print('List of Hello World + Numbers:')        
print(hello_world_list)
'''b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".'''
#Tuple cannot be changed, so we need first change the words in list and only after make a tuple
print('Tuple of Python Works:')
for index, item in enumerate(hello_world_list):
    if item == 'Hello':
        hello_world_list[index] = 'Python'
    elif item == 'World':
        hello_world_list[index] = 'Works'
#Now we can convert list to tuple
print(tuple(hello_world_list))


# In[ ]:


'''2. The swap

Write a program that swaps the values of two input variables x and y from command line (whatever the type).
Try to do that without using a temporary variable, exploiting the Python syntax.'''

x, y = input("Set x: "), input("Set y: ")
x, y = y, x
print(x, y)


# In[ ]:


'''3. Computing the distance

Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).
Example: if u=(3,0) and v=(0,4), the function should return 5.
Hint: in order to compute the square root, import the math library with import math and use math.sqrt().
'''
import math
def euclid(u,v):
    s = math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
    return s

u = (3, 0)
v = (0, 4)
euclid(u,v)


# In[ ]:


'''4. Counting letters

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
The strings are in the cell below.
'''
s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

print(s1)
s1_dict = {} #create a dictionary to count symbol and its number
for i in s1.lower(): #to ignore the difference in upper and lower case convert all to lowercase
    if i in s1_dict:
        s1_dict[i] += 1
    else:
        s1_dict[i] = 1
for i in s1_dict:
    print(i, s1_dict[i])
    
#repeat for s2
print(s2)
s2_dict = {}
for i in s2.lower():
    if i in s2_dict:
        s2_dict[i] += 1
    else:
        s2_dict[i] = 1
for i in s2_dict:
    print(i, s2_dict[i])


# In[ ]:


'''5. Isolating the unique

Write a program that determines and counts the unique numbers in the list:
'''
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
#we can convert list in set, because set does not support duplicates.
print('Unique numbers in list: ', set(l), '\nNumber of unique numbers in list:', len(set(l)))


# In[ ]:


'''6. Casting

Write a program that:
reads from command line two variables, that can be either int, float, or str.
use the try/except expressions to perform the addition of these two variables, 
only if possible and print the result without making 
the code crash for all the int/float/str input combinations.'''
a, b = input('set a '), input('set b ')
try:
    c = int(a) + int(b)
    print(c)
except:
    try:
        c = int(a) + float(b)
        print(c)
    except:
        try:
            c = float(a) + int(b)
            print(c)
        except:
            try:
                c = float(a) + float(b)
                print(c)
            except:
                print('at least one of variables is a string so addition is impossible')


# In[ ]:


'''7. Cubes

Create a list of the cubes of x for x in [0, 10] using:
a) a for loop
b) a list comprehension'''

x3 = []
for x in range(11):
    x **= 3
    x3.append(x)
print('a) Using for loop: ', x3)

print('b) Using list comprehension: ', [x**3 for x in range(11)])


# In[ ]:


'''8. List comprehension

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)'''

print([(i,j) for i in range(3) for j in range(4)])


# In[ ]:


'''9. Nested list comprehension

A Pythagorean triple is an integer solution to the Pythagorean theorem  𝑎2+𝑏2=𝑐2 . The first Pythagorean triple is (3, 4, 5).
Find and put in a tuple all unique Pythagorean triples for the positive integers  𝑎 ,  𝑏  and  𝑐  with  𝑐<100 .'''

i = 100
print([(a, b, c) for a in range(1, i + 1) for b in range(a, i + 1)
       for c in range(b, i + 1) if a**2 + b**2 == c**2])


# In[ ]:


'''10. Normalization of a N-dimensional vector

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one 
(in such a way that the squared sum of all the entries is equal to 1).'''

import math
vector = (5, 5, 4, 6)
sumx2 = 0
for x in vector:
    sumx2 += x**2

length = math.sqrt(sumx2)
norm_vector = []
for x in vector:
    norm_vector.append(x/length)
print(norm_vector)


# In[ ]:


'''11. The Fibonacci sequence

Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.'''

fib_range = []
for i in range(20):
    if i <= 1:
        fib_range.append(1)
    else:
        fib_range.append(fib_range[i - 2] + fib_range[i - 1])
print(fib_range)

