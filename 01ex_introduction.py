import math
from collections import Counter

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:42:16 2022

@author: daria
"""

#The HelloWorld replacement
print("--- THE HELLOWORLD REPLACEMENT ---\n")

i = 1
list = []
while i <= 100:
    if (i % 3 == 0 and i % 5 == 0):
        print("HelloWorld")
        list.append("PythonWorks")
    elif (i % 3 == 0):
        print("Hello")
        list.append("Python")
    elif(i % 5 == 0):
        print("World")
        list.append("Works")
    else: 
        print(i)
        list.append(i)
    i += 1
    
my_tuple = tuple(list)
print(my_tuple)

#The swap
print("\n--- THE SWAP ---")

x = input("Insert input variable x: ")
y = input("Insert input variable y: ")
x, y = y, x
print("\nx = ", x)
print("y = ", y)

#Computing the distance
print("\n--- COMPUTING THE DISTANCE ---\n")

def EuclideanDistance(u: tuple, v: tuple):
    z = math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
    print("Euclidean distance between", u, "and", v, "is: ", z)

EuclideanDistance((3, 0), (0, 4))    
EuclideanDistance((5, 2), (5, 1))
EuclideanDistance((5, 2), (6, 1))

#Counting letters
print("\n--- COUNTING LETTERS ---\n")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the \
multiples of five print World. For numbers which are multiples of both three \
and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

collection1 = Counter(s1.lower())
print("Occourance of each letter: \n", collection1)
collection2 = Counter(s2.lower())
print("Occourance of each letter: \n", collection2)

#Isolating the unique
print("\n--- ISOLATING THE UNIQUE ---\n")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

dictionary={}
for x in l:
    if x in dictionary:
        dictionary[x] = dictionary[x] + 1
    else:
        dictionary[x] = 1
        
unique_list = []
for x in dictionary:
    if dictionary[x] == 1:
        unique_list.append(x)
           
print("Number of unique numbers is: ", len(unique_list))

#exploiting only python data structure
unique_list1 = [x for x in l if l.count(x)==1]
print("Number of unique numbers is: ", len(unique_list1))

#Casting
print("\n--- CASTING ---")

var1 = input("Insert first input variable (int, float, or str): ")
var2 = input("Insert second input variable (int, float, or str): ")
try:
    varSum = float(var1) + float(var2)
    print("Addition of variables is: ", varSum)
except ValueError:
    varSum = var1 + var2
    print("Addition of variables is: ", varSum)
    
#Cubes
print("\n--- CUBES ---\n")

xvalues = [i for i in range(11)]
xcubes=[]
for x in xvalues:
    xcubes.append(x**3)
print("List of cubes obtained with for loop: ", xcubes)
xcubes1 = [x**3 for x in xvalues]
print("List of cubes obtained with list comprehension: ", xcubes1)

#List comprehension
print("\n--- LIST COMPREHENSION ---\n")

a = [(i, j) for i in range(3) for j in range(4)]
print(a)

#Nested list comprehension   
print("\n--- NESTED LIST COMPREHENSION ---\n")

climit = 100
m = 2
c = 1
while c < climit:
    for n in range(1,  m):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
 
        if c >= climit:
            break;

        t = (a, b, c)
        print(t)
    m = m + 1

#Normalization of a N-dimensional vector
print("\n--- NORMALIZATION OF A N-DIMENSIONAL VECTOR ---\n")

my_tuple = (2, 4, -1)
print("My vector: ", my_tuple)
normcoeff = math.sqrt(sum(x**2 for x in my_tuple))
my_normalizedlist = [x/normcoeff for x in my_tuple]
my_normalizedtuple = tuple(my_normalizedlist)
print("My normalized vector: ", my_normalizedtuple)
print("Squared sum of all entries in", my_normalizedtuple, "is", sum(t**2 for t in my_normalizedtuple))

#The Fibonacci sequence
print("\n--- THE FIBONACCI SEQUENCE ---\n")

Fibonacci=[0, 1]
a=0
b=1
for i in range(18):
    Fibonacci.append(a+b)
    a, b = b, a+b

print("The first 20 numbers of the Fibonacci sequence are: ", Fibonacci)
