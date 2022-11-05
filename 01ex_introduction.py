#1. The HelloWorld replacement
a = []
for i in range(1,101):
    if i % 15 ==0:
        print("HelloWorld")
        a.append("PythonWorks")
    elif i % 3 ==0:
        print("Hello")
        a.append("Python")
    elif i % 5 ==0:
        print("World")
        a.append("Works")
    else:
        print(i)
        a.append(i)
my_tuple=tuple(a)
print(my_tuple)

#2. The swap
x = input("Set the value of x: ")
y = input("Set the value of y: ")
x , y = y , x
print ("x=",x)
print ("y=",y)

#3. Computing the distance
import math
def eu_d(u, v):
    a = (u[0] - v[0])**2
    b = (u[1] - v[1])**2
    print("Euclidean Distance: ", math.sqrt((a+b)))

u = (3,0)
v = (0,4)
print("Point 1: ", u)
print("Point 2: ", v)
eu_d(u,v)

#4. Counting letters
from collections import Counter
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
c1 = Counter(s1.lower())
c2 = Counter(s2.lower())
print(c1)
print(c2)

#5. Isolating the unique (Part 1)
import numpy as np
from numpy import array
from numpy import unique
from collections import Counter

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


x = np.array(l)
print("Unique numbers list: " , np.unique(x))
num_values = len(set(x))
print("There are", num_values, "unique numbers")

#5. Isolating the unique (Part 2)

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique_list = []
num_values = 0
for x in l:
  if x not in unique_list:
      unique_list.append(x)
      num_values += 1
print("Unique numbers list: ", unique_list)
print("There are", num_values, "unique numbers")

# 6. Casting
x = input("Enter your variable x: ")
y = input("Enter your variable y: ")
try:
    a = float(x) + float(y)
    print("Sum of numbers:", a)
except:
    a = x + y
    print("Sum of strings:", a)

#7. Cubes (Part 1)
l = []
for a in range(10):
   a=a**3
   l.append(a)
print(l)

#7. Cubes (Part 2)
cubes = [x**3 for x in range(10)]
print(cubes)

#8. List comprehension
a = [(i,j) for i in range(3) for j in range(4)]
print(a)

#9. Nested list comprehension
a = [(i,j,k) for i in range(1,100) for j in range(1,100) for k in range(1,100) if i**2 + j**2 == k**2]
print(a)

#10. Normalization of a N-dimensional vector
import math
t = (1,2,3)
n = []
f = 0
for i in range(len(t)):
    f = f + t[i]**2
f = math.sqrt(f)
for i in range(len(t)):
    n.append(t[i]/f)
my_tuple=tuple(n)
print(my_tuple)

# 11. The Fibonacci sequence
fibonacci = []
for i in range(1, 20):
    if n == 1:
        fibonacci = [0]
    else:
        fibonacci = [0, 1]
        for i in range(1, 19):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i])
print(fibonacci)

