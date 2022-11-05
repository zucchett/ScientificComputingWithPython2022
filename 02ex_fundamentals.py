"""
_____________________________ ESERCIZIO 1 _____________________________

Global variables

Convert the function into a function that doesn't use global variables 
and that does not modify the original list

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

def f(alist):
	x =5;  #x exists now only inside the function
	alist = [1,2,3]; 
	for i in range(x):
		alist.append(i)
	return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist hasn't been changed


"""
_____________________________ ESERCIZIO 2 _____________________________

List comprehension

Write the following expression using a list comprehension:

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))


"""

#ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))) 
#print(ans)

#print the squares with odd base < 10

anslist = [x**2 for x in range(10) if (x % 2 == 1)]
#print(anslist)


"""
_____________________________ ESERCIZIO 3 _____________________________  

Using the filter() hof, define a function that takes a list of words and an 
integer n as arguments, and returns a list of words that are shorter than n.


"""

n = 6; 
#example of a list of words
words = ["c", "ci", "cia", "ciao", "ciaoc", "ciaoci", "ciaocia", "ciaociao", "b", "bu", "buo", "buon", "buong", "buongi", "buongio", "buongior", "buongiorn", "buongiorno"] 


# function with one input
#def is_shorter(word):   #function that checks if the length of a given word is shorter than n or not
#	if (len(word) < n): return True
#	else: return False

#s_words = list(filter(is_shorter, words))
#print(s_words)



#function with two inputs
def is_shorter(word, n):
	if len(word)< n: return True
	else: return False

words_s = list(filter(lambda words_f: is_shorter(words_f, n), words))
print(words_s)



"""
_____________________________ ESERCIZIO 4 _____________________________

Consider the following dictionary:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

Write a function that takes the above dictionary and uses the map() 
higher order function to return a list that contains the length of the 
keys of the dictionary.


"""

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7} #given dictionary

def keyLen(key):       #function that calculate the length of a key
	return len(key)

lenKeys = list(map(keyLen, lang)) #apply keyLen at every element of the dictionary
print(lenKeys)


"""
_____________________________ ESERCIZIO 5 _____________________________    

Lambda functions

Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

Hint: use the method sort() and its argument key of the list data structure.


"""

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort( key = lambda tup: tup[0] ) #use sort on the key (first element of the tuples) of the list

print(language_scores)





"""
_____________________________ ESERCIZIO 6 _____________________________

Nested functions

Write two functions: one that returns the square of a number, and one that returns its cube.
Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.


"""

def square(n) : 
	return n**2 #return square of n
def cube(n) :
	return n**3 #return cube of n
def sixthPower(n) :
	return cube(square(n)) #use the power-to-power property to calculate the sixth power of n


"""
_____________________________ ESERCIZIO 7 _____________________________

Decorators

Write a decorator named hello that makes every wrapped function print 'Hello World!' each time the function is called.
The wrapped function should look like:

@hello
def square(x):
    return x*x


"""

def hello(func) :   #define decorator
    def wrapper(self) : 
        print('Hello World!') #print 'Hello World!' before invoking the function
        return func(self) #lauch the function with its argument
    return wrapper


@hello
def square(x):
    return x*x

print(square(2))


"""
_____________________________ ESERCIZIO 8 _____________________________

The Fibonacci sequence (part 2)

Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.


"""

def recFib(x) :
    #define basic cases
    if x == 0 : 
        return 0
    if x == 1 :
        return 1
    #recursive call
    else : 
        return recFib(x-1) + recFib(x-2)


for i in range(21) :
    print(recFib(i))



"""
_____________________________ ESERCIZIO 9 _____________________________ 

The Fibonacci sequence (part 3)

Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.
Measure the execution code of the two functions with timeit (link to the doc), for example:

%timeit loopFibonacci(20)
%timeit recursiveFibonacci(20)

Which one is the most efficient implementation? By how much?


"""

import timeit 

def iterFib(n) : #fibonacci iterativo
    x = 0
    y = 1
    for i in range(n) :
        x, y = y, x + y
    return x

#recursive
starting_time = timeit.default_timer() 
recFib(20)
finish_time = timeit.default_timer()

print('Recoursive execution time: ')
print(finish_time - starting_time)

#iterative
starting_time = timeit.default_timer()
iterFib(20)
finish_time = timeit.default_timer()

print('Iterative execution time: ')
print(finish_time - starting_time)


# the iterative one is the most efficient impletentation by three orders of magnitude


"""
_____________________________ ESERCIZIO 10 _____________________________ 

Class definition

Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. 
The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

Create appropriate methods to get and set the length of each side
Create a method perimeter() that returns the perimeter of the polygon
Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.


"""

class Polygon :
    ''' this class create polygons given the length of each side '''
    x = []

    #constructor
    def __init__(self, lengths) :
        if( len(lengths) >= 3 ) :
            self.x = lengths #a tuple that contains the length of each side is expected as input
        else :
            print('Error, polygons must have at least 3 sides')   

    #this method allow to get the length of the required side
    def getLength(self, n) :
        return self.x[n]

    #this method allow to set the length of the required side
    def setLength(self, v, n) : #n index thet identify the side, v new value to set for that side
        if n < len(self.x) : #check if the index is included
            self.x[n] = v

    #this method return the perimeter of the polygon
    def perimeter(self) :
        p = 0
        for i in range(len(self.x)) :
            p = p + self.x[i]
        return p

    #this method allow to sort the sides of the polygon
    def getOrderedSides(self, increasing) :
        return sorted(self.x, reverse = not(increasing))

    
#test
lp = (3, 6, 7, 12, 19,) #tuple of lengths
pol = Polygon(lp) #create object polygon

print(pol.perimeter())
print(pol.getOrderedSides(True))



"""
_____________________________ ESERCIZIO 11 _____________________________ 

Define a class rectangle that inherits from polygon. 
Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

Create a method area() that returns the area of the rectangle.
Test the rectangle class by creating an instance and passing an appropriate input to the constructor.


"""

class Rectangle (Polygon):

	#Redefine constructor
	def __init__(self, l):
		if len(l) == 4 and l[0] == l[2] and l[1] == l[3] :
			self.x = l # a tuple is expected as input
		else:
			print("Error: not a rectangle")
	
	# This method return the area of the rectangle
	def area(self):
		return self.x[0] * self.x[1]

# test
lr = (7, 3 , 7, 3,) #tuple of lengths
ret = Rectangle(lr) #create rectangle object

print(ret.area())

