#!/usr/bin/env python
# coding: utf-8

# 1)

# In[1]:


def f(alist):
    x = 5
    alist = [1, 2, 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) 


# 2)

# In[3]:


ans = [x*x for x in range(10) if(x**2 % 2 == 1)] 
ans


# 3)

# In[ ]:


words = ["a", "aa", "aaa", "4444", "55555", "666666", "7777777"] 
x = int(input("max lenght: "))
def fil(words, x):
    filtered = list(filter(lambda i : len(i) < x, words))
    return filtered
print( fil(words,x))


# 4)

# In[ ]:


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def take(dic):
    return len(dic)

leng = list(map(take,lang))
print(leng)


# 5)

# In[7]:


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = (lambda x : x[0])) 

print(language_scores)


# 6)

# In[10]:


def xp2(x): 

    return x**2
def xp3(x): 
    return x**3

def xp6(x): 
    return(xp2(xp3(x))) 

xp6(2)


# 7)

# In[11]:


def hello(func):
    def wrapper(x): #wrapper
        print("Hello World!")
        return func(x)    
    return wrapper
    
@hello 
def square(x):
    return x*x
    
print(square(12))


# 8)

# In[17]:


def recfib(i):
    if i == 0: 
        return 0
    elif i == 1: 
        return 1
    else:
        return recfib(i-1)+recfib(i-2)

flist=[]
for x in range(0,21):
    flist.append(recfib(x))

print(flist)


# 9)

# In[1]:


import timeit

def loopFibonacci(t):
    
    FS = [0,1]
    n=1
    for x in range(t-2):
        FS.append(FS[x]+FS[x+1])
    print("loop fib",FS)


def recursiveFibonacci(t):
    
    
    def recfib(i):
        if i == 0: 
            return 0
        elif i == 1: 
            return 1
        else:
            return recfib(i-1)+recfib(i-2)
    flist=[]
    for y in range(t):
        flist.append(recfib(y))
    print("rec fib",flist)


loop = timeit.timeit(stmt='loopFibonacci(20)', globals=globals(), number=1)
print("time of loop:",loop)
rec = timeit.timeit(stmt='recursiveFibonacci(20)', globals=globals(), number=1)
print("time of rec:",rec)

print("Loop is faster, the difference is:",(rec-loop))


# 10)

# In[2]:


class Polygon:
    def __init__(self, sides: tuple):
        if len(sides) < 3:
            raise ValueError("Shouldn't be less sides than 3")
        self.sides = sides

    def set_side(self, index, new_side):
        sides = list(self.sides)
        sides[index] = new_side
        self.sides = tuple(sides)
        return self.sides[index]

    def get_side(self, index):
        return self.sides[index]

    def perimeter(self):
        return sum(list(self.sides))

    def getOrderedSides(self, increasing=True):
        if increasing:
            sides = list(self.sides)
            sides = sorted(sides)
            self.sides = tuple(sides)
            return self.sides
        else:
            return self.sides

        
polygon = Polygon((2,4,5))
print(polygon.set_side(0,10))
print(polygon.get_side(1))
print(polygon.perimeter())
print(polygon.getOrderedSides(True))


# 11)

# In[15]:


class Polygon:
    def __init__(self, sides: tuple):
        if len(sides) < 3:
            raise ValueError("Atleast 3")
        self.sides = sides

    def set_side(self, index, new_side):
        sides = list(self.sides)
        sides[index] = new_side
        self.sides = tuple(sides)
        return self.sides[index]

    def get_side(self, index):
        return self.sides[index]

    def perimeter(self):
        return sum(list(self.sides))

    def getOrderedSides(self, increasing=True):
        if increasing:
            sides = list(self.sides)
            sides = sorted(sides)
            self.sides = tuple(sides)
            return self.sides
        else:
            return self.sides

        
polygon = Polygon((10,4,7))
print(polygon.set_side(0,20))
print(polygon.get_side(1))
print(polygon.perimeter())
print(polygon.getOrderedSides(True))


# In[ ]:




