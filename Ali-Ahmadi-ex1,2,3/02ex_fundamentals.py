#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `02ex_fundamentals.py`.
# 
# In case you need multiple files, name them `02ex_fundamentals_es01.py`, `02ex_fundamentals_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `02ex_fundamentals`. 
# 
# The exercises need to run without errors with `python3`.

# 1\. **Global variables**
# 
# Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list

# In[9]:


x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# In[10]:


#Answer

x = 5
def f(alist):
    for i in range(x):
         alist.append(i)
    return alist

alist = [1,2,3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed!

def f_2(alist,x_range):
    
    temp_list=alist.copy() #this will prevent it from changing
                        
    
    for i in range(x_range):
        temp_list.append(i)
    return temp_list

alist = [1,2,3]
ans = f_2(alist,5)
print(ans)
print(alist)


# 2. List comprehension
# 
# Write the following expression using a list comprehension:
# 
# ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))

# In[11]:


# First-Soloution
ans = []
for i in range(3): 
    for j in range(4):
        ans.append((i, j))
print(ans)


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[12]:


def filter_list(words, n):
    return list(filter(lambda word : len(word)<n, words))

print(filter_list(["goodbye", "bye","goodevening","ciao"],6))


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[13]:


def map_dict(dic):
    return list(map(lambda key : len(key), dic.keys()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(map_dict(lang))


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[14]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

#alternative solution:
language_scores2 = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores2.sort()
print(language_scores2)


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[15]:


def squared(i):
    return i**2

def cubed(i):
    return i**3

def power6(i):
    return squared(cubed(i))

print(power6(2))


# 7\. **Decorators**
# 
# Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.
# 
# The wrapped function should look like:
# 
# ```python
# @hello
# def square(x):
#     return x*x
# ```

# In[16]:


def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Hello")
    return wrapper

@hello
def square(x):
    print( x**2)
    
    
@hello
def do_sth(x,y,z):
    print(x*y*z)


do_sth(4,2,5)
print("----------")

square(5)


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[17]:


def recursiveFibonacci(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return recursiveFibonacci(i-1) + recursiveFibonacci(i-2)


for i in range(1,21):
    print(recursiveFibonacci(i))




def loopFibonacci(i):
    if i ==1:
        return 0
    elif i ==2:
        return 1
    else:
        a,b = 0,1
        for j in range(i-2):
            a,b = b, a+b
        return b

for i in range(1,21):
    print(loopFibonacci(i))


# 9\. **The Fibonacci sequence (part 3)**
# 
# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
# 
# Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
# 
# `%timeit loopFibonacci(20)`
# 
# `%timeit recursiveFibonacci(20)`
# 
# which one is the most efficient implementation? By how much?

# In[18]:


get_ipython().run_line_magic('timeit', 'loopFibonacci(20)')
get_ipython().run_line_magic('timeit', 'recursiveFibonacci(20)')


# 10\. **Class definition**
# 
# Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
# 
# - Create appropriate methods to get and set the length of each side
# 
# - Create a method `perimeter()` that returns the perimeter of the polygon
# 
# - Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
# 
# Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.

# In[19]:


class polygon:

    x = ()

    def __init__(self,components):
        if len(components) > 2:
            self.x = components
        else:
            print("Error: not enough number of sides given")
    def get_side(self,n):
        return self.x[n]

    def set_side(self,n, val):
        x_temp = list(self.x)
        if n < len(self.x):
            x_temp[n] = val
        self.x = tuple(x_temp)

    def perimeter(self):
        p = 0
        for side in self.x:
            p+=side
        return p

    def getOrderedSides(self, increasing = True):
        if increasing == True:
            return tuple(sorted(self.x))
        else:
            return tuple(sorted(self.x, reverse=True))
a = polygon((3,5,8))
#print(a.get_side(2))
#a.set_side(2,9)
#print(a.get_side(2))
#print(a.perimeter())
print(a.getOrderedSides(increasing = True))
#print(a.getOrderedSides(increasing = False))




class rectangle(polygon):
    def __init__(self, components):
        #Making sure the tuple contains four elements and that pairs/all sides are the same value (also including squares)
        if len(components) == 4 and len(set(components)) <=2:
            self.x = components
        else:
            print("Error: not following the geometrical properties of a rectangle")

    def area(self):
        sides = sorted(self.x)
        return sides[0]*sides[-1]


b = rectangle((2,5,2,5))
print(b.perimeter())
print(b.area())


# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[ ]:




