#!/usr/bin/env python
# coding: utf-8

# # 01ex_introduction

# In[1]:


# 1. The HelloWorld replacement

a1 = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("HelloWorld")
        a1.append("HelloWorld")
    elif number % 3 == 0:
        print("Hello")
        a1.append("Hello")
    elif number % 5 == 0:
        print("World")
        a1.append("World")
    else:
        print(number)
        a1.append(number)

for item in range(len(a1)):
    if a1[item] == 'Hello':
        a1[item] = "python"
    elif a1[item] == 'World':
        a1[item] = "Works"

b = tuple(a1)
for i in range(len(b)):
    print(b[i])


# In[2]:


# 2. The swap

def swap_func(x, y):
    x, y = y, x
    return x, y

print(swap_func("Seyedali", "Hosseinishamoushaki"))


# In[4]:


# 3. Computing the distance


import math


def calculate_distance(d1, d2):
    (x1, y1) = d1
    (x2, y2) = d2
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"distance between two points: {d}")


calculate_distance((7, 0), (0, 9))


# In[5]:


# 4. Counting letters


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


def counter(string):
    char_list = []
    count_char = {}

    string = string.lower()

    for i in range(len(string)):    
        if string[i] not in char_list:
            char_list.append(string[i])

        elif string[i] in char_list:
            pass

    for i in range(len(char_list)):
        count_char[char_list[i]] = string.count(string[i])

    return count_char


print(counter(s1))
print(counter(s2))


# In[6]:


# 5. Isolating the unique


L = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20,
     54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


def unique_isolator(N):
    tem = []
    for item in N:
        if item not in tem:
            tem.append(item)
    return len(tem), tem


print("Unique number count of the list: " + str(unique_isolator(L)[0]))
print("New list: " + str(unique_isolator(L)[1]))


# In[7]:


# 6. Casting


a = input("1st : ")
b = input("2st: ")

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
    z = "Unacceptable"
    print(z)


# In[8]:


# 7. Cubes


# a) for loop

list_a = []
for i in range(0, 11):
    list_a.append(i ** 2)
print(list_a)


# b) list comprehension

list_b = [i ** 2 for i in range(0, 11)]
print(list_b)


# In[9]:


# 8. List comprehension


a2 = [(i, j) for i in range(3) for j in range(4)]
print(a2)


# In[11]:


# 9. Nested list comprehension


Nested_list = [(a, b, c) for a in range(1, 101)
               for b in range(1, 101)
               for c in range(1, 101)
               if a ** 2 + b ** 2 == c ** 2]

print(Nested_list)


# In[12]:


# 11. The Fibonacci sequence


n = 20
fibonacciSeries = [1, 1]
if n > 2:
    for i in range(2, n):
        nextOne = fibonacciSeries[i - 1] + fibonacciSeries[i - 2]
        fibonacciSeries.append(nextOne)

print(fibonacciSeries)


# In[ ]:




