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

# In[8]:


x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# In[9]:


x = 5
alist_temp =[]

def f(alist):
    alist_temp = alist
    for i in range(x):
         alist_temp.append(i)
    return alist_temp

alist = [1,2,3]
ans = f(alist)

print(ans)
print(alist) 


# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`

# In[10]:


ans = [x*x  for x in range(10) if x % 2 == 1]
print(ans)


# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# In[11]:


def filterlongword(string,number):
    listfinal = []
    for i in range(len(string)):
        if len(string[i]) > number:
            listfinal.append(string[i])
    print("The list of words greater than the integer is",listfinal)
    return listfinal
    

def main():
    listwords=[]
    number_of_times =int(input("Please enter how many words in the list: "))
    
    for i in range(0,number_of_times):
        words = input("Please enter a word: ")
        listwords.append(words)
        
    integer = eval(input("Please input an integer: "))
    filterlongword(listwords,integer)

    
main()  


# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# In[12]:


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def length_keys(language):
    length_keys = list(map(lambda x: len(x), language))
    return length_keys

print("Length of the keys of the dictionary:", length_keys(lang))


# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# In[13]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print("Original list of tuples: ")
print(language_scores)
language_scores.sort(key = lambda x: x[0])
print("\nSorting the list of tuples: ")
print(language_scores)


# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# In[14]:


n = int(input("Enter a number: "))


def square():
    return n**2
def cube():
    return n**3
def power_6():
    return square() * cube()
    
print("Square of", n, "is", square())
print("Cube of", n, "is", cube())
print("6th power of", n, "is", power_6())


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

# In[15]:


def my_decorator(f): 
    def log_f_as_called():
        print(f'{f} was called.')
        f()
    return log_f_as_called

@my_decorator
def hello():
    print('Hello World!')
    
hello()


# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# In[16]:


def recur_f(n):
   if n <= 1:
       return n
   else:
       return(recur_f(n-1) + recur_f(n-2))

nterms = 20


print("First 20 numbers of the Fibonacci sequence:")
for i in range(nterms):
    print(recur_f(i))


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

# In[17]:


import timeit

fib = 20
n = 0
n1 = 0
n2 = 1
count = 0
while (count<fib):
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    count +=1

get_ipython().run_line_magic('timeit', 'n')

print()
    
    
def recur_f(n):
   if n <= 1:
       return n
   else:
       return(recur_f(n-1) + recur_f(n-2))

nterms = 20


print("First 20 numbers of the Fibonacci sequence:")
for i in range(nterms):
    print(recur_f(i))
    

get_ipython().run_line_magic('timeit', 'recur_f(i)')
#The most efficient implementation for Fibonacci function is using only for and while loops. It took 33.1 ns with for loop and 1.99 ms with recursive function. The difference is 1989966.9 ns


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

# In[20]:


class polygon:
    def __init__(self, shape):
        self.shape = shape
         
    def perimeter(self):
        return sum(self.shape)
    
    def getOrderedSides(self, increasing=True):
        self.sorted = tuple(sorted(self.shape, reverse=not increasing))
        return self.sorted


triangle = polygon((10, 12, 14, 16))                     
print(triangle.getOrderedSides())                    
print(triangle.getOrderedSides(increasing=True))     
print(triangle.getOrderedSides(increasing=False))    
    


# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[19]:


class rectangle(polygon):
    def __init__(self, shape):
        super().__init__(shape)
    
    def area(self):
        area = self.getOrderedSides()  
        return area[0] * area[2]       

rectangle = rectangle((10,12,10,12))                    
print(rectangle.perimeter())                        
print(rectangle.getOrderedSides(increasing=False))  
print(rectangle.area())                            

