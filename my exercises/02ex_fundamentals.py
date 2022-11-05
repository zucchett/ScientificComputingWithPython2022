#!/usr/bin/env python
# coding: utf-8

# # Exercise 2: Fundamentals
# # Duy Tommy Tran
# 
# #### 1. Global variables

# In[1]:


def f(alist, x):
    newlist = alist.copy()  # Make a copy of the input list
    for i in range(x):
        newlist.append(i)   # Add more components to the copy
    return newlist          # The function returns the copy of the list with more components

alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist)


# #### 2. List comprehension

# In[2]:


ans = [x*x for x in range(10) if x%2==1]
print(ans)


# #### 3. Filter list

# In[3]:


def filter_list(l, n):
    return list(filter(lambda word: len(word) < n, words)) # 'word's shorter than n is put in an new list called 'words'

words = ['hi', 'where', 'is', 'the', 'gelato']

print(filter_list(words, 3))


# #### 4. Map dictionary

# In[4]:


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def len_keys(dic):
    return list(map(lambda key: len(key), dic))
    
print(len_keys(lang))


# #### 5. Lambda functions

# In[5]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda i: i[0])

print(language_scores)


# #### 6. Nested functions

# In[6]:


def square(x):
    return x**2

def cube(x):
    return x**3

def sixth(x):
    return square(cube(x))

print(sixth(2))


# #### 7. Decorators

# In[7]:


def hello(func):
    def wrapper(x):
        print('Hello World!')
        func(x)
    return wrapper

@hello
def square(x):
    return x*x

square(2)


# #### 8. The Fibonacci sequence (Part 2)

# In[8]:


def recursiveFibonacci(n):
    if n == 1:         # First element is always 0
        return 0
    elif n == 2:       # Second element is always 1
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

# The function only returns the last element, so they are put in a list with a for-loop
F = []
for i in range(1,21):
    F.append(recursiveFibonacci(i))
    
print(F)


# #### 9. The Fibonacci sequence (Part 3)

# In[9]:


def loopFibonacci(n):
    F = [0, 1]
    while len(F) < n:
        F.append(F[len(F)-1]+F[len(F)-2])
    return F

print(loopFibonacci(20))


# In[10]:


get_ipython().run_line_magic('timeit', 'loopFibonacci(20)')
get_ipython().run_line_magic('timeit', 'recursiveFibonacci(20)')


# The loop is more efficient as the running time is much shorter.
# 
# #### 10. Class definition

# In[11]:


class Polygon:
    # Definition of class attributes
    # l: class attribute, length
    l = ()
    
    # Definition of constructor
    def __init__(self, components):
        self.l = components
    
    # Definition of methods
    def getLength(self, i):
        return self.l[i]
    
    def setLength(self, i, li):
        lNew = list(self.l)
        lNew[n] = li
        self.l = tuple(lNew)
    
    def perimeter(self):
        perimeter = 0
        for i in self.l:
            perimeter += i
        return perimeter
    
    def getOrderedSides(self, increasing=True):
        s1 = list(self.l)
        s1.sort(reverse = not increasing)
        s2=tuple(s1)
        return s2


# In[12]:


poly = Polygon((6,5,4,3,2))
perimeter = poly.perimeter()
s1 = poly.getOrderedSides(increasing=True)
s2 = poly.getOrderedSides(increasing=False)

print(perimeter)
print(s1)
print(s2)


# #### 11. Class inheritance

# In[13]:


class Rectangle(Polygon):
    
    # Definition of constructor
    def __init__(self, components):
        if (len(components)==4 and len(set(components))==2):
            self.l = components
        else:
            print("Error: number of components is not 4")
    
    # Definition of methods
    def area(self):
        return list(set(self.l))[0]*list(set(self.l))[1]


# In[14]:


rectangle = Rectangle((4,4,2,2))
perimeter = rectangle.perimeter()
area = rectangle.area()

print(perimeter)
print(area)

