#!/usr/bin/env python
# coding: utf-8

# # 02ex_fundamentals
# 

# In[10]:


# 1. Global variables


def f_2(alist,x_range):
    
    temp_list=alist.copy() #this will prevent it from changing
                        
    
    for i in range(x_range):
        temp_list.append(i)
    return temp_list

alist = [1,2,3]
ans = f_2(alist,5)
print(ans)
print(alist)


# In[11]:


# 2. List comprehension


a = [x*x for x in range(10) if x % 2 == 1]
print(a)


# In[2]:


# 3. Filter list


n = int(input("enter the number: "))
a = input("enter words: ").split()

def filterlongword(string,number):
    return filter(lambda word:len(word)<number, string)


b = filterlongword(a, n)
print(list(b))


# In[3]:


# 4. Map dictionary


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
a = map(lambda key : len(key), lang.keys())
print(list(a))


# In[4]:


# 5. Lambda functions


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])
a = []
for i in language_scores:
    a.append(i[0])
print(a)


# In[5]:


# 6. Nested functions


def p2(x):
    return x*x


def p3(x):
    return x**3


def p6(x):
    return p3(x)**2


print(p6(7))


# In[7]:


# 7. Decorators


def hello(func):
    def wrapper(*args, **kwargs):
        print("hello world")
        return func(*args)
    return wrapper


@hello
def square(x):
    return x*x


print(square(7))


# In[8]:


# 8. The Fibonacci sequence (part 2)


def fib(x):
    if x < 3:
        return 1
    else:
        # return x-1 + x-2
        return fib(x-1) + fib(x-2)

print(fib(20))


# In[9]:


# 9. The Fibonacci sequence (part 3)


import timeit

s_1 = """
def fib(x):
    if x < 3:
        return 1
    else:
        # return x-1 + x-2
        return fib(x-1) + fib(x-2)

fib(20)
"""
s_2 = """
def fibo(N):
    fibonacciSeries = [1, 1]
    if N > 2:
        for i in range(2, N):
            nextOne = fibonacciSeries[i - 1] + fibonacciSeries[i - 2]
            fibonacciSeries.append(nextOne)
    return nextOne

fibo(20)
"""

print(timeit.timeit(stmt=s_1, number=1))
print(timeit.timeit(stmt=s_2, number=1))


# In[10]:


# 10. Class definition


class polygon:
    x = tuple()

    def __init__(self, components):
        if len(components) < 3:
            raise Exception()

        self.x = components
        print(components)

    def perimeter(self):
        return sum(self.x)

    def getorderedSides(self, increasing=True):
        list_1 = []
        for i in range(len(self.x)):
            list_1.append(self.x[i])
        if increasing:
            list_1.sort()
            return list_1
        else:
            list_1.sort(reverse=True)
            return list_1


a = polygon((9, 8, 7, 6))

print("The perimeter is :", a.perimeter())
print("The orderedsides are:", a.getorderedSides(increasing=True))


# In[13]:


# 11. Class inheritance


class polygon:
    x = tuple()

    def __init__(self, components):
        self.x = components
        print(components)

    def perimeter(self):
        s2 = 0
        for i in range(len(self.x)):
            s2 += self.x[i]
        return (s2)

    def getorderedSides(self, increasing=True):
        list_1 = []
        for i in range(len(self.x)):
            list_1.append(self.x[i])
        list_1.sort()
        return (list_1)


class rectangle(polygon):
    def __init__(self, components):
        if len(components) == 2:
            self.x = components
        else:
            raise Exception("Error: This is not rectangle!!!")

    def area(self):
        return (max(self.x) * min(self.x))
    
    
a = rectangle((12,6))

print("The area is : ", a.area())


# In[ ]:




