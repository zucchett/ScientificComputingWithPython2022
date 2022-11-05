#!/usr/bin/env python
# coding: utf-8

import math as m


#TASK 1

def f(alist,x):
    blist = alist.copy()
    for i in range(x):
        blist.append(i)
    return blist

alist = [1,2,3]
ans = f(alist,5)
print(ans)
print(alist)




#TASK 2
ans = [x**2 for x in range(10) if x % 2 ==1]
print(ans)





#TASK 3

def filter_list(words, n):
    return list(filter(lambda word : len(word)<n, words))

print(filter_list(["hello", "hi","goodmorning","ciao"],5))





#TASK 4

def map_dict(dic):
    return list(map(lambda key : len(key), dic.keys()))

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(map_dict(lang))





#TASK 5

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

#alternative solution:
language_scores2 = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores2.sort()
print(language_scores2)




#TASK 6
def squared(x):
    return x**2

def cubed(x):
    return x**3

def power6(x):
    return squared(cubed(x))

print(power6(2))





#TASK 7

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper

@hello
def square(x):
    return x*x

print(square(3))




#TASK 8

def recursiveFibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

    
for n in range(1,21):
    print(recursiveFibonacci(n))




def loopFibonacci(n):
    if n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        a,b = 0,1
        for i in range(n-2):
            a,b = b, a+b
        return b
    
for n in range(1,21):
    print(loopFibonacci(n))




#TASK 9

get_ipython().run_line_magic('timeit', 'loopFibonacci(20)')
get_ipython().run_line_magic('timeit', 'recursiveFibonacci(20)')



# Results:
# loop: 2.5 us
# recursive: 3.72 ms
# We can see that the loop is almost 1000 times faster



#TASK 10

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

