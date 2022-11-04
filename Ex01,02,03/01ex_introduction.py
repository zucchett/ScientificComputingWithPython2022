"""1\. **The HelloWorld replacement**

a) Write a program that:
- prints the numbers from 1 to 100
- but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
- for numbers which are multiples of both three and five print "`HelloWorld`".

b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`"."""

t_insert=list()
for i in range(1,100):
	if (i%3==0 and i%5==0):
		print("HelloWorld")
		t_insert.append("Python Works")
	elif (i%3==0):
		print("Hello")
		t_insert.append("Python")
	elif (i%5==0):
		print("world")
		t_insert.append("Works")
	else:
		print(i)
		t_insert.append(i)
t=tuple(t_insert)
tuple1 = list(t)
for i in t_insert:
	if i == "Hello":
		tuple1.append("Python")
	elif i == "world":
		tuple1.append("Works")
	else:
		tuple1.append(i)
print(tuple(tuple1))


"""2. The swap

Write a program that swaps the values of two input variables x and y from command line (whatever the type).

Try to do that without using a temporary variable, exploiting the Python syntax."""

x = input("enter a variable")
y = input("enter a variable")

x,y = y,x
print("x =",x,"y =",y)


"""3. Computing the distance

Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).

Example: if u=(3,0) and v=(0,4), the function should return 5.

Hint: in order to compute the square root, import the math library with import math and use math.sqrt()."""

import math
def get_distance_between_two_points(tuple1,tuple2):
    return math.sqrt(pow((tuple1[0]-tuple2[0]),2)+pow((tuple1[1]-tuple2[1]),2))
tuple1 = (3,0)
tuple2 = (0,4)
distance_between_two_points = get_distance_between_two_points(tuple1,tuple2)
print (distance_between_two_points)

"""4. Counting letters

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

The strings are in the cell below."""

a = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(a)
mainlist,mainlist1,mainlist2,m = [], [], [],[] 
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1 = s1.lower().replace(" ","")
s2 = s2.lower().replace(" ","")
s1s2 = s1+s2
for i in alphabet:
    counter1,counter2,counter=0,0,0
    for j in s1:
        if i == j:
            counter1 = counter1 + 1
    mainlist1.append([i,counter1])
    for k in s2: 
        if i == k:
            counter2 = counter2 + 1
    mainlist2.append([i,counter2])
    for l in s1s2: 
        if i == l:
            counter = counter + 1
    mainlist.append([i,counter])
print (mainlist1)
print ("---------------")
print (mainlist2)
print ("---------------")
print (mainlist)

"""5. Isolating the unique

Write a program that determines and counts the unique numbers in the list:"""

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
lset = sorted(set(l))
llist = []
print(" in the list there are ", len(lset) ,"different numbers")
counter = 0
for i in lset:
    counter = 0
    for j in l:
        if i == j:
            counter = counter + 1
    llist.append([i,counter])
print (llist)

"""6. Casting

Write a program that:

reads from command line two variables, that can be either int, float, or str.
use the try/except expressions to perform the addition of these two variables, only if possible
and print the result without making the code crash for all the int/float/str input combinations."""

x,y=input("enter a variable"),input("enter a variable")
try:
    x=float(x)
    if x%1==0:
        x=int(x)
        print(x,"=int")
    else: 
        print(x,"=float")
    try:
        y = float(y)
        if y%1==0:
            y=int(y)
            print(y,"=int")
        else:
            print(y,"=float")
        print(x+y)
    except:
        y = str(y)
        print(y,"= string")
        print("the values are not the same type")
except:
    x = str(x)
    print(x,"= string")
    try:
        y = float(y)
        if y%1==0:
            y=int(y)
            print(y,"=int")
        else:
            print(y,"=float")
        print("the values are not the same type")
    except:
        y = str(y)
        print(y,"= string")
        print(x+y)

"""7. Cubes

Create a list of the cubes of x for x in [0, 10] using:

a) a for loop"""
list_l=[]
for i in range(11):
    list_l.append(pow(i,3))
print(list_l)

"""b) a list comprehension"""
list_l = [pow(x,3) for x in range(11)]
print(list_l)

"""8. List comprehension

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)"""
a = [(i,j) for i in range(3) for j in range(4)]
print(a)

"""9. Nested list comprehension

A Pythagorean triple is an integer solution to the Pythagorean theorem  𝑎2+𝑏2=𝑐2 . The first Pythagorean triple is (3, 4, 5).

Find and put in a tuple all unique Pythagorean triples for the positive integers  𝑎 ,  𝑏  and  𝑐  with  𝑐<100 ."""

import math
list_d = tuple([(i,j,int(math.sqrt(i*i+j*j))) for i in range(1,100) for j in range (1,100) if math.sqrt(i*i+j*j)<100 and math.sqrt(i*i+j*j)%1==0])
print(list_d)

"""10. Normalization of a N-dimensional vector

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1)."""

import math
print("how much dimension")
x,counter = int(input()),1
list_d = []
for i in range(x):
    print("write dimension ", counter)
    list_d.append(int(input()))
    counter = counter + 1
counter = 0
for j in list_d:
    counter = counter + pow(j,2)
a = math.sqrt(counter)
counter = 0
for k in list_d:
    k  = k/a
    counter = counter + pow(k,2)
print (counter)

"""11. The Fibonacci sequence

Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops."""

counter = 0
fibonacci=[]
f1 , f2 = 0,1
for i in range(0,20):
    fibonacci.append(f1)
    counter = f1 + f2
    f1 = f2
    f2 = counter
print(fibonacci)