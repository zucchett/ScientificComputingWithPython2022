#!/usr/bin/env python
# coding: utf-8

# Ceren Yılmaz Gülten Exercise 2

# In[1]:


# 1. Global Variables
x = 5

def f(alist):
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


# In[24]:


# 2. List Comprehension 

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

def square(x):
    return x*x 
def is_odd(x):
    return x %2 ==1
ans_comp = list(map(square, filter(is_odd, range(10))))

print(ans_comp)


# In[139]:


# 3. Filter List 


def shorter(alist):
    
        return n> len(alist) 
           
n = 5
alist = ["aaaa","bcderhfj", "er", "hepworyhdkwm", "ertyu"]
m = len(alist)    
ans = list(filter(shorter,alist))
print(ans)


# In[145]:


# 4. Map Dictionary 

def key(word):
    return len(word)

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}      
result = list(map(key,lang))

print(result)


# In[150]:


# 5. Lambda Function 

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x:x)
print(language_scores)


# In[170]:


# 6. Nested Functions 
n = 2
def square(n):
    return n**2 
def cube(n):
    return n**3

def sixth_power(n):
    return cube(square(n))

print(square(n))
print(cube(n))
print(sixth_power(n))


# In[196]:


# 7. Decorators

def hello(func):
    def wrapper(n):
         for i in range(func(n)):
            print("Hello World!")
    return wrapper 
@hello
def square(x):
    return x*x

square(3)


# In[51]:


# 8. The Fibonacci sequence (part 2)
import timeit
def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1 
    else:
        
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(20):
      print(fibonacci(i)) 


# In[39]:


# 9. The Fibonacci sequence (part 3)

def loop_fibonacci(a):
    fib = [0,1]
    for n in range(0,a): 
        if n ==0:
            continue
        elif n == 1: 
            continue
        else: 
            k = fib[n-1] + fib[n-2]
            fib.append(k)


import timeit
get_ipython().run_line_magic('timeit', '-n100 fibonacci(19)')
get_ipython().run_line_magic('timeit', '-n100 loop_fibonacci(20)')

# for loop solution is much more faster than recursive solution. 
# approximately 3,86 times faster. 


# In[19]:


# 10. Class definition

class Polygon:
    
    x=[]
    
    def __init__(self,elements, increasing):
        
        self.x = elements
        self.increasing = increasing
    def getx(self,i):
        
        return self.x[i]
    
    def setx(self,i,xi):
        if i < len(self.x):
            self.x[i] =xi
        
    def perimeter(self):
        perimeter = 0
        for n in range(len(self.x)):
            perimeter += self.x[n]
        return perimeter 
    def getOrderedSides(self):
        if self.increasing == True: 
            self.x.sort()
            return self.x
        else:
            self.x.sort(reverse=True)
            return self.x
        

test = Polygon([6,7,8],False)

print(test.getx(2))

print(test.perimeter())

print(test.getOrderedSides())


# In[17]:


# 11. Class inheritance
class Polygon:
    
    x=[]
    
    def __init__(self,elements, increasing):
        
        self.x = elements
        self.increasing = increasing
    def getx(self,i):
        
        return self.x[i]
    
    def setx(self,i,xi):
        if i < len(self.x):
            self.x[i] =xi
        
    def perimeter(self):
        perimeter = 0
        for n in range(len(self.x)):
            perimeter += self.x[n]
        return perimeter 
    def getOrderedSides(self):
        if self.increasing == True: 
            self.x.sort()
            return self.x
        else:
            self.x.sort(reverse=True)
            return self.x
class Rectangle(Polygon):
    
    def __init__(self,elements):
        
        if len(elements) == 4:
            self.x = elements
        else:
            print("Error: Number of component is not true for rectangular.")
    def area(self):
        area = 1
        for i in range(len(self.x)):
            area *= self.x[i]
        return area 

test_case = Rectangle([4,5,7,8])

print(test_case.area())

