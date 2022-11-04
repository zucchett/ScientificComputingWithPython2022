#!/usr/bin/env python
# coding: utf-8

# # Exercises 1

# ### Tone Alsvik Finstad

# ### 1. The HelloWorld replacement

# In[1]:


#a)
for i in range(1,101):
    if i%3==0 or i%5==0:
        print("Hello"*(i%3==0)+"World"*(i%5==0))
    else:
        print(i)


# In[2]:


#b)
a=[]
for i in range(1,101):
    if i%3==0 or i%5==0:
        a.append("Hello"*(i%3==0)+"World"*(i%5==0))   #Use booleans to avoid to many if-statements
    else:
        a.append(i)
a_tuple=tuple(a)


print(f"Resulting tuple:\n {a_tuple}")

for i in range(len(a)):
    if str(a[i]).isalpha()==True:
        a[i]="Python"*("Hello" in a[i])+"Works"*("World" in a[i]) 
new_a_tuple=tuple(a)


print(f"Substituted tuple: \n{new_a_tuple}")


# ### 2. The swap

# In[3]:


x=input("x: ")
y=input("y: ")
x,y=y,x              #Swapping without a temporary variable
print(f"x={x}")
print(f"y={y}")


# ### 3. Computing the distance

# In[4]:


import math as m


# In[5]:


u=(int(input("U_x:")),int(input("U_y:")))
v=(int(input("V_x:")),int(input("V_y:")))

def euc_dist(u,v):
    d=m.sqrt((v[0]-u[0])**2+(v[1]-u[1])**2)
    print(f"Euclidean distance: {d}")
    
euc_dist(u,v)


# ### 4. Counting letters

# In[6]:


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def count_letters(string_name):
    print(f"Counting letters in: {string_name}")
    for i in range(97, 123):
        print(f"{chr(i)}:{string_name.lower().count(chr(i))}")
        
count_letters(s1)


# ### 5. Isolating the unique

# In[7]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l_unique=[]
for elem in l:
    if elem not in l_unique:
        l_unique.append(elem)
    
print(f"Unique numbers: {l_unique}")
print(f"Number of unique numbers: {len(l_unique)}")


# Exploiting only the Python data structures:

# In[8]:


print(f"Unique numbers: {set(l)}")
print(f"Number of unique numbers: {len(set(l))}")


# ### 6. Casting

# In[9]:


var_a=input("Variable 1:")
var_b=input("Variable 2:")
try:
    if var_a.isalpha() and var_b.isalpha():
        var_c=var_a+var_b
    else:
        var_c=float(var_a)+float(var_b)
    print(f"{var_a} + {var_b} = {var_c}")
except:
    print("The addition is not possible")
    


# ### 7. Cubes

# In[10]:


x_list=[]
for i in range(0,11):
    x_list.append(i)
    
x_list_2=[x for x in range(0,11)]

print(x_list)
print(x_list_2)


# ### 8. List comprehension
# 

# In[11]:


a=[(x,y) for x in range(3) for y in range(4)]
print(a)


# ### 9. Nested list comprehension

# In[18]:


a=[(a,b,int(m.sqrt(a**2+b**2))) for a in range(1,100) for b in range(1,100) if m.sqrt(a**2+b**2)<100 and m.sqrt(a**2+b**2)%1==0]
print(tuple(a))


# ### 10. Normalization of a N-dimensional vector

# In[19]:


def normalization(vec):
    c=0
    temp_list=[]
    for elem in vec:
        c+=elem**2
    for elem in vec:
        temp_list.append(elem/m.sqrt(c))
    return tuple(temp_list)
v=(1,3,5,6,8)
print(normalization(v))


# ### 11. The Fibonacci sequence

# In[22]:


fib_seq=[0,1]
while len(fib_seq)<20:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
print(fib_seq)

