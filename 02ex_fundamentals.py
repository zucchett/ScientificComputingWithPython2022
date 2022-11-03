import timeit
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:29:18 2022

@author: daria
"""

#Global variables
print("--- GLOBAL VARIABLES ---")

x = 5
def f(alist):
    newlist = alist.copy()
    for i in range(x):
        newlist.append(i)
    return newlist

alist = [1, 2, 3]
ans = f(alist)
print("\nModified list:", ans)
print("Original list:", alist)

#List comprehension
print("\n--- LIST COMPREHENSION ---")

a = [i*i for i in range(10) if i % 2 == 1]
print("\n", a)

#Filter list
print("\n--- FILTER LIST ---")

def is_shorter(word, n):
    return len(word) < n
def shorten_list(wlist, n):
    short_wlist = list(filter(lambda w: is_shorter(w, n), wlist))
    return short_wlist

l = ["testando", "lista", "di", "parole", "per", "lunghezza"]
try:
    n = int(input("Given the list " + str(l) + 
    " enter an integer n to print words of the list shorter than n: "))
    short_l = shorten_list(l, n)
    print("List of words shorter than", n, "is:", short_l)  
except ValueError:
    print("Insert a valid integer")

#Map dictionary
print("\n--- MAP DICTIONARY --- ")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def fun(dic):
    key_list = dic.keys()
    keylen_list = list(map(len, key_list))
    return keylen_list

keylen_list = fun(lang)
print("\nLength of the keys: ", keylen_list)

#Lambda function
print("\n--- LAMBA FUNCTION  --- ")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print("\nList: ", language_scores)
language_scores.sort()
print("Sorted list: ", language_scores)

#Nested functions
print("\n--- NESTED FUNCTIONS --- ")

def square2(x):
    return x*x
def cube(x):
    return x**3
def raiseto6(x):
    return x*square2(x)*cube(x)
try:
    num = int(input("Enter an integer: "))
    print("Number", num ,"raised to the 6th power is: ", raiseto6(num))
except ValueError:
    print("Insert a valid integer")
    
#Decorators
print("\n--- DECORATORS --- \n")

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x

print(square(9))

#The Fibonacci sequence (part 2)
print("\n--- FIBONACCI SEQUENCE (PART 2) --- ")

def recur_fibo(n):    
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

print("\nFibonacci sequence (recursive): ")
for i in range(20):
    print(recur_fibo(i))

#The Fibonacci sequence (part 3)
print("\n--- FIBONACCI SEQUENCE (PART 3) --- ")

def loopFibonacci(n):
    if n <= 1:
        return n
    else:
        a=0
        b=1
        for i in range(n-2):
            a, b = b, a+b
        return b
    
print("\nFibonacci sequence (iterative): ")
for i in range(20):
    print(loopFibonacci(i))

testRecFibo = '''
def recur_fibo(n):    
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
recur_fibo(20)
''' 
testLoopFibo = '''
def loopFibonacci(n):
    if n <= 1:
        return n
    else:
        a=0
        b=1
        for i in range(n-2):
            a, b = b, a+b
        return b
loopFibonacci(20)
'''
print("Time(in seconds) for iterative Fibonacci: ", timeit.timeit(stmt=testLoopFibo, number=100))
print("Time(in seconds) for recursive Fibonacci: ", timeit.timeit(stmt=testRecFibo, number=100))

print('%s %d %s' % ('\nIterative Fibonacci is about', 
2000, "times faster than Recursive Fibonacci"))

#Class definition
print("\n--- CLASS DEFINITION --- ")

class polygon:
    x = []
    def __init__(self, components):
        if len(components) >= 3:
            self.x = components
        else:
            print("Error: number of components has to be at least 3")
        
    def setSideLen(self, n, xi):
        if n < len(self.x):
            self.x[n] = xi
    
    def getSideLen(self, n):
        return self.x[n]
    
    def perimeter(self):
        p = 0
        for i in range(len(self.x)):
            p += self.x[i]
        return p
    
    def getOrderedSides(self, increasing = True):
        orderedList = []
        if increasing:
            orderedList = sorted(self.x)
        else:
            orderedList = sorted(self.x, reverse = True)
        orderedTuple = tuple(orderedList)
        return orderedTuple
        
    
poly = polygon((3, 5, 8, 1, 11))
perimeter = poly.perimeter()
print("\nThe perimeter of the polygon is:", perimeter)
orderedPoly = poly.getOrderedSides(increasing = True)
print("Polygon sides in order:", orderedPoly)

# Class inheritance
print("\n--- CLASS INHERITANCE --- ")

class rectangle(polygon):
    
    def __init__(self, components):
        if len(components) == 2:
            self.x = components
        else:
            print("Error: number of components is not 2")
    def area(self):
        return self.x[0]*self.x[1]
            
rect = rectangle((2, 5))
area = rect.area()
print("\nThe area of the rectangle is:", area)
            
            
        