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

# In[2]:


x = 5

def f(alist):
    x = 7
    alist = [4, 5, 6]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`
# 

# In[8]:


print([x**2 for x in range (0,10) if x%2 == 1])


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[105]:


v = int(input('Enter the acceptable length of words in the list = '))
def wordlimit(x):
    v_list = []
    if len(x)<v:
        v_list.append(a_list[i])
    else:
        pass
    return v_list

b_list = ['happy', 'beautiful', 'love', 'buff', 'fun', 'oh', 'wow', 'banana', 'freeing']
print(list(filter(wordlimit, b_list)))


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[30]:


def length(x):
    return len(x)
    
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7} 
print(list(map(length, lang.keys())))


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[17]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = (lambda x : x[0])) 

print(language_scores)


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[44]:


def square(x):
    return x**2

def cube(x):
    return square(x)*x

def sixthPwr(x):
    return cube(x)*cube(x)
a = int(input('input a number to obtain its square, cube and sixth power'))
print(square(a))
print(cube(a))
print(sixthPwr(a))


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

# In[20]:


def a(f): 
    def b():
        print(f'{f} is printed here')
        f()
    return b

@a
def hello():
    print('Hello World!')

hello()


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[10]:


def recursiveFibonacci(n):  
    if n <= 1:  
        return n  
    else:  
        return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))  

for i in range(20):  
    print(recursiveFibonacci(i)) 


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

# In[ ]:





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

# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.
