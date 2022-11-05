import os

# 1. The HelloWorld replacement
# a)

print("\n 1. The HelloWorld replacement \n a) \n")

for i in range(100):
  if ((i+1) % 3 == 0 and (i+1) % 5 == 0):
    print("HelloWorld")
  elif (i+1) % 3 == 0:
    print("Hello")
  elif (i+1) % 5 == 0:
    print("World")
  else:
    print(i+1)
  
# b)

print("\n 1. The HelloWorld replacement \n b) \n")

lst = []

for i in range(100):
  if ((i+1) % 3 == 0 and (i+1) % 5 == 0):
    lst.append("HelloWorld")
  elif (i+1) % 3 == 0:
    lst.append("Hello")
  elif (i+1) % 5 == 0:
    lst.append("World")
  else:
    lst.append(str(i+1))
    
tple = tuple(lst)
lst = list(tple)

for i in range(100):
  if (lst[i] == "Hello"):
    lst[i] = "Python"
  elif (lst[i] == "World"):
    lst[i] = "Works"
  elif (lst[i] == "HelloWorld"):
    lst[i] = "PythonWorks"
    
tpl = tuple(lst)
tpl

# 2. The Swap

x = input("Set the value of x: ")
y = input("Set the value of y: ")

x, y = y, x
print("x =", x)
print("y =", y)

# 3. Computing the distance

import math

def euclideanDistance(u,v):
    return math.sqrt(u[0]**2 + u[1]**2 + v[0]**2 + v[1]**2)

x = (3,0)
y = (0,4)
euclideanDistance(x,y)

# 4. Counting Letters

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def count(s, l):
     
    count = 0
    
    for i in range(len(s)) :
         
        if (s[i] == l):
            count = count + 1
    return count
     
print(count(s1,"r"))
print(count(s2,"f"))

# 5. Isolating the unique

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
import numpy as np

uniqueList = np.unique(l)

print("Unique numbers are: " + str(uniqueList))
uniqueList
print("Number of unique numbers is: " + str(len(uniqueList)))

# 6. Casting

x = input()
y = input()

try:
    res = x + y
    print(res)
except:
    print("int/float/str states are not suitable for operation")
    
# 7. Cubes

cube_for = []

#for

for i in range(10):
    cube_for.append(i**3)
    
print(cube_for)
    
#list comprehension

cube_listh = [x**3 for x in range(10)]
print(cube_listh)

# 8. List comprehension

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

a = [(i,j) for i in range(3) for j in range(4)]
print(a)

# 9. Nested list comprehension

print("I couldn't make this part work.")

# 10. Normalization of a N-dimensional vector

N = np.random.randint(2, 10)

tup = np.random.random((N, 1))

tpl = tup / np.sqrt(np.sum(tup**2))
tpl = tuple(tpl)
print(tpl)

# 11. The Fibonacci sequence

fibo = [0, 1]

for i in range(20-2):
    fibo.append(fibo[-2] + fibo[-1])
    
print(fibo)




