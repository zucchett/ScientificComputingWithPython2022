"""
Umut Berk Cakmakci
Week-1 Exercises

"""

""
# 01ex_introduction_es01

list_a = []
for i in range(1, 101, 1):
    if i%15 == 0:
        y="HelloWorld"
        #print(y)
    elif i%5 == 0:
        y="World"
        #print(y)
    elif i%3 == 0:
        y="Hello"
       # print(y)
    else:
        y=i
        #print(i)
        
    list_a.append(y)
    
print(list_a)

list_b = str(list_a)
list_b = list_b.replace('Hello', 'Python')
list_b = list_b.replace('World', 'Works')
print(list_b)
""

"""
# 01ex_introduction_es02

x = input("enter x: ")
#print(x)
y = input("enter y: ")
#print(y)

print("the existing value of x:", x)
print("the existing value of y:", y)

x, y = y, x

print("the new value of x:", x)
print("the new value of y:", y)
"""

"""
# 01ex_introduction_es03

import math

#u1 = int(input("enter u1: "))
#u2 = int(input("enter u2: "))
#v1 = int(input("enter v1: "))
#v2 = int(input("enter v2: "))

u = (8,5)
v = (1,2)

a = (u[0]-v[0])**2
b = (u[1]-v[1])**2
z = math.sqrt(a+b)

print("z:", z)
"""

"""
# 01ex_introduction_es04

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s11 = s1.lower()
s21 = s2.lower()

a = len(s11)
b = len(s21)

c = []
d = []

for i in range(0, a, 1):
    if s11[i] in c:
        i
    else:
        print("list s1,", s11[i],s11.count(s11[i]))
        c.append(s11[i])

print("---------------")

for j in range(0, b, 1):
    if s21[j] in d:
        j
    else:
        print("list s2,", s21[j],s21.count(s21[j]))
        d.append(s21[j])
"""

"""
# 01ex_introduction_es05

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

a = len(l)

c = []
print("list_l num counts")
for i in range(0, a, 1):
    if l[i] in c:
        i
    else:
        print("list_l,", l[i], l.count(l[i]))
        c.append(l[i])
"""

"""
# 01ex_introduction_es06

var1 = input("Type the first variable: ")
var2 = input("Type the second variable: ")
print(type(var1))
print(type(var2))

var1 = int(var1)
var2 = int(var2)
try:
    print(var1+var2)
except:
    print("The 2 variables cannot be sum because their types are different.")
"""

"""
# 01ex_introduction_es07

cubes = []
for x in range(10):
    cubes.append((x+1)**3)
print(cubes)

print([(x+1)**3 for x in range(10)])
"""

"""
# 01ex_introduction_es08

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

print([(x, y) for x in range(3) for y in range(4)])
"""

"""
# 01ex_introduction_es09

import math
x = []

for a in range(1, 100, 1):
    for b in range (1, 100, 1):
        c = a**2 + b**2
        c2 = math.sqrt(c)
        c3 = str(c2)
        if c3.endswith(".0") and c2 < 100:
            x.append((a, b, c2))
        else:
            #print(type(c2), c2)
            c
print(x)
"""

"""
# 01ex_introduction_e10

import math

x = list(map(int, input("Enter multiple values: ").split()))
print("The N-dimensional vector is: ", x)

a=len(x)
list2=[]
x2=0

for i in range(0, a, 1):
    x2=x2+x[i]**2

x2=math.sqrt(x2)
print("The length of the N-dimensional vector is: ", x2)

for j in range(0, a, 1):
    list2.append(x[j]/x2)

print("The normalized N-dimensional vector is: ", list2)
"""

"""
# 01ex_introduction_e11

fib = [0, 1]

for i in range(2, 20, 1):
    fib.append(fib[i-1]+fib[i-2])

print(fib)
"""

