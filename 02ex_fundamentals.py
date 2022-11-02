# Author: Luca Bonaventura matr. 2090005

#_________________________________________________ESERCIZIO 1__________________________________________________

"""
1. Global variables

Convert the function  into a function that doesn't use global variables and that does not modify the original list

x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
"""
print("___________ESERCIZIO 1___________")

def f(alist):
    x = 5 # x is not global
    alist=[1, 2 , 3]
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist) #does not modify the original list
print(ans)
print(alist) # alist hasn't been changed


#_________________________________________________ESERCIZIO 2__________________________________________________

"""
2. List comprehension

Write the following expression using a list comprehension:

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))
"""
print("___________ESERCIZIO 2___________")

# write the odd squres with odd bases <10
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print (ans)

# write the odd squres with odd bases <10 using list comprehension
ans = [y**2 for y in range(10) if (y%2 == 1)]
print (ans)

#_________________________________________________ESERCIZIO 3__________________________________________________

"""
3. Filter list

Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n.
"""
print("___________ESERCIZIO 3___________")

myList = ["a2", "bbb4", "cc3", "dddddd6"]
#length of the filtering words
leng = 5;
print(myList)
# Function length check, return true only if the word il shorter than leng
def lengCheck(word, l):
	if len(word)< l: return True
	else: return False

#Apply the function lengCheck to every word of the list
shorter = list(filter(lambda myList_: lengCheck(myList_, leng), myList))
print(shorter)

#_________________________________________________ESERCIZIO 4__________________________________________________

"""
4. Map dictionary

Consider the following dictionary:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

Write a function that takes the above dictionary and uses the map() higher order function to return a list that contains the length of the keys of the dictionary.
"""
print("___________ESERCIZIO 4___________")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(lang)
# Function that return the length of the key
def keyLength(x):
	return len(x)

# Apply keyLength to every element of lang
lengs = list(map(keyLength, lang))
print(lengs)

#_________________________________________________ESERCIZIO 5__________________________________________________

"""
5. Lambda functions

Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

Hint: use the method sort() and its argument key of the list data structure.
"""
print("___________ESERCIZIO 5___________")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

print(language_scores)
# Use sort on language_scores with key of the first element of the tuple
language_scores.sort(key = lambda tup: tup[0])
print(language_scores)

#_________________________________________________ESERCIZIO 6__________________________________________________

"""
6. Nested functions

Write two functions: one that returns the square of a number, and one that returns its cube.

Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
"""
print("___________ESERCIZIO 6___________")

# return square of x
def squareN(x):
	return x**2

# return cube of x
def cubeN (x):
	return x**3

# return 6th power of x
def sixthN (x):
	return squareN(cubeN(x))

# Test sixthN on 2
print (sixthN(2))

#_________________________________________________ESERCIZIO 7__________________________________________________
"""
7. Decorators
Write a decorator named hello that makes every wrapped function print Hello World! each time the function is called.
The wrapped function should look like:
"""
print("___________ESERCIZIO 7___________")

# Define decorator
def hello(func):
	def wrapper(self):
		# print "Hello World!" before invoking the function
		print("Hello World!")
		# launch the function passing the arguments and retourning what it retourns
		return func(self)
	return wrapper

#define the function with decrator hello
@hello
def square(x):
    return x*x

print(square(2))
#_________________________________________________ESERCIZIO 8__________________________________________________

"""
8. The Fibonacci sequence (part 2)

Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
"""
print("___________ESERCIZIO 8___________")

def recFib(x):
	# basic cases
	if x == 1: return 0
	if x == 2: return 1
	# recoursive call
	return recFib(x-1) + recFib(x-2)

# print all the first 20 values
for i in range(1, 21):
	print(recFib(i))
#_________________________________________________ESERCIZIO 9__________________________________________________

"""
9. The Fibonacci sequence (part 3)

Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.

Measure the execution code of the two functions with timeit (link to the doc), for example:

%timeit loopFibonacci(20)

%timeit recursiveFibonacci(20)

which one is the most efficient implementation? By how much?
"""
print("___________ESERCIZIO 9___________")

# Iterative fibonacci
def itFib(x):
	x = x-2
	if x < 0: return 0 # rerturn 0 if x < 2
	a1 = 0
	a2 = 1
	for i in range(x):
		b = a1 + a2
		a1 = a2
		a2 = b
	return a2

# Test the time used by the iteractive function
import timeit
starting_time = timeit.default_timer()
itFib(20)
print("Used time for the iterative :", timeit.default_timer() - starting_time)

# Test the time used by the recoursive function
starting_time = timeit.default_timer()
recFib(20)
print("Used time for the recoursive :", timeit.default_timer() - starting_time)
#The most efficent is the iterative one by three orders of magnitude for x = 20

#_________________________________________________ESERCIZIO 10__________________________________________________

"""
10. Class definition

Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

Create appropriate methods to get and set the length of each side

Create a method perimeter() that returns the perimeter of the polygon

Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.
"""
print("___________ESERCIZIO 10___________")

class polygon:
	# define list
	x = []
	
	# Constructor
	def __init__(self, t):
		if len(t) >= 3:
			self.x = t # a list is expected as input
		else:
			print("Error: number of components less than 3")
	
	# This method allows to get individial elements of the length of each side
	def getX(self, n): # n is the component index
		return self.x[n]
	
	# This method allows to set individial elements of the length of each side
	def setX(self, n, xi): # n is the component index, and xi is the value
		if n < len(self.x):
			self.x[n] = xi
	
	# This method return the perimeter of the polygon
	def perimeter(self):
		per = 0
		for i in range(len(self.x)):
			per = per + self.x[i]
		return per
	
	# This method return the sides of the polygon ordered
	def getOrderedSides(self, increasing):
		return tuple(sorted(self.x, reverse = not(increasing)))

# Define tuple
t = (2, 3 , 4, 1)
# Create Polygon object
a = polygon(t)
# print the perimeter of the polygon
print (a.perimeter())
# print the ordered sides of the polygon
print (a.getOrderedSides(True)) 
#_________________________________________________ESERCIZIO 11__________________________________________________

"""
11. Class inheritance

Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor.
"""
print("___________ESERCIZIO 11___________")

class rectangle (polygon):
	#Redefine constructor
	def __init__(self, t):
		if len(t) == 4 and t[0] == t[2] and t[1] == t[3]:
			self.x = t # a list is expected as input
		else:
			print("Error: not a rectangle")
	
	# This method return the area of the rectangle
	def area(self):
		return self.x[0] * self.x[1]

# Define tuple
t1 = (2, 3 , 2, 3)
# Create polygon object
a1 = rectangle(t1)
# print the area of the rectangle
print(a1.area())