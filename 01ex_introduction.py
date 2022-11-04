#!/usr/bin/env python
# coding: utf-8

# # 01ex_introduction

# In[5]:


'''
1. The HelloWorld replacementl
a) Write a program that:
prints the numbers from 1 to 100
but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
for numbers which are multiples of both three and five print "HelloWorld".
b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".
'''


a = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("HelloWorld")
        a.append("HelloWorld")
    elif number % 3 == 0:
        print("Hello")
        a.append("Hello")
    elif number % 5 == 0:
        print("World")
        a.append("World")
    else:
        print(number)
        a.append(number)

for item in range(len(a)):
    if a[item] == 'Hello':
        a[item] = "python"
    elif a[item] == 'World':
        a[item] = "Works"

b = tuple(a)
for i in range(len(b)):
    print(b[i])


# In[6]:


'''
2. The swap
Write a program that swaps the values of two input variables x and y from command line (whatever the type).
Try to do that without using a temporary variable, exploiting the Python syntax.
'''

def swap_func(x, y):
    x, y = y, x
    return x, y

print(swap_func("mahsa", "shahbazi"))


# In[7]:


'''
3. Computing the distance
Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).
Example: if u=(3,0) and v=(0,4), the function should return 5.
Hint: in order to compute the square root, import the math library with import math and use math.sqrt().
'''

import math

def calculate_distance(d1, d2):
    (x1, y1) = d1
    (x2, y2) = d2
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"distance between two points: {d}")


calculate_distance((3, 0), (0, 4))


# In[8]:


'''
4. Counting letters
Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
'''



s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def char_counter(string):
    list_of_char = []
    count_char = {}

    string = string.lower()

    for i in range(len(string)):
        if string[i] not in list_of_char:
            list_of_char.append(string[i])

        elif string[i] in list_of_char:
            pass

    for i in range(len(list_of_char)):
        count_char[list_of_char[i]] = string.count(string[i])

    return count_char


print(char_counter(s1))
print(char_counter(s2))


# In[9]:


'''
5. Isolating the unique
Write a program that determines and counts the unique numbers in the list.
'''

L = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20,
     54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


def unique_isolator(arr):
    tem = []
    for item in arr:
        if item not in tem:
            tem.append(item)
    return len(tem), tem


print("Unique number count of the list: " + str(unique_isolator(L)[0]))
print("New list: " + str(unique_isolator(L)[1]))


# In[10]:


'''
6. Casting
Write a program that:
reads from command line two variables, that can be either int, float, or str.
use the try/except expressions to perform the addition of these two variables, only if possible
and print the result without making the code crash for all the int/float/str input combinations.
'''

a = input("enter first item: ")
b = input("enter second item: ")

try:
    if a.isalpha() and b.isalpha() == 1:
        z = str(a) + str(b)
        print(z)
    else:
        if a.isnumeric() and b.isnumeric() == 1:
            z = int(a) + int(b)
            print(z)
        else:
            z = float(a) + float(b)
            print(z)

except:
    z = "impossible"
    print(z)


# In[11]:


'''
7. Cubes
Create a list of the cubes of x for x in [0, 10] using:
a) a for loop
b) a list comprehension
'''

# a) for loop
list_1 = []
for i in range(0, 11):
    list_1.append(i**2)
print(list_1)

# b) list comprehension
list_2 = [i**2 for i in range(0, 11)]
print(list_2)


# In[12]:


'''
8. List comprehension
Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
'''

a = [(i, j) for i in range(3) for j in range(4)]
print(a)


# In[13]:


'''
9. Nested list comprehension
Find and put in a tuple all unique Pythagorean triples for
the positive integers  𝑎 ,  𝑏  and  𝑐  with  𝑐<100 .
'''

nested_list = [(a, b, c) for a in range(1, 101)
               for b in range(1, 101)
               for c in range(1, 101)
               if a ** 2 + b ** 2 == c ** 2]

print(nested_list)


# In[34]:


'''
10. Normalization of a N-dimensional vector
Write a program that takes an N-dimensional vector,
e.g. a variable-length tuple of numbers, and normalizes it
to one (in such a way that the squared sum of all the entries
is equal to 1).
'''

vector_1 = float(input("insert the s:"))
vector_2= float(input("insert the h:"))
vector_3= float(input("insert the m:"))
vector=(vector_1,vector_2,vector_3)
mylist1 , sum = [] , 0
for i in vector:
    sum = sum + i**2
dist = sum**0.5
print(f"The normalized vector is: \n{[i/dist for i in vector]}")


# In[35]:


'''
11. The Fibonacci sequence
Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.
'''

N = 20
fibonacciSeries = [1, 1]
if N > 2:
    for i in range(2, N):
        nextElement = fibonacciSeries[i - 1] + fibonacciSeries[i - 2]
        fibonacciSeries.append(nextElement)

print(fibonacciSeries)


# In[ ]:




