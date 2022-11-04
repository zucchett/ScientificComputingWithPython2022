#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" Convert the function  𝑓
  into a function that doesn't use global variables and that does not modify the original list
"""

x = 5
print ('Default function')
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)

y=5
print ('new function')
def newF(alist2):
    alist2=[1,2,3]
    for i in range(y):
        alist2.append(i)
    return alist2
alist2 = [1, 2, 3]
ans2 = newF(alist2)
print(ans2)
print(alist2) #A list has not been change


# In[ ]:


'''
Write the following expression using a list comprehension:
'''
ans = [i*i for i in range(10) if i%2 == 1]
print(ans)


# In[ ]:


#3. Filter list
'''Using the filter() hof, define a function that takes a list of words and an integer 
n as arguments, and returns a list of words that are shorter than n'''
n=4
words=['ghbdtn', 'ghbdt', 'ghbd', 'ghb', 'gh', 'g']

print(list(filter(lambda i: len(i)<n,words)))


# In[ ]:


#4. Map dictionary
"""Consider the following dictionary:
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
Write a function that takes the above dictionary and uses the map() higher order function 
to return a list that contains the length of the keys of the dictionary."""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print (lang)
b = list(map(len, lang))
print (b)


# In[ ]:


#5. Lambda functions
'''Write a Python program that sorts the following list of tuples using a lambda function, 
according to the alphabetical order of the first element of the tuple:
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
Hint: use the method sort() and its argument key of the list data structure.'''

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda x : x[0])
print(language_scores)


# In[ ]:


#6. Nested functions
'''Write two functions: one that returns the square of a number, and one that returns its cube.
Then, write a third function that returns the number raised to the 6th power, using only the two
previous functions.'''
def square(x):
    x **= 2
    return x

def cube(x):
    x **= 3
    return x

y = 2 
cube(y)

def six(x):
    return square(cube(x))
print(six(2))


# In[ ]:


#7. Decorators
'''Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function 
is called. The wrapped function should look like:
@hello
def square(x):
    return x*x'''

def hello(func):
    
    def wrap():
        func()
        print ("Hello World")
    return wrap

@hello
def square(x):
    return x*x
    


# In[ ]:


#8. The Fibonacci sequence (part 2)
#Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

amount = 20
for i in range(amount):
    print(fibo(i))


# In[ ]:


#9. The Fibonacci sequence (part 3)
'''Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function
from 01ex that use only for and while loops.
Measure the execution code of the two functions with timeit, for example:
%timeit loopFibonacci(20)
%timeit recursiveFibonacci(20)
which one is the most efficient implementation? By how much?'''
import timeit

test_code = '''
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

amount = 20
for i in range(amount):
    print(fibo(i))'''
a=timeit.timeit(stmt = test_code, setup='pass', number = 1)
print(a)

test_code2 = '''
def PrintFibonacci(length):
    first = 0
    second = 1
    print(first, second, end=" ")
    length -= 2
    while length > 0:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        length -= 1
if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(20)
    pass'''
b=timeit.timeit(stmt = test_code2, setup='pass', number = 1)
print(b)
print(a-b)


# In[ ]:


#10. Class definition
'''Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. 
The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
Create appropriate methods to get and set the length of each side
Create a method perimeter() that returns the perimeter of the polygon
Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides 
arranged in increasing or decreasing order, depending on the argument of the method
Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.'''

import math

class Polygon:
    x = ()
    def __init__(self, components):
        self.x = components # a tuple as input       
   
  # Definition of the methods 
    def perimeter(self):
        p = 0
        for i in range(len(self.x)):
            p += self.x[i]
        print('per = ',p)

    def getOrderedSides(self, value):
        self.x = list(self.x)
        if value == True:
            self.x.sort()
            print(self.x)
        else:
            self.x.sort(reverse = True)
            print(self.x) 
            


# In[ ]:


a = Polygon((2, 4, 5, 3))
a.perimeter()
a.getOrderedSides(False)


# In[ ]:


#11. Class inheritance
'''Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, 
to make sure that the input data is consistent with the geometrical properties of a rectangle.
-Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor.'''

class Rectangle(Polygon):
    
    def __init__(self, components):
        if len(components) == 2:
            print ("The area is")
        else:
            print("Please, set only 2 components")
    
    # New methods that only belong to the child class
    def area(self):
        area = (self.x[0] * self.x[1])
        print(area)
        return area


# In[ ]:


b = Rectangle((5, 7))
b.area()


# In[ ]:





# In[ ]:




