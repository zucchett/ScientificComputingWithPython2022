import math

"""
_______________________ ESERCIZIO 1 _________________________

a) Write a program that:

    prints the numbers from 1 to 100
    but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
    for numbers which are multiples of both three and five print "HelloWorld".

"""
for  i in range(1,100):
    if (i % 3 == 0):    
        if(i % 5 == 0): #multiples of both three and five
            print("HelloWorld")
        else:   #multiples of three
            print("Hello")

    elif(i % 5 == 0): #multiples of five
        print("World")
    else:   #other numbers
        print(i)

"""
b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".
"""
tup = (1,) #tuple is immutable, so at every iteration I create a new tuple which is the concatenation of the old one with the new number/word
for  i in range(2,100):
    if (i % 3 == 0):
        if(i % 5 == 0):
            tup = tup + ("PythonWorks",)
            #print("HelloWorld")
        else:
            tup = tup + ("Python",)
            #print("Hello")

    elif(i % 5 == 0):
        tup = tup + ("Works",)
        #print("World")
    else:
        tup = tup + (i,)
        #print(i)
print(tup)



"""
_______________________ ESERCIZIO 2 _________________________

Write a program that swaps the values of two input variables x and y from command line (whatever the type).
Try to do that without using a temporary variable, exploiting the Python syntax.


"""

x = input("Insert the first value:")
y = input("Insert the second value:")
x, y = y, x #swap of the values

#print(x)
#print(y)

#another way to do the exercise
#import sys
#x = sys.argv[2]
#y = sys.argv[1]




"""
_______________________ ESERCIZIO 3 _________________________

Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).
Example: if u=(3,0) and v=(0,4), the function should return 5.
Hint: in order to compute the square root, import the math library with import math and use math.sqrt().

"""

def euclideanDistance(p1,p2): #we assume that p1 e p2 are 2-tuples (x,y)

    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) #from the definition of euclidean distance between two points
    return dist

#test example
p1 = (3, 0,)
p2 = (0,4,)

dist = euclideanDistance(p1,p2)
print(dist)




"""
____________________________________ ESERCIZIO 4 ____________________________________

Counting letters

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

The strings are in the cell below.

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

"""

def charNumber(s) :
    d = {};  #creation of an empty dictionary
    s = s.lower() #to ignore capitalization problem
    for i in range(len(s)):   #for each char of the string
        if (s[i] in d ) == True : # if the char was already in the dictionary
            d[s[i]] = d[s[i]] + 1 #increment the counter
            
        else: #if we find a new char
            d[s[i]] = 1 #create a new couple

    return d 

#first string    
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld." 
d1 =charNumber(s1)
print(sorted(d1.items()))

#second string
s2 = "The quick brown fox jumps over the lazy dog"
d2 =charNumber(s2)
print(sorted(d2.items()))


"""
____________________________________ ESERCIZIO 5 ____________________________________

Write a program that determines and counts the unique numbers in the list:

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

"""

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20] 
 
l_sort = sorted(l)  #sort the given list
l_unique = []   #create a new list for the unique numbers
i = 0
while (i < len(l_sort)-1): 
    if (l_sort[i+1] != l_sort[i]): # element is different from the next one, so it's unique (the list is sorted)
        l_unique.append(l_sort[i]) #insert the element in the list of unique numbers
    count = 1 #counter 
    while (i+count < len(l_sort)-1 and l_sort[i+count]==l_sort[i]): #as long as the element is equal to its next
            count = count + 1 #increment the counter
    i = i + count #update the list index
if (l_sort[i] != l_sort[i-1]) : #check the last element
    l_unique.append(l_sort[i])       
print(l_unique)
print("The unique numbers in the list are: ", len(l_unique))

"""
Do the same exploiting only the Python data structures.

"""

d = {}  # Create empty dictionary

for i in range(len(l)): # Create a dictionary with <key = number >:<number of time it appears>
	if( (l[i] in d) == True):   # Contained in dictionary
		d[l[i]] = (d[l[i]]+1)   # Update element

	else:   # Not contained in dictionary
		d[l[i]] = 1 # Add new element

for i in range(len(l)): # Delete item with occurance higher than 1
	if d.get(l[i], -1) > 1:
		d.pop(l[i])

# Order to better explain the out
d = dict(sorted(d.items()))
# Print the dictionary with the unique values
print(d.keys())
# Count them
print("The unique numbers in the list are: ", len(d))



"""
____________________________________ ESERCIZIO 6 ____________________________________ 

Casting

Write a program that:

reads from command line two variables, that can be either int, float, or str.
use the try/except expressions to perform the addition of these two variables, only if possible
and print the result without making the code crash for all the int/float/str input combinations.


"""

try :
    v1 = float(input("Insert the first variable: " )) #first input from the command line
    v2 = float(input("Insert the second variable: ")) #second input from the command line
    sum = v1 + v2
    if(sum == int(sum)): 
        print(int(sum)) #if the sum is an integer print the integer value
    else: 
        print(sum) 

except :
    print("Wrong type insered")





"""
____________________________________ ESERCIZIO 7 ____________________________________

Cubes

Create a list of the cubes of x for x in [0, 10] using:
a) a for loop
b) a list comprehension

"""

# (a) loop
la = []
for i in range(11) :
    la.append(i**2)
print(la)

# (b) list comprehension
lb = [i**2 for i in range(11)]
print(lb)



"""
____________________________________ ESERCIZIO 8 ____________________________________

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


"""

a = [(i, j) for i in range(3) for j in range(4)]
print(a)


"""
____________________________________ ESERCIZIO 9 ____________________________________ 

A Pythagorean triple is an integer solution to the Pythagorean theorem a^2 + b^2 = c^2. The first Pythagorean triple is (3, 4, 5).
Find and put in a tuple all unique Pythagorean triples for the positive integers a, b and c with c < 100.

"""

def isPrime(x,y): #check if two numbers are prime to each other
    if math.gcd(x,y) > 1 : # if their MCD is > 1 they are not prime
        return False 
    else:
        return True

pt = [(a, b, int(math.sqrt(a**2 + b**2),)) for a in range(3, 101) for b in range(4, a+1) if math.sqrt(a**2 + b**2) < 100 and int(math.sqrt(a**2 + b**2)) == math.sqrt(a**2 + b**2) and isPrime(a,b)] 
print(pt)




"""
____________________________________ ESERCIZIO 10 ____________________________________

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, 
and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

"""

x = [1, 10, 2, 3, 0]    #input vector

sum = 0    #squared sum
for i in range(len(x)-1):   # compute the sum of the squares
	sum = sum + x[i]**2
for i in range(len(x)-1):   # divide every element for the sum
	x[i] = x[i]/sum
print(x)


"""
____________________________________ ESERCIZIO 11 ____________________________________

The Fibonacci sequence
Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

"""


def iterFib(n) :
    x = 0
    y = 1
    fib = [0]   #add the first element
    for i in range(n-1) :
        x, y = y, x + y 
        fib.append(x)   #insert the computed value in the list
    return fib

print(iterFib(20))
