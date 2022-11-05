#!/usr/bin/env python
# coding: utf-8

# 1) a)

# In[5]:


n=1
while n<101:
    if n % 3 == 0 and n % 5 == 0:
        print("HelloWorld")
    elif n % 3 == 0:
        print("Hello")
    elif n % 5 == 0:
        print("World")
    else:
        print(n)
    n= n+1
        
        


# 1) b)

# In[1]:


rep=[]
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("HelloWorld")
        rep.append("HelloWorld")
    elif n % 3 == 0:
        print("Hello")
        rep.append("HelloWorld")
    elif n % 5 == 0:
        print("World")
        rep.append("HelloWorld")
    else:
        print(n)
        rep.append(n)

for n in range(len(rep)):
    if rep[n]=="Hello":
        rep[n]="Python"
    elif rep[n]=="World":
        rep[n]="Works"

tupl = (tuple(rep))
print(tupl)


# 2)

# In[6]:


x = input("x: ")
y = input("y: ")  
   
# To Swap the values of two variables  
x, y = y, x  
   
print ("x: ", x)  
print ("y: ", y)  


# 3)

# In[8]:


import math
V = (int(input("Xv: ")),int(input("Yv: ")))
U = (int(input("Xu: ")),int(input("Yu: ")))
a=V[0]-U[0]
b=V[1]-U[1]
c=(a**2)+(b**2)
d=int(math.sqrt(c))
print(d)


# 4)

# In[1]:



s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
x = list(s1.lower())

print(sorted([[i, x.count(i)] for i in set(x)]))

s2 = "The quick brown fox jumps over the lazy dog"

y = list(s2.lower())

print(sorted([[i, y.count(i)] for i in set(y)]))


# 5)

# In[3]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

print(sorted([[i, l.count(i)] for i in set(l)]))


# 6)

# In[3]:


V1 = input("V1:") 
V2 = input("V2:")
print(type(V1), type(V2))
try:
    V1 = float(V1)
    V2 = float(V2)
    if (V1+V2)%1==0:
        print(int(V1+V2))
    else: print(V1+V2)
except:
    V1 = str(V1)
    V2 = str(V2)
    print("Addition is not possible")


# 7)

# In[5]:


#A
cubesFor = []
for i in range (11):
    
    cubesFor.append(i**3)
print(cubesFor)


# In[ ]:


#B
cubesComp = [x**3 for x in range(11)]
print(cubesComp)


# 8)

# In[ ]:


a=[ (i,j) for i in range(3) for j in range (4)]
print(a)


# 9)

# In[ ]:


triples = []

for a in range(1, 100):
    for b in range(a, 100):
        for c in range(b, 100):
            if (pow(a,2)+pow(b,2)) == (pow(c,2)):
                triples.append((a,b,c))
triples = tuple(triples)
print(triples)


# 10)

# In[ ]:


V = input('Enter the vector: ').split()
su = sum([int(x) for x in V])
norm = [int(x)/su for x in V]
print(norm)
print('Normalized sum: ', sum(norm))


# 11)

# In[ ]:


FS = [0,1]
n=1
for x in range(18):
    FS.append(FS[x]+FS[x+1])
    
print(FS)


# In[ ]:




