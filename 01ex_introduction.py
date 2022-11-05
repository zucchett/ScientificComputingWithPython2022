#es. 1

print()
print("The HelloWorld replacement")
print()

list_1 = []

for i in range (1,101,1):
    if i % 5 == 0 and i % 3 == 0:
        i = "HelloWorld"
        list_1.append(i)
    elif i % 5 == 0:
        i = "World"
        list_1.append(i)
    elif i % 3 == 0:
        i = "Hello"
        list_1.append(i)
    else:
        list_1.append(i)

for i in list_1:
    if i == "Hello":
        j = list_1.index(i)
        list_1 = list_1[:j]+["Python"]+list_1[j+1:]
    elif i == "World":
        j = list_1.index(i)
        list_1 = list_1[:j]+["Works"]+list_1[j+1:]
    elif i == "HelloWorld":
        j = list_1.index(i)
        list_1 = list_1[:j]+["PythonWorks"]+list_1[j+1:]
    else:
        i = i

print(tuple(list_1))

#es. 2

print()
print("The swap")
print()

x = input("insert x:")
y = input("insert y:")
x, y = y, x
print ("x:",x,"y:",y)

#es. 3

print()
print("Computing the distance")
print()

from random import randint

def euclidean(u,v):
    import math
    u1,u2 = u
    v1,v2 = v
    d = math.sqrt(pow(u[1]-u[0],2)+pow(v[1]-v[0],2))
    return d

res = euclidean([randint(1,100), randint(1,100)],[randint(1,100), randint(1,100)])

print(res)

#es. 4

print()
print("Counting letters")
print()


s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


def countlet(s):

    i = 0
    l = []
    s = s.lower()

    while i < len(s):
        m = s[i]+"="+str(s.count(s[i]))
        l.append(m)
        i = i+1

#rimuovere i doppioni (conteggio stessa lettera)

    j = len(l)-1
    c = 0

    while j > 0:
        if l.count(l[j]) > 1:
            l.remove(l[j])
            c = c+1
        if c != 0:
            j = len(l)-1
            c = 0
        else:
            j = j-1

    return tuple(l)

print(countlet(s1))
print(countlet(s2))

#es. 5

print()
print("Isolating the unique")
print()

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l1 = []
i = 0

while i < len(l):
    if l.count(l[i]) == 1:
        l1.append(l[i])
    i = i+1

print(sorted(l1))
print()
print("the number of unique numbers is:", len(l1))

#es. 6

print()
print("Casting")
print()

x = input("insert number or character:")
y = input("insert number or character:")

try:
    x = int(x)
    y = int(y)
    z = x + y
    print("adding them equals to:",z)

except:

    try:
        x = float(x)
        y = float(y)
        z = x+y
        print("adding them equals to:",z)

    except:
        print(x, "or", y, "is not a number so I can't add them")

#es. 7

print()
print("Cubes")
print()

l1 = []
l2 = []

for x in range (0,11,1):
    l1.append(x)
    l2.append(pow(x,3))

print('a:',l2)

l3 = [pow(x,3) for x in l1]

print('b:',l3)

#es. 8

print()
print("List comprehension")
print()

a = []
for i in range(3):
    for j in range(4):
        a.append((i,j))
print(a)

b = [(i,j) for j in range(4) for i in range(3)]

print(b)

#es. 9

print()
print("Nested list comprehension")
print()

nl = [(a,b,c) for c in range (1,100,1) for b in range (1,100,1) for a in range (1,100,1) if pow(c,2) == pow(a,2) + pow(b,2)]

i = len(nl)-2

#per far comparire una terna una volta sola

while i >= 0:
    nl.remove(nl[i])
    i = i - 2

print("all unique Pythagorean triples for the positive integers < 100:", tuple(nl))

#es. 10

print()
print("Normalization of a N-dimensional vector")
print()

from random import randint
from math import sqrt

N = randint(1,100)
i = 0
vector = []

while i < N:
    vector.append(randint(0,100))
    i = i+1

sum = 0
for i in vector:
    sum = sum+pow(i,2)

V = sqrt(sum)
vector1 = []

i = 0
while i < len(vector):
    vector1.append(vector[i]/V)
    i = i + 1

sum = 0
for i in vector1:
    sum = sum+pow(i,2)

V1 = sqrt(sum)

print()
print(vector1)
print()
print(V)
print()
print("check:", V1)

#es. 11

print()
print("The Fibonacci sequence")
print()

n1 = 0
n2 = 1
c = 0
l = []

while c < 20:
    l.append(n1)
    n = n1+n2
    n1 = n2
    n2 = n
    c = c+1

print(tuple(l))
