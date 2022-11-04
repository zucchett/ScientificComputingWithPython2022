#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Introduction
# # Duy Tommy Tran
# 
# #### Importing library

# In[1]:


from math import sqrt


# #### 1. The HelloWorld replacement
# #### 1.a)

# In[2]:


num = list(range(1,101))              # Making a list with numbers from 1 to 100

for i in range(len(num)):
    if (i+1) % 3 == 0:                # Replace multiples of 3 with 'Hello'
        num[i] = 'Hello'
    if (i+1) % 5 == 0:                # Replace multiples of 5 with 'World' 
        num[i] = "World"
    if (i+1) % 3 == 0 and i % 5 == 0: # Replace multiples of 3 and 5 with 'HelloWorld'
        num[i] = 'HelloWorld'

Hello_world = tuple(num)              # Put the result in a tuple

print(Hello_world)


# #### 1.b)

# In[3]:


for i in range(len(num)):
    if num[i] == 'Hello':             # Replace every 'Hello' with 'Python'
        num[i] = 'Python'
    if num[i] == 'World':             # Replace every 'World' with 'Works'
        num[i] = 'Works'

print(num)


# #### 2. The swap

# In[4]:


def swap(x,y):
    x, y = y, x                       # Define x as y and define y as x
    return x, y

x = input('Insert x: ')
y = input('Insert y: ')
x, y = swap(x, y)
print(f'x is now {x}, and y is now {y}')


# #### 3. Computing the distance

# In[5]:


def distance(u, v):
    # The function calculates the euclidean distance between two points u and v in a 2D space
    return sqrt((u[0]+v[0])**2 + (u[1]+v[1])**2)

u = (3,0)
v = (0,4)

print(distance(u,v))


# #### 4. Counting letters

# In[6]:


def count(string):
    # The function calculates the amount of times each letter occurs in a given string
    chars_dict = {}                      # Creating an empty dictionary
    
    for s in string:
        if s in chars_dict:              # The amount is +1 when the letter is in the dictionary
            chars_dict[s.lower()] += 1
        else:
            chars_dict[s.lower()] = 1    # Set the amount to 1 when the letter is new to the dictionary
    
    sort = sorted(chars_dict.items())    # Sort the dictionary
    
    for i in range(len(chars_dict)):
        print(sort[i])


# In[7]:


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
print(count(s1))


# In[8]:


s2 = "The quick brown fox jumps over the lazy dog"
print(count(s2))


# #### 5. Isolating the unique

# In[9]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# In[10]:


# Method 1: Appending to an empty with in a loop
unique_1 = []

for i in range(len(l)):
    if l[i] not in unique_1:
        unique_1.append(l[i])
        
print(f'The unique numbers are: {sorted(unique_1)} \n')
print(f'There are {len(unique_1)} unique numbers')


# In[11]:


# Method 2: Exploiting Python data structures with set
unique_2 = set(l)

print(f'The unique numbers are: {unique_2} \n')
print(f'There are {len(unique_2)} unique numbers')


# #### 6. Casting

# In[12]:


x = input('x = ')
y = input('y = ')

try:                                  # Try to add the variables as int
    x = int(x)
    y = int(y)
    
    print(f'{x} + {y} = {x+y}')
except:
    try:                              # Try to add the variables as float
        x = float(x)
        y = float(y)
        
        print(f'{x} + {y} = {x+y}')
    except:
        try:                          # Try to add the variables as str
            print(f'{x} + {y} = {x+y}')
        except:
            print('They cannot be added.')


# #### 7. Cubes
# #### 7. a)

# In[13]:


x = list(range(0,11))      # List with numbers from [0, 10]

cube = []

for i in x:
    cube.append(i**3)      # Cube each element and append it to a new list

print(cube)


# #### 7. b)

# In[14]:


x = list(range(0,11))

cube = [i**3 for i in x]   # Perform the same using list comprehension
print(cube)


# #### 8. List comprehension

# In[15]:


a = [(i,j) for i in range(3) for j in range(4)]
print(a)


# #### 9. Nested list comprehension

# In[16]:


# Checks every possible combination of pythagoras for a and b values from 1 to 100
# The last condition makes sure to only keep the combinations where c is an integer

pythagorean = [(a, b, int(sqrt(a**2+b**2))) for a in range(1,100) for b in range(1,100) if sqrt(a**2+b**2)<100 and sqrt(a**2+b**2)%1 == 0]
print(tuple(pythagorean))


# #### 10. Normalization of a N-dimensional vector

# In[17]:


def normalization(v):
    squared = [i**2 for i in v]    # Square each element in the vector
    length = sqrt(sum(squared))    # Find the length of the vector
    
    return [i/length for i in v]   # Returns a new vector where each element is divided by the length


# In[18]:


v = [1, 3, 5, 6, 8]
print(normalization(v))

# Checks that the integral equals to 1 to ensure the normalization is done correctly
s = 0
for i in range(len(v)):
    s+=normalization(v)[i]**2
print(s)


# #### 11. The Fibonacci sequence

# In[19]:


F = [0, 1]                          # The first to elements of the sequence is 0 and 1

while len(F) <= 20:
    F.append(F[len(F)-1]+F[len(F)-2])

print(F)

