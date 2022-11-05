#!/usr/bin/env python
# coding: utf-8

# Ceren Yılmaz Gülten 
# Exercise 01 
# 

# In[40]:


# 1.HelloWorld Replacement
t=()
L =list(t)
for i in range(1,101,1):
    if i%3==0 and i%5==0:
        L.append("HelloWorld")
    elif i%3==0:
        L.append("Hello")
    elif i%5==0 :
        L.append("World")
    else:
        L.append(i)
i+=1  
t = tuple(L)
print(t)
for j in range(len(L)):
    if L[j] == 'Hello':
        L[j] = 'Python'
    elif L[j]== 'World':
        L[j] = 'Works'
a = tuple(L)
print(a)


# In[44]:


# 2.The Swap
x = input("Enter a value for x:")
y = input ("Enter a value for y:")

x, y = y, x 
print("Value of the x=" + x)
print("Value of the y=" + y)


# In[50]:


# 3.Computing the distance
import math 
u = (6,0)
v = (0,8)
k= u[0]-v[0]
euclidean_distance = math.sqrt(pow(u[0]-v[0],2) + pow(u[1]-v[1],2))
print(euclidean_distance)


# In[74]:


# 4.Counting Letters 
s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."  
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
s2 = s2.lower()

temp1 = {}
temp2 ={}
temp3 = {}

for i in s1:
    if i in temp1:
        temp1[i] += 1
    else:
        temp1[i] = 1
        
for j in s2:
    if j in temp2:
        temp2[j] += 1
    else:
        temp2[j] = 1
for k in (s1 + s2):
    if k in temp3:
        temp3[k] += 1
    else:
        temp3[k] =1

print ("Count of the characters in s1 :\n "+  str(temp1))
print ("Count of the characters in s2:\n "+  str(temp2))
print ("Count of the characters in s1 + s2:\n "+  str(temp3))


# In[149]:


# 5. Isolating the unique ????

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
k = []
r = {}
for j in l:
    r[j] = l.count(j)
for i in range(0,len(l)):
    if l[i] in k:
        continue
    else:
        k.append(l[i])     
print(k)
print(r)

#with set function for data structure 
z = set(l)
print(z)


# In[204]:


# 6. Casting
a = input("Enter a value for a:")
b = input ("Enter a value for b:")
try :
    a = int(a)
except: 
    try: 
        a = float(a)
    except: 
        a = str(a)
try :
    b = int(b)
except: 
    try: 
        b = float(b)
    except: 
        b = str(b)
print(type(a))
print(type(b))
try:
    c = a + b
    print(c)
except:
    print(" can not calculate")


# In[4]:


# 7. Cubes 
# a. for loop

k = []
for x in range(0,11):
    k.append(pow(x,3)) 
print(k)

# b. list comprehension

cubes = [pow(x,3) for x in range(0,11)]
print(cubes)


# In[8]:


# 8. List Comprehension 

# given code 
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print("Given code with for loop:", a)

# single line code with list comprehension 
a = [(i,j) for i in range(3) for j in range(4)]
print("List comprehension: " , a)


# In[36]:


# 9. Nested List Comprehension 
# using for loop 
k=[]
t = {}
for a in range(1,100):
    for b in range(1,100):
        for c in range(1,100):
            if  pow(a,2) + pow(b,2) == pow (c,2):
                k.append((a,b,c))
t = tuple(k)
print("With loop: ",t , "\n")

# using nested list comprehension 

l = [(a,b,c) for a in range(1,100) for b in range(1,100) for c in range(1,100) if pow(a,2) + pow(b,2) == pow (c,2)]
m = tuple(l)
print("With Comprehension: ",m)


# In[43]:


# 10. Normalization of a N-dimensional vector

# n-dimentional vector = (x_1, x_2, x_3,....,x_n)
import math 
a = (1,2,34,67,43,12,90,54)
#a=[3,4,5]
print(a)
sum=0
sum_2 =0
normalized=[]
for i in range(len(a)):
    sum += (a[i])**2 
for i in range(len(a)):    
    normalized.append(a[i] / math.sqrt(sum))
# to check 
for i in range(len(normalized)):
    sum_2 += (normalized[i]**2)
t = tuple(normalized)
print(t)

print(sum_2)


# In[92]:


# 11. The Fibonacci sequence

# with for loop 
fib = [0,1]
for n in range(0,20): 
    if n ==0:
        continue
    elif n == 1: 
        continue
    else: 
        k = fib[n-1] + fib[n-2]
        fib.append(k)
print("with for loop:\n",fib)

# with while loop 
fib_2 =[0,1]
x = 0 
while x<20:
    if x == 0:
        x+=1
    elif x == 1: 
        x+=1
    else: 
        l = fib_2[x-1] + fib_2[x-2]
        fib_2.append(l)        
    x+=1
print("with while loop:\n",fib_2)    

