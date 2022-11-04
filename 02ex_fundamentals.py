"""1. Global variables

Convert the function  𝑓  into a function that doesn't use global variables and that does not modify the original list
x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)

print(alist) # alist has been changed"""

def f(alist,x):
    changed_list=list(alist)
    for i in range(x):
        changed_list.append(i)
    return changed_list

alist = [1, 2, 3]
ans = f(alist,8)
print(ans)
print(alist) # alist has been changed

"""2. List comprehension

Write the following expression using a list comprehension: ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))"""

print ([pow(x,2) for x in range(1,10,2)])

"""3. Filter list

Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n."""

l_of_words=["a","aa","aaa","b","bb","bbb","bbbb","bbbbb","cc","cccccccc","ccc","ccccccccc","cc","dddd"]
i =int(input())
def func(x):
    return len(list(x))<=i
print(list(filter(func, l_of_words)))
   
"""4. Map dictionary

Consider the following dictionary:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

Write a function that takes the above dictionary and uses the map() higher order function to return a list that contains the length of the keys of the dictionary."""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def fu(x):
    return [i for i in map(lambda y: len(y), list(x.keys()))]
print(fu(lang))

"""5. Lambda functions

Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

Hint: use the method sort() and its argument key of the list data structure."""

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x:x[0])
print(language_scores)

"""6. Nested functions

Write two functions: one that returns the square of a number, and one that returns its cube.

Then, write a third function that returns the number raised to the 6th power, using only the two previous functions."""

def square(x):
    return pow(x,2)
def cube(x):
    return pow(x,3)
def combined(x):
    return square(cube(x))
print(combined(int(input())))

"""7. Decorators

Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.

The wrapped function should look like:

@hello
def square(x):
    return x*x"""

x=3
def hello(func):
    def hello2():
        print("Hello World!")
        func()
    return hello2
@hello
def hey():
    print("hey!")

hey()

"""8. The Fibonacci sequence (part 2)

Calculate the first 20 numbers of the Fibonacci sequence using a recursive function."""

import timeit
f1,f2,fs = 0,1,0
f_list = []
def fibonacci(x):
    global f1,f2,fs,f_list
    if x>0:
        f_list.append(f1)
        fs = f1 + f2
        f1 = f2
        f2 = fs
        return fibonacci(x-1)
x = 20
fibonacci(x)
print(f_list)

"""9. The Fibonacci sequence (part 3)

Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.

Measure the execution code of the two functions with timeit (link to the doc), for example:

%timeit loopFibonacci(20)

%timeit recursiveFibonacci(20)

which one is the most efficient implementation? By how much?"""

import timeit
f1,f2,fs = 0,1,0
f_list = []
def fibonacci(x):
    global f1,f2,fs,f_list
    if x>0:
        f_list.append(f1)
        fs = f1 + f2
        f1 = f2
        f2 = fs
        return fibonacci(x-1)
x = 20
fibonacci(x)
print(f_list)
print("\t\t recursive timeit =")
recursive_time = timeit.timeit(stmt='[fibonacci(i) for i in range(20)]', setup="from __main__ import fibonacci", number=1)
print(recursive_time)

def fibonacciloop():
    counter = 0
    fibonacci=[]
    f1 , f2 = 0,1

    for i in range(0,20):
        fibonacci.append(f1)
        counter = f1 + f2
        f1 = f2
        f2 = counter
    return fibonacci
print("\t\t Loop timeit =")
loop_time =timeit.timeit(stmt='fibonacciloop()', setup="from __main__ import fibonacciloop", number=1)
print(loop_time)

if loop_time > recursive_time:
    
    print("loop is ", loop_time-recursive_time, "faster")
else:
    print("recursive is", recursive_time-loop_time,"faster")

"""10. Class definition

Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

Create appropriate methods to get and set the length of each side

Create a method perimeter() that returns the perimeter of the polygon

Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods."""

import math
class polygon:
    list_sides=[]
    def __init__(self,list_sides):
        self.list_sides = list_sides
    def perimeter(self):
        return [sum(self.list_sides)]
    def getOrderedSides(self,increasing = True):
        sorted = list(self.list_sides)
        if increasing == True:
            sorted.sort()
            return tuple(sorted)
        else:
            sorted.sort(reverse=True)
            return tuple(sorted)
tuple1 = tuple([1,1,4,4])
tuple2 = tuple([5,4,6])
a = polygon(tuple1)
b = polygon(tuple2)
print(a.perimeter())
print(b.getOrderedSides(increasing = True))

"""11. Class inheritance

Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor."""

import math
import math
class polygon:
    list_sides=[]
    def __init__(self,list_sides):
        self.list_sides = list_sides
    def perimeter(self):
        return [sum(self.list_sides)]
    def getOrderedSides(self,increasing = True):
        sorted = list(self.list_sides)
        if increasing == True:
            sorted.sort()
            return tuple(sorted)
        else:
            sorted.sort(reverse=True)
            return tuple(sorted)
class rectangle(polygon):
    def __init__(self,list_sidesR):
        if len(list_sidesR)==4 and len(set(list_sidesR)) == 2:
            print("this is a rectangle")
            self.list_sides= list_sidesR
        else:
            print("this is not rectangle")
    def area(self):
        s = list(set(self.list_sides))
        return (s[0]*s[1])

tuple1 = tuple([1,1,4,4])
tuple2 = tuple([5,4,6])
c = rectangle(tuple2)
d = c.area()
print(d)


