#Anaïs_fragne

#1/a.
#b.

my_list=[i for i in range(100)]
#print(my_list)
for i in range(100):
    if (i+1)%3==0 and (i+1)%5==0:
        print ('Hello World')
        my_list[i]='Python Works'
    elif (i+1)%3==0:
        print('Hello')
        my_list[i]='Python'
    elif (i+1)%5==0:
        print('World')
        my_list[i]='Works'
    else:
        print(i+1)
        my_list[i]=i+1
my_tuple=tuple(my_list)
print(my_tuple)


#2/
y=input("Enter the variable x:\n")
x=input("Enter the variable y:\n")


print('x=',x)
print('y=',y)

#3/
import math
def dist(u,v):
    dist1=((v[0]-u[0])**2)+((v[1]-u[1])**2)
    dist=math.sqrt(dist1)
    print(dist)
u=(3,4)
v=(5,6)
dist(u,v)

#4/
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


def occurs(s):
    count={}
    s=s.lower()
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    print('occurs_: ',count)
occurs(s1)
occurs(s2)
                
#5/
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]



def unique(l):
    unique_list = []
    for x in l:
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list

print("There is : " ,len(unique(l)),"unique numbers in the list l which are: ", unique(l))


#-------Python data structure----------------

num_values = len(set(l))
print('num_unique_values: ',num_values)

#6

var1=input("Enter the variable 1:\n")
var2=input("Enter the variable 2:\n")
def q6(a,b):
    try:
        a=int(a)
        b=int(b)
        c = a + b
        print(c)
    except ValueError:
        try: 
            a=float(a)
            b=float(b)
            c = a + b
            print(c)
        except:
            print("this sum is not a number")
        
q6(var1,var2)
q6(4,'2')

#7
#a.----for loop
l1=[]
for i in range(11):
    l1.append(i**3)
print("List_forloop: ", l1)

#b.----list comprehension
l=[i**3 for i in range(11)]
print("List_comprehension: ",l)

#8
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

#---------with list comprehension

l=[(i,j) for i in range(3) for j in range(4)]
print(l)

#9
#-----without nested list
   
def triplet(n):
  for c in range(n):
    for b in range(c):
      for a in range(b):
        if c*c == a*a + b*b:
          print(a, b, c)
n=100
triplet(n)

#----with nested list

t=[(a,b,c) for c in range(100) for b in range(c) for a in range(b) if c*c == a*a + b*b]
t=tuple(t)
print(t)

#10
from numpy import linalg as la
import numpy as np
import math as m
N=10
arr = np.random.rand(N)
print(arr)
normalized_vector = arr / np.linalg.norm(arr)
print('normalized_vector= ',normalized_vector)

#-----without numpy
N=10
import random
import math as m
arr2=tuple(random.random() for i in range(N))
print('arr2= ',arr2)
norm=m.sqrt(sum(i**2 for i in arr2))
print('norm= ',norm)
normalized2=tuple(e/norm for e in arr2)
print('normalized2= ', normalized2)

#11
l=[]
f=0
fp=1
for i in range(20):
    if i<=1:
        l.append(i)
    else:
        fpp=f+fp
        f=fp
        fp=fpp
        l.append(fpp)
print(l)
