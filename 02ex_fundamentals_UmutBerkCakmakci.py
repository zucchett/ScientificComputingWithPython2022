# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:57:07 2022

@author: Umut Berk Cakmakci
"""

# 02ex_fundamentals_es01
"""
print("\n02ex_es01 answer:\n--------------------------------------------------")

def f(alist,x):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(list(alist),5)
print("ans  :", ans)
print("alist:", alist) # alist has been changed
"""

# 02ex_fundamentals_es02
"""
print("\n02ex_es02 answer:\n--------------------------------------------------")
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

# ans2 = []
# for x in range(10): 
#     if x % 2 == 1: 
#        ans2.append(x*x)
# print(ans2)

ans3 = [y*y for y in range(10) if y%2==1]
print(ans3)

"""

# 02ex_fundamentals_es03
"""
print("\n02ex_es03 answer:\n--------------------------------------------------")
s1 = list(map(str, input("Enter multiple words: ").split()))
n = int(input("enter n: "))
c = []
def is_short(x):
    a = len(s1)
    for i in range(0, a, 1):
        if len(s1[i]) < n:
            if s1[i] not in c:
                c.append(s1[i])

print("\nThe original list: ", s1)
b=list(filter(is_short, s1))
print("\nThe filtered list: " , c)

"""

# 02ex_fundamentals_es04
"""
print("\n02ex_es04 answer:\n--------------------------------------------------")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

x = list(map(len, lang)) 
print(x)
"""

# 02ex_fundamentals_es05
"""
print("\n02ex_es05 answer:\n--------------------------------------------------")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x:x[0])
print(language_scores)
"""

# 02ex_fundamentals_es06
"""
print("\n02ex_es06 answer:\n--------------------------------------------------")
def squared(x):
    return x**2

def cubed(x):
    return x**3

def sixth(x):
    x=cubed(x)
    x=squared(x)
    return x
    
x=int(input("Enter a value for x: "))
x2=squared(x)
x3=cubed(x)
x6=sixth(x)
print("Square of ", x,":", x2, "\nCube of ", x,":", x3, "\n6th power of ", x,":", x6)
"""

# 02ex_fundamentals_es07
"""
print("\n02ex_es07 answer:\n--------------------------------------------------")
def hello(func):
    def wrapper(x):
        print("Hello World!")
        print(func(x))
    return wrapper

@hello
def square(x):
    return x*x

square(3)
"""

# 02ex_fundamentals_es08
"""
print("\n02ex_es08 answer:\n--------------------------------------------------")
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 20
fibo_list = []

print("Fibonacci sequence:")
for i in range(nterms):
    fibo_list.append(recur_fibo(i))

print(fibo_list)
"""

# 02ex_fundamentals_es09
"""
print("\n02ex_es09 answer:\n--------------------------------------------------")
import timeit

stmt_lF='''
fib = [0, 1]

for i in range(2, 20, 1):
    fib.append(fib[i-1]+fib[i-2])

print(fib)
'''
stmt_rF='''
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 20
fibo_list = []

for i in range(nterms):
    fibo_list.append(recur_fibo(i))

print(fibo_list)
'''
time_lF=timeit.timeit(stmt = stmt_lF, setup = "", number = 1)
time_rF=timeit.timeit(stmt = stmt_rF, setup = "", number = 1)
print("Time passed for Loop Function Fibonnacci:", time_lF)
print("Time passed for Recursive Function Fibonnacci:", time_rF)
print("Loop F. is ", int(time_rF/time_lF), " times faster than Recursive F.")
"""

# 02ex_fundamentals_es10
"""
print("\n02ex_es10 answer:\n--------------------------------------------------")
class polygon:
    
    def perimeter(self,y):
        per=0
        for i in range(y):
            per += x[i]
        return per
    
    def getOrderedSides(self, x, increasing):
        if increasing == True:
            x=sorted(x)
            x=tuple(x)
            return x
        else:
            x=sorted(x)
            x=reversed(x)
            x=tuple(x)
            return x

abc=polygon()
x = tuple(map(int, input("Enter at least 3 value for the polygon: ").split()))
y = len(x)
print("the polygon has ", y, "sides")
print("the perimeter of the polygon is: ", abc.perimeter(y))
print("the sorted list of the lengths of the polygon is: ", abc.getOrderedSides(x,True))
"""

# 02ex_fundamentals_es11
"""
print("\n02ex_es11 answer:\n--------------------------------------------------")
import math

class rectangle(polygon):
 
    def area(self,x): 
        s2=abc.perimeter(y)/2
        s3=1
        for i in range(y):
            s3 *= (s2-x[i])
        return math.sqrt(s3)
    
c=rectangle()

if(y!=4):
    print("Please enter 4 valid values to create a rectangle!")
else:
    if(x[0]==x[1]):
        if(x[2]==x[3]):
            print("The area of the rectangle is:", c.area(x))
        else:
            print("Please enter 4 valid values to create a rectangle!")
    elif(x[0]==x[2]):
        if(x[1]==x[3]):
            print("The area of the rectangle is:", c.area(x))
        else:
            print("Please enter 4 valid values to create a rectangle!")
    elif(x[0]==x[3]):
        if(x[2]==x[1]):
            print("The area of the rectangle is:", c.area(x))
        else:
            print("Please enter 4 valid values to create a rectangle!")
    else:
        print("Please enter 4 valid values to create a rectangle!")

"""