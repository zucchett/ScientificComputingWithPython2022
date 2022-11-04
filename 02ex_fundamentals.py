# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:47:00 2022

@author: 10
"""
import math
import timeit

#%%QUESTION 1

x = 5
alist = [1, 2, 3]

def f(alist):
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

ans = f(alist)
print(ans)
print(alist) # alist has not  been changed !!
#%% QUESTION 2
def square(x):
    """Square of x."""
    return x * x
    
def is_odd(x):
    return x % 2 == 1

ans = list(map(square, filter(is_odd ,range(10))))
print(ans)
#%% QUESTION 3
words =[ "hi", "python", "hello"]
n= 5

def filter_list(word):
    
    for i in range(len(word)):
        if word[i] < n:
            return len(word)
           
print(list(filter(filter_list,words)))

#%%QUESTION 4

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def length(key):
     return len(key)

x = list(map(length, lang)) 
# lengths = [len(v) for v in lang.keys()]t = list(

#%%QUESTION 5
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x:x[0])

#%%QUESTION 6
def sixth(x):
    def  cube(x):
        return x*x*x
        def square(x):
            return x*x
    print(cube(square(x)))
    
sixth(2) # it will give 2 to the power 6

#%%QUESTION 7

def hello(func):
    def wrapper():
        print('Ã¢Â€ÂœHello World!Ã¢Â€Â')
    return wrapper

@hello
def square(x):
    return x*x

square()

#%%QUESTION 8
def fibonacci(n):
        if n<=1:
            return n
        else:
            return(fibonacci(n-1) + fibonacci(n-2))

terms = 20
for i in range(terms):
    print(fibonacci(i))

#%% QUESTION 9
##### USING RECURSION
def recursiveFibonacci(n):
        if n<=1:
            return n
        else:
            return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))

recursiveFibonacci(20)

terms = 20
for i in range(terms):
    print(recursiveFibonacci(i))
    
#------------------------
##### USING LOOP
 # we should start by knowing first 2 elements
def loopFibonacci(n):
    num=[0,1]
    for i in range(n):
        num[i+1] = num[i]+num[i-1]
        num.append(num)
        print(num[i])

nth_number =20 
loopFibonacci(nth_number)

#--------TIME CALCULATION--------

stmt_code_1 =  "loopFibonacci(20)"
stmt_code_2 =  "recursiveFibonacci(20)"
iterations = 1000

setup_code1 = """
from __main__ import loopFibonacci  """

setup_code2 = """
from __main__ import recursiveFibonacci  """

time_1 = timeit.timeit(stmt = stmt_code_1, setup = setup_code1 ,number = iterations)
time_2 = timeit.timeit(stmt = stmt_code_2, setup = setup_code2 ,number = iterations)
print(f"The time for single iteration for loop is {time_1/iterations}s")
print(f"The time for single iteration for recursion is {time_2/iterations}s")

#%% QUESTION 10
import math

class polygon:
    
    
    x = []
    
    def __init__(self, components):
        self.x = components 

    def __del__(self):
        print("Goodbye")
    
    def getDimension(self):
        return len(self.x)
    
  
    def getSideLength(self, n):
        return self.x[n]
    
    def setSideLength(self, n, xi):
        if n < len(self.x):
            self.x[n] = xi
    
    def perimeter(self):
        per = 0
        for i in range(len(self.x)):
            per += self.x[i]
        return per
    
    def getOrderedSides(self,increasing=True):
        if increasing==True:
            sorted_list = sorted(self.x)
            return sorted_list
        else:
            sorted_list=sorted(self.x,reverse=True)
            return sorted_list
        
    #def setAddSide(self,n,s): #n=size to increase , s=added length 
        

Polygon = polygon([5, 2, 1])

#Polygon.setSideLength(2, 5) # set the third component to 5 if u want
Polygon.getSideLength(2)
Polygon.getOrderedSides(True)
print("The perimeter of the polygon is:", Polygon.perimeter()) 

#%% QUESTION 11

class rectangle(polygon): 
    
    def __init__(self, components):
        if len(components) == 2: #we can think as rectangle has 2 components one is short edge and the other is long edge
            self.x = components # a list is expected as input
        else:
            print("Error: you should enter 2 components(one for short edge , one for long edge)")
    
    # New methods that only belong to the child class
    def area(self):
        area=1
        for i in range(len(self.x)):
            area *= self.x[i]
        return area
    
Sides_Rect = [3,4]
Sides_Rect = rectangle(Sides_Rect)
print( "The area of the rectangle is ", Sides_Rect.area())
#%%
