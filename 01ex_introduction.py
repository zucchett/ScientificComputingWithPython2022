#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#ex1(a)
"""Write a program that:
prints the numbers from 1 to 100
but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
for numbers which are multiples of both three and five print "HelloWorld"."""

def HelloWorld(num):
    if num%3==0 and num%5==0:
        return 'HelloWorld'

    elif num % 3 == 0:
        return 'Hello'

    elif num % 5==0:
        return 'World'
    else:
        return num

for n in range(1,101):
    print(HelloWorld(n))


# In[ ]:


#Ex2. The swap
'''Write a program that swaps the values of two input variables x and y from command line (whatever the type).
Try to do that without using a temporary variable, exploiting the Python syntax.'''

x=input('x=')
y=input('y=')
x, y = y, x
print("x=", x)
print("y=", y)


# In[ ]:


#Ex3. Computing the distance
"""Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space,
where u and v are both 2-tuples (x,y).
Example: if u=(3,0) and v=(0,4), the function should return 5.
Hint: in order to compute the square root, import the math library with import math and use math.sqrt()."""
import math
def distance(a,b):
    distance=math.sqrt((b[0] - a[0])**2 +(b[1] - a[1])**2)
    return(distance)


a=(float(input('set a x')),float(input('set a y')))
b=(float(input('set b x')),float(input('set b y')))
distance(a,b)


# In[ ]:


#4.Counting letters
'''Write a program that calculates the number of times each character occurs in a given string. 
Ignore differences in capitalization.
The strings are in the cell below.'''

str1="Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
str2="The quick brown fox jumps over the lazy dog"

print (str1)
str1mod=str1.upper() #convert all to uppercase
str1_dict = {} #create a dictionary to count symbol and its number
for i in str1mod: 
    if i in str1_dict:
        str1_dict[i] += 1
    else:
        str1_dict[i] = 1
for i in str1_dict:
    print(i, str1_dict[i])

print (str2)

str2mod=str2.upper()
str2_dict = {}
for i in str2mod:
    if i in str2_dict:
        str2_dict[i] += 1
    else:
        str2_dict[i] = 1
for i in str2_dict:
    print(i, str2_dict[i])


# In[ ]:


#5.Isolating the unique
#Write a program that determines and counts the unique numbers in the list:
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
l=set(l)
print (l)
print(len(l))


# In[ ]:


#6.Casting
'''Write a program that:
-reads from command line two variables, that can be either int, float, or str.
-use the try/except expressions to perform the addition of these two variables, only if possible
-and print the result without making the code crash for all the int/float/str input combinations.'''
a,b=input().split()
try:
    c = str(a)+str(b)
    print(c)
except:
    print("not possible")
try:
    c = float(a)+float(b)
    print(c)
except:
    print("not possible")
try:
    c = int(a)+int(b)
    print(c)
except:
    print("not possible")


# In[ ]:


#7.Cubes
'''Create a list of the cubes of x for x in [0, 10] using:
a) a for loop
b) a list comprehension'''
num=[]
for n in range(0,11):
    n=n**3
    num.append(n)
print ('a)',num)

cubes = [x ** 3 for x in range(0,11)]
print ('b)',cubes)


# In[ ]:


#8. List comprehension
'''Write, using the list comprehension, a single-line expression that gets 
the same result as the code in the cell below.
'''
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print('a =',a)

b=[(i,j)for i in range(3) for j in range(4)]
print ('b =',b)


# In[ ]:


#9. Nested list comprehension
#Find and put in a tuple all unique Pythagorean triples for the positive integers  a,b and c with c<100.

def pythagoreanTriplets(limits) :
    c, m = 0, 2
    while c < limits :
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limits :
                break
            print(a, b, c)
        m = m + 1
if __name__ == '__main__' :
    limit = 100
    pythagoreanTriplets(limit)
c,m = 0,2
a=[(c,m)for n in range (1,m)]


# In[ ]:


#10. Normalization of a N-dimensional vector
'''Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers,
and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).'''
raw = list(map(float,input().split()))
norm = [float(i)/sum(raw) for i in raw]
print(norm)


# In[ ]:


#11. The Fibonacci sequence
"Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops."

def PrintFibonacci(length):
    first = 0
    second = 1
    print(first, second, end=" ")
    length -= 2
    while length > 0:
        print(first + second, end=" ")
        temp = second
        second = first + second
        first = temp
        length -= 1
if __name__ == "__main__":
    print("Fibonacci Series - ")
    PrintFibonacci(20)
    pass


# In[ ]:





# In[ ]:





# In[ ]:




