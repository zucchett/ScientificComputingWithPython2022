#!/usr/bin/env python
# coding: utf-8

# ## Exercise 2 - hannafalch_nastby
# 

# ### 1. Global variables
# Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list

# In[ ]:


def f(alist, x):
    newList = alist.copy()
    for i in range(x):
        newList.append(i)
    return newList

alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist)


# ### 2. List comprehension
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`

# In[ ]:


ans2 = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans2)

newAns2 = [x**2 for x in range(10) if x % 2 == 1]
print(newAns2)


# ### 3. Filter list
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[ ]:


def filterList(words, n):
    newList = []
    for word in words:
        if len(word) < n:
            newList.append(word)
    return newList

wordList = ["hei", "jee", "python", "no", "yehaw"]
filterList(wordList, 3)


# ### 4. Map dictionary
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[ ]:


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def mapDict(dic):
    return list(map(lambda x: len(x), dic))
    
mapDict(lang)


# ### 5. Lambda functions
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[ ]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda item: item[0])

print(language_scores)


# ### 6. Nested functions
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[ ]:


def squareFunc(n):
    return n**2

def cubeFunc(n):
    return n**3

def nestedFunc(n):
    return cubeFunc(squareFunc(n))


print(f"2 raised to the 6th power is : {nestedFunc(2)}")


# ### 7. Decorators
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

# In[ ]:


def hello(func):
    def wrapper():
        func(4)
        print("Hello World!")
    return wrapper

@hello
def square(x):
    return x*x


# ### 8. The Fibonacci sequence
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[1]:


def fibRec(n):
    if n <= 1:
        return n
    return fibRec(n-1) + fibRec(n-2)

fibList = [fibRec(n) for n in range(20)]
print(fibList)


# In[5]:


def fib(n):
    fibList = [0, 1]
    F_0 = 0
    F_1 = 1
    for i in range(n-2):
        F = F_1 + F_0
        fibList.append(F)
        F_0 = F_1
        F_1 = F
        i += 1
    return fibList
print(fib(20))


# ### 9. The Fibonacci sequence
# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
# 
# Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
# 
# `%timeit loopFibonacci(20)`
# 
# `%timeit recursiveFibonacci(20)`
# 
# which one is the most efficient implementation? By how much?

# In[4]:


import timeit
get_ipython().run_line_magic('timeit', 'timeFib = fib(20)')
get_ipython().run_line_magic('timeit', 'timeRec = [fibRec(n) for n in range(20)]')


# ### 10. Class definition
# Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
# 
# - Create appropriate methods to get and set the length of each side
# 
# - Create a method `perimeter()` that returns the perimeter of the polygon
# 
# - Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
# 
# Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.

# In[3]:


class polygon:
    
    lengths = ()
    
    def __init__(self, components):
        self.lengths = components
    
    
    def getA(self, n):
        return self.lengths[n]
    
    def setA(self, n, val):
        if n < len(self.lengths):
            self.lengths[n] = val
            
    def perimeter(self):
        return sum(self.lengths)
        
    def getOrderedSides(self, increasing = True):
        if increasing == False:
            return tuple(sorted(self.lengths))
        return tuple(sorted(self.lengths, reverse = False))
    
    


# In[22]:


p = polygon([3, 5, 2, 6])
print("Perimeter: ", p.perimeter())
print("Ordered sides: ", p.getOrderedSides())


# ### 11. Class inheritance
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[13]:


class rectangle(polygon):
    def __init__(self, components):
        if len(components) == 4 and len(set(components)) == 2:
            if components[0] == components[1] and components[2] == components[3]:
                self.lengths = components
            elif components[0] == components[2] and components[1] == components[3]:
                self.lengths = components
            elif components[0] == components[3] and components[1] == components[2]:
                self.lengths = components
        else:
            print("This is not a rectangle")
            return
            
            
    def area(self):
        if self.lengths[0] == self.lengths[1]:
            return self.lengths[0] * self.lengths[2]
        elif self.lengths[0] == self.lengths[2]:
            return self.lengths[0] * self.lengths[1]
        elif self.lengths[0] == self.lengths[3]:
            return self.lengths[0] * self.lengths[2]
        else:
            print("not possible")


# In[15]:


a = rectangle([3,2,2,3])
print(a.area())


# In[ ]:




