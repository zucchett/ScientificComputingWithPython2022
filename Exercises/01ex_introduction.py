#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1 - hannafalch_nastby

# This is my soulutions to Exercise 1 in the class "Scientific computing with Python". I have chosen to solve many of the tasks by using functions, so as to avoid using many global variables.

# ### 1. The HelloWorld replacement

# a)

# In[17]:


numbersList = list(range(1, 101))
for number in numbersList:
    if (number % 3 == 0) and (number % 5 == 0):
        numbersList[number-1] = "Helloworld"
    elif (number % 3 == 0):
        numbersList[number-1] = "Hello"
    elif (number % 5 == 0):
        numbersList[number-1] = "World"

numbersTuple = tuple(numbersList)
print(numbersTuple)


# b)

# In[19]:


for i in range(len(numbersList)):
    if numbersList[i] == "Hello":
        numbersList[i] = "Python"
    elif numbersList[i] == "World":
        numbersList[i] = "Works"   
print(numbersList)


# ### 2. The swap

# In[22]:


def replaceFunc():
    x = input("Set the value of variable x: ")
    y = input("Set the value of variable y: ")
    x, y = y, x
    print(f"The value of variable x is: {x}")
    print(f"The value of variable y is: {y}")
    
replaceFunc()


# ### 3. Computing the distance

# In[27]:


import math
def euclideanDist(u, v):
    return math.sqrt((u[1]-u[0])**2+(v[1]-v[0])**2)

u = tuple((3,0))
v = tuple((0,4))
euclideanDist(u, v)


# ### 4. Counting letters

# In[53]:


def countingLetters(s):
    letterDict = {}
    for letter in s.lower():
        if letter not in letterDict.keys():
            letterDict[letter] = 1
        else:
            letterDict[letter] += 1
        sortedDict = sorted(letterDict.items())
    return sortedDict

    
s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"  

countingLetters(s1)


# ### 5. Isolating the unique

# In[61]:


def uniqueNumbers1(l):
    uniqueList = []
    for n in l:
        if n not in uniqueList:
            uniqueList.append(n)
    print(uniqueList)
    print(f"There are {len(uniqueList)} unique characthers")

#exploiting the Python data structures
def uniqueNumbers2(l):
    numberSet = set(l)

    print(numberSet)
    print(f"There are {len(numberSet)} unique characthers")

          
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]          
uniqueNumbers1(l)
uniqueNumbers2(l)


# ### 6. Casting
# 
# 

# In[165]:


def casting():
    inputVar1 = input("Choose a variable, either int, float or str: ")
    inputVar2 = input("Choose a variable, either int, float or str: ")

    try:
        #check if it is an integer
        var1 = int(inputVar1)
    except ValueError:
        try:
            #check if it is a float
            var1 = float(inputVar1)
        except ValueError:
            #it is a string
            var1 = inputVar1
    
    try:
        #check if it is an integer
        var2 = int(inputVar2)
    except ValueError:
        try:
            #check if it is a float
            var2 = float(inputVar2)
        except ValueError:
            #it is a string
            var2 = inputVar2
    
    try:
        x = var1 + var2
        print(f"Addition gives: {x}")
        
    except:
        print(f"Addition was not possible with the variables {inputVar1} and {inputVar2}")
        
casting()


# ### 7. Cubes

# a) using a for loop
# 

# In[90]:


def forCube():
    cubeList = []
    for i in range(11):
        cubeList.append(i**3)
    print(cubeList)
forCube()


# b) using a list comprehension

# In[91]:


def listCube():
    cubeList = [x**3 for x in range(11)]
    print(cubeList)

listCube()


# ### 8. List comprehension

# In[103]:


listComp = [(i, j) for j in range(4) for i in range(3)]
print(listComp)


# ### 9. Nested list comprehension

# In[123]:


def pyth():
    c = 0
    intTuple = []
    while c < 100:
        for a in range(1,100):
            for b in range(1,100):
                c = math.sqrt(a**2 + b**2)
                if c <= 100 and c.is_integer():
                    intTuple.append((a, b, int(c)))
    intTuple = tuple(intTuple)
    for i in intTuple:
        print(i)
    
pyth()


# In[121]:


def pythagoreanTriplets(limits) :
    c, m = 0, 2
 
    # Limiting c would limit
    # all a, b and c
    while c < limits :
         
        # Now loop on n from 1 to m-1
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
 
            # if c is greater than
            # limit then break it
            if c > limits :
                break
 
            print(a, b, c)
 
        m = m + 1
pythagoreanTriplets(100) 


# ### 10. Normalization of a N-dimensional vector

# In[166]:


def norm(vec):
    N = 0
    for i in vec:
        N += i
    normVec = [x / (N**2) for x in vec]
    print(normVec)


exVec = (1, 4, 7, 10, 4)    
    
norm(exVec)


# ### 11. The Fibonacci sequence

# In[154]:


def fib():
    fibList = [0, 1]
    F_0 = 0
    F_1 = 1
    for i in range(20):
        while len(fibList) < 20:
            F = F_1 + F_0
            fibList.append(F)
            F_0 = F_1
            F_1 = F
            i += 1
    print(fibList)
fib()


# %%
