"""
02ex_fundamentals
Name and surname: Mattia Sabatini
Number of matricola: 2092001
Istitutional email adress: mattia.sabatini@studenti.unipd.it
Your curriculum: single courses
"""



###########################################################################################################################################



'''
1. Global variables

Convert the function f into a function that doesn't use global variables and that does not modify the original list
'''



# Ex. 1.

print("\n\n\nEx. 1.\n")

x = 5

#Function that modifies the original list
def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed



#Function that doesn't use global variables and that does not modify the original list
def f(alist, r):
    blist = []
    for i in range(r):
        blist.append(i)
    return alist + blist

alist = [1, 2, 3]
ans = f(alist, 5)
print('\n')
print(ans)
print(alist)



###########################################################################################################################################



'''
2. List comprehension

Write the following expression using a list comprehension:

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))

'''



# Ex. 2.

print("\n\n\nEx. 2.\n")


ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

#List comprehension:
ans2 = [x for x in map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))] 
print(ans2)



###########################################################################################################################################



'''
3. Filter list

Using the filter() hof, define a function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n.
'''



# Ex. 3.

print("\n\n\nEx. 3.\n")

#Function that takes a list of words and an integer n as arguments, and returns a list of words that are shorter than n
def length_str(s,n):
    return list(filter(lambda x: len(x) < n, s))

words = ['Ciao', 'Mela', 'Monte Carlo', 'Python']
res = length_str(words,5)
print(res)



###########################################################################################################################################



'''
4. Map dictionary

Consider the following dictionary:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

Write a function that takes the above dictionary and uses the map() higher order function to return a list that contains the length of the keys of the dictionary.
'''



# Ex. 4.

print("\n\n\nEx. 4.\n")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

#Function that takes a dictionary and returns a list that contains the length of the keys of the dictionary
def length_keys(dic):
    return list(map(lambda x: len(x), dic))

res = length_keys(lang)
print(res)



###########################################################################################################################################



'''
5. Lambda functions

Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

Hint: use the method sort() and its argument key of the list data structure.
'''



# Ex. 5.

print("\n\n\nEx. 5.\n")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

#Sorts a list of tuples using a lambda function according to the alphabetical order of the first element of the tuple
language_scores.sort(key = lambda x:x[1])
print(language_scores)



###########################################################################################################################################



'''
6. Nested functions

Write two functions: one that returns the square of a number, and one that returns its cube.

Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
'''



# Ex. 6.

print("\n\n\nEx. 6.\n")

#Function that returns the square of a number
def square(x):
    return x * x

#Function that returns the cube of a number
def cube(x):
    return x * x * x

#Function that returns the number raised to the 6th power using only the two previous functions
def sixth_power(x):
    return square(x) * cube(x)

print('2 to the 6th power =',sixth_power(2))



###########################################################################################################################################



'''
7. Decorators

Write a decorator named hello that makes every wrapped function print “Hello World!” each time the function is called.

The wrapped function should look like:

@hello
def square(x):
    return x*x
'''



# Ex. 7.

print("\n\n\nEx. 7.\n")

def hello(func): # The decorator takes a function as an argument and return a wrapped function that provides additional useful properties
    def wrapper(x): # Defining the wrapped function 
        print("Hello World!")
        return(func(x)) # returns the function
    return wrapper # returns the wrapped function

@hello # Appling the decorator to the function below
def square(x): 
    return x*x

print(square(2))



###########################################################################################################################################



'''
8. The Fibonacci sequence (part 2)

Calculate the first 20 numbers of the Fibonacci sequence using a recursive function.
'''



# Ex. 8.

print("\n\n\nEx. 8.\n")

#Recursive function to calculate the Fibonacci sequence
def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

res = list(map(Fibonacci, range(1,21)))
print(res)



###########################################################################################################################################



'''
9. The Fibonacci sequence (part 3)

Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only for and while loops.

Measure the execution code of the two functions with timeit (link to the doc), for example:

%timeit loopFibonacci(20)

%timeit recursiveFibonacci(20)

which one is the most efficient implementation? By how much?
'''



# Ex. 9.

print("\n\n\nEx. 9.\n")

import timeit


#Function that calculates the first n numbers of the Fibonacci sequence using the for loop and returns a list
def loop_for_Fibonacci(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print("First 20 numbers of the Fibonacci sequence:\n", loop_for_Fibonacci(20),"\n")

print("Fibonacci sequence performed with for loops: ", timeit.timeit('loop_for_Fibonacci(20)', globals=globals()), "seconds")


#Function that calculates the first n numbers of the Fibonacci sequence using the while loop and returns a list
def loop_while_Fibonacci(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        count = 2
        while count < n:
            sequence.append(sequence[count-1] + sequence[count-2])
            count += 1
    return sequence

print("Fibonacci sequence performed with while loops:", timeit.timeit('loop_while_Fibonacci(20)', globals=globals()), "seconds")


#Recursive function to calculate the Fibonacci sequence
def recursiveFibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

print("Fibonacci sequence performed with recursive function:", timeit.timeit('map(recursiveFibonacci, range(1,21))', globals=globals()), "seconds\n")
print("=>The most efficient implementation is the one with the recursive function of around an order of magnitude with respect to the for and while loops")



###########################################################################################################################################



'''
10. Class definition

Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

    Create appropriate methods to get and set the length of each side

    Create a method perimeter() that returns the perimeter of the polygon

    Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.
'''



# Ex. 10.

print("\n\n\nEx. 10.\n")

class polygon:
    
    # Definition of the class attributes
    x = []
    
    # Definition of the constructor, it takes a tuple as input that contains the length of each side
    def __init__(self, components):
        if len(components)>=3:
            self.x = list(components) # a tuple is expected as input
        else:
            print("Error: the tuple should contain at least 3 items.")
    
    # This method allows to get individial elements of the 'x' attribute 
    def getX(self, n): # n is the component index
        return self.x[n]
    
    # This method allows to get all elements of the 'x' attribute 
    def getAllX(self):
        return tuple(self.x)
    
    # This method allows to set individial elements of the 'x' attribute 
    def setX(self, n, xi): # n is the component index, and xi is the value
        if n < len(self.x):
            self.x[n] = xi
    
    # This method returns the perimeter of the polygon
    def perimeter(self):
        sum_sides = 0
        for i in range(len(self.x)):
            sum_sides += self.x[i]
        return sum_sides
    
    #This method returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
    def getOrderedSides(self, increasing):
        if increasing == True:
            self.x.sort()
            return tuple(self.x)
        elif increasing == False:
            self.x.sort(reverse=True)
            return tuple(self.x)

trap = polygon((4, 2, 3, 2))


print("Polygon:",trap.getAllX())
print("Perimeter =",trap.perimeter())
   
print("\ngetOrderedSides(increasing = True):", trap.getOrderedSides(True))
print("getOrderedSides(increasing = False):",trap.getOrderedSides(False))



###########################################################################################################################################



'''
11. Class inheritance

Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

    Create a method area() that returns the area of the rectangle.

Test the rectangle class by creating an instance and passing an appropriate input to the constructor.
'''



# Ex. 11.

print("\n\n\nEx. 11.\n")

class rectangle(polygon): # class 'rectangle' inherits from class 'polygon'
    
    # The constructor is used to make sure that the input data is consistent with the geometrical properties of a rectangle
    def __init__(self, components):
        
        #Check that the sides are equal to 4
        if len(components) == 4:
            self.x = list(components)
            
            #Check that there are two pairs of equal sides
            equal_sides = 0
            for i in range(len(self.x)):
                for j in range(i + 1, len(self.x)):
                    if self.x[i]==self.x[j]:
                        equal_sides += 1
            if equal_sides!=2:
                print("Error: a rectangle has two pairs of equal sides.")
        else:
            print("Error: a rectangle has 4 sides. Enter the correct number of sides.")
    
    # Method area() that returns the area of the rectangle and that only belong to the child class
    def area(self):
        for i in range(len(self.x)):
            for j in range(i + 1, len(self.x)):
                if self.x[i]!=self.x[j]:
                    return self.x[i]*self.x[j]

rect = rectangle((2,1,1,2))

print("Rectangle:",rect.getAllX())
print("Area =",rect.area())

#pentagon = rectangle((1,1,1,1,1))
#square = rectangle((1,1,1,1))



