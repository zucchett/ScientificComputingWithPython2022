#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''1. Global Variables
Convert the function  into a function that 
doesn't use global variables and that does not modify the original list
'''

print("Default function:")
x = 5
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

print('Converted function:')
y = 5
def fnew(alistnew):
    alistnew = [1, 2, 3]
    for i in range(y):
        alistnew.append(i)
    return alistnew

alistnew = [1, 2, 3]
ansnew = fnew(alistnew)
print(ansnew)
print(alistnew) #alistnew has not been changed


# In[ ]:


'''2. List comprehension
Write the following expression using a list comprehension:
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))
'''

ans = [i * i for i in range(10) if i % 2 == 1]
print("List of squares of odd numbers from 0 to 9:")
print(ans) 


# In[ ]:


'''3. Filter list

Using the filter() hof, define a function that takes a list 
of words and an integer n as arguments, and returns a list of words that are shorter than n.'''

n = int(input('set n: '))
listwords = input('set list of words: ')
print(list(filter(lambda x: len(x) < n, listwords.split())))


# In[ ]:


'''4. Map dictionary

Consider the following dictionary:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

Write a function that takes the above dictionary and uses the map() 
higher order function to return a list that contains the length of the keys of the dictionary.'''

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(lang.keys())
langkeyslen = []
for i in map(lambda x: len(x), list(lang.keys())):
    langkeyslen.append(i)
print(langkeyslen)


# In[ ]:


'''5. Lambda functions

Write a Python program that sorts the following list of tuples using a lambda function, 
according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

Hint: use the method sort() and its argument key of the list data structure.'''

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
sorted(language_scores, key=lambda x: x[0]) 
#if we need to rewrite our list, use this one:
#language_scores = sorted(language_scores, key=lambda x: x[0]) 
#print(language_scores)


# In[ ]:


'''6. Nested functions

Write two functions: one that returns the square of a number, and one that returns its cube.

Then, write a third function that returns the number raised to the 6th power, 
using only the two previous functions.'''
def square(x):
    x = x**2
    return x
def cube(x):
    x = x**3
    return x
def six(x):
    x = square(cube(x))
    return x

x = float(input('set x: '))
print(six(x))


# In[ ]:


'''7. Decorators

Write a decorator named hello that makes every wrapped 
function print “Hello World!” each time the function is called.

The wrapped function should look like:

@hello
def square(x):
    return x*x'''
      
def hello(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        print('Hello World!')
        return return_value
    return wrapper

@hello
def square(x):
    return(x*x)

square(5)


# In[ ]:


'''8. The Fibonacci sequence (part 2)

Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.'''

def fibonaccirec(n):
    if (n <= 1):
        return n
    else:
        return(fibonaccirec(n - 1) + fibonaccirec(n - 2))
    
fib_range=[]
for i in range(1,21):
    fib_range.append((fibonaccirec(i)))
print(fib_range)
print('Other option:')
print([fibonaccirec(i) for i in range(1,21)])


# In[ ]:


'''9. The Fibonacci sequence (part 3)

Run both the Fibonacci recursive function from the previous exercise, 
and the Fibonacci function from 01ex that use only for and while loops.
Measure the execution code of the two functions with timeit (link to the doc), for example:
%timeit loopFibonacci(20)
%timeit recursiveFibonacci(20)
which one is the most efficient implementation? By how much?'''

def fibonacciloop(n): #define function from 01ex
    fib_range=[]
    for i in range(n):
        if i <= 1:
            fib_range.append(1)
        else:
            fib_range.append(fib_range[i - 2] + fib_range[i - 1])
    print(fib_range)


# In[ ]:


import timeit
if __name__ == '__main__':
    resloop = timeit.timeit("fibonacciloop(20)", setup="from __main__ import fibonacciloop",number=1)
    print('for loop function     : ', resloop)
    resrec = timeit.timeit("print([fibonaccirec(i) for i in range(1,21)])", setup="from __main__ import fibonaccirec",number=1)
    print('for recursive function: ', resrec)
print('\nloop function is faster than recursive function by ', resrec/resloop, ' times')


# In[ ]:


'''10. Class definition

Define a class polygon. The constructor has to take a tuple as 
input that contains the length of each side. The (unordered) input list does not have 
to have a fixed length, but should contain at least 3 items.

Create appropriate methods to get and set the length of each side

Create a method perimeter() that returns the perimeter of the polygon

Create a method getOrderedSides(increasing = True) that returns a tuple containing 
the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

Test the class by creating an instance and calling the perimeter() 
and getOrderedSides(increasing = True) methods.'''

# Class definition
import math

class Polygon:
    
    # Definition of the class attributes, which are common for all instances of the same class
    x = ()
    
    # Definition of the Constructor, a special method that is called every time a new object is created
    # The first argument of the constructor (and also for all other methods in the class) is the instance itself
    def __init__(self, components):
        self.x = components # a tuple is expected as input
       
    # Definition of the methods
     
    def perimeter(self):
        p = 0
        for i in range(len(self.x)):
            p += self.x[i]
        print(p)
    
    
    
    def getOrderedSides(self, value):
        self.x = list(self.x)
        if value == True:
            self.x.sort()
            print(self.x)
        else:
            self.x.sort(reverse = True)
            print(self.x)


# In[ ]:


a = Polygon((3,1,5,1))


# In[ ]:


a.perimeter()
a.getOrderedSides(False)


# In[ ]:


'''11. Class inheritance

Define a class rectangle that inherits from polygon. Modify the constructor, 
if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor.'''

class Rectangle(Polygon): # class 'Rectangle' inherits from class 'Polygon'
    
    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(self, components):
        if len(components) == 2:
            self.x = components + components #do an addition to be possible use other methods (such as perimeter) for rectangle
        else:
            print("Please, set only 2 components: length and wight")
    
    # New methods that only belong to the child class
    def area(self):
        area = (self.x[0] * self.x[1])
        print(area)
        return area


# In[ ]:


a = Rectangle((2,4))
a.area()
a.perimeter()

