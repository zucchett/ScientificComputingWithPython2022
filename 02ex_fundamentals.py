#!/usr/bin/env python
# coding: utf-8

# # Exercises 2

# ### Tone Alsvik Finstad

# ### 1. Global variables

# In[2]:


def f(alist, x):
    ans=alist.copy()
    for i in range(x):
        ans.append(i)
    return ans

alist = [1, 2, 3]
ans = f(alist, 5)
print(f"New list: {ans}")
print(f"Old list: {alist}")  #Checking that this list is unchanged


# ### 2. List comprehension

# In[4]:


a = [x * x for x in range(10) if x%2==1] #Using list comprehension
print(a)


# ### 3. Filter list

# In[5]:


def filter_list(input_list, n):
    a=list(filter(lambda element: len(element)<n, input_list))
    return a
liste=["haudhu", "hei", "hahahoahw", "a"]
print(filter_list(liste, 4))


# ### 4. Map dictionary

# Consider the following dictionary:
# 
# lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
# 
# Write a function that takes the above dictionary and uses the map() higher order function to return a list that contains the length of the keys of the dictionary.

# In[1]:


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def length_dict(dict):
    return list(map(lambda x: len(x), dict))
print(length_dict(lang))


# ### 5. Lambda functions

# In[2]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda item: item[0])
print(language_scores)


# ### 6. Nested functions

# In[3]:


def square(x):
    return x**2
def cube(x):
    return x**3
def sixth_power(x):
    return square(cube(x))
print(sixth_power(4))


# ### 7. Decorator

# In[37]:


def hello(func):
    def wrapper(x):
        print("Hello world!")
        func(x)
    return wrapper

@hello
def square(x):
    return x*x

square(5)


# ### 8. The fibonacci sequence

# In[39]:


def recursive_fibonacci(i):
    if i in [0,1]:
        return i
    return recursive_fibonacci(i-1)+recursive_fibonacci(i-2)
fib_numbers=[recursive_fibonacci(i) for i in range(20)]
print(fib_numbers)


# ### 9. The fibonacci sequence

# In[40]:


import timeit

def loop_fibonacci(n):
    fib_seq=[0,1]
    while len(fib_seq)<20:
            fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq
    

get_ipython().run_line_magic('timeit', 'fib_numbers=[recursive_fibonacci(i) for i in range(20)]')
get_ipython().run_line_magic('timeit', 'fib_seq=loop_fibonacci(20)')

fib_seq=loop_fibonacci(20)
print(fib_numbers)
print(fib_seq)

#Recursive is slower??


# ### 10. Class definition

# In[44]:


class Polygon:
    x=()
    
    def __init__(self, components):
        self.x=components
    
    def __del__(self):
        print("Goodbye")
        
    def get_length(self, index):
        return x[index]
    
    def set_length(self, index, new_val):
        x_new=list(self.x)
        x_new[index]=new_val
        self.x=tuple(x_new)
    
    def perimeter(self):
        perimeter=0
        for l in self.x:
            perimeter+=l
        return perimeter
    
    def getOrderedSides(self, increasing=True):
        a=list(self.x)
        a.sort(reverse = not increasing)
        b=tuple(a)
        return b
    
triangle=Polygon((5,2,3))
a=triangle.perimeter()
b=triangle.getOrderedSides(increasing=True)
c=triangle.getOrderedSides(increasing=False)
print(a)      
print(b)
print(c)
triangle.set_length(1,22)
print(triangle.x)


# ### 11. Class inheritance

# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# In[32]:


class Rectangle(Polygon):
    
    def __init__(self, components):
        if (len(components)==4 and len(set(components))==2):
            self.x=components
        else:
            self.__del__()
    
    def area(self):
        return list(set(self.x))[0]*list(set(self.x))[1]
    
rect=Rectangle((2,2,3,3))
print(rect.perimeter())
print(rect.area())

