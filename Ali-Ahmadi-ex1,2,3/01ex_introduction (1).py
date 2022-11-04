#!/usr/bin/env python
# coding: utf-8

# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `01ex_introduction.py`.
# 
# In case you need multiple files, name them `01ex_introduction_es01.py`, `01ex_introduction_es02.py` and so on. 
# 
# The exercises need to run without errors in `python3`.

# 1\. **The HelloWorld replacement**
# 
# a) Write a program that:
# - prints the numbers from 1 to 100
# - but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
# - for numbers which are multiples of both three and five print "`HelloWorld`".
# 
# b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

# In[1]:







for x in range(1, 101):
    if x%15 == 0: 
       print ("Hello World") 
       

    elif x%3 == 0:
           print ("Hello")
           
           
    elif x%5 == 0:
           print ("World")
           

        
    else:
        print (x) 
        


# In[2]:




y = ("python", "Works", "Hello World")


for x in range(1, 101):
    if x%15 == 0: 
       print (y[2]) 
       

    elif x%3 == 0:
           print (y[0])
           
           
    elif x%5 == 0:
           print (y[1])
           

        
    else:
        print (x) 


# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# In[3]:



x = 10
y = 5

x = x+y
y = x-y
x = x-y 

print ("After swapping: x = ", x, "y =", y)


# 3\. **Computing the distance**
# 
# Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.
# 
# Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# In[4]:




import math
u = (3,0)
v = (0,4)

def main():
    distance = math.sqrt(( (u[0]-v[0])**2)+ (u[1]-v[1])**2 )

    print (distance)
    
main()


# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The strings are in the cell below.

# In[5]:


s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


# In[6]:



s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

all_freq = {}
  
for i in s1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
print ("Count of all characters in s1 is  :/n"
                                        +  str(all_freq))

for i in s2:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
print ("Count of all characters in s2 is :\n "
                                        +  str(all_freq))


# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers in the list:

# In[7]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# Do the same exploiting only the Python data structures.

# In[8]:



l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l1 = []

count = 0

for i in l:
    if i not in l1:
        count += 1
        l1.append(i)
    
        
print (count)


# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# In[9]:


x = input("enter the : ")


try:
    z = x + 2
    print(z)
except:
    print(x, " is not a number")


# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[10]:


for i in range(1,11):
    x=i*i*i
    print(x)


# In[11]:


list1=[0,1,2,3,4,5,6,7,8,9,10]
for i in list1:
    x=i*i*i
    print(x)


# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# In[12]:


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# In[13]:


[(a,b,c) for c in range(1,101) for b in range(1,101) for a in range(1,101) if a**2+b**2==c**2]


# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# In[14]:


tup1=(2,3,4,5,6)
max(tup1)
def normalize_tup(tup):
    tup2=[] 
    for i in range(len(tup)):
        tup2.append(tup[i]/sum(tup)) #i normalized it the total sum of the tuple
    return tuple(tup2)
        


# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# In[15]:


#while

s = int(input("How many sentence? "))


n1, n2 = 0, 1
c = 0

# check if the number of terms is valid
if s <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif s == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while c < s:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       c += 1


# In[16]:


#for
s = int(input("How many sentence? "))

x=0
n1, n2 = 0, 1
c = 0

# check if the number of terms is valid
if s <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif s == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
for x in range(s):
    if c>s: 
        break
    else:    
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2=nth
        c+=1


# In[ ]:




