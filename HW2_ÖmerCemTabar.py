"""
Author : Ömer Cem Tabar
Exercise Document 02 Solution File

This file only includes the codes that is required to solve the questions
You can also check the outputs from the notebook

"""

"""
1\. **Global variables**
"""
x = 5
def f(alist):
    temporary = x
    a_copy_list = [element for element in alist]
    for i in range(temporary):
        a_copy_list.append(i)
    return a_copy_list

alist = [1, 2, 3] 
ans = f(alist)
print(ans)
print(alist) # alist has been changed

"""
2\. **List comprehension**

"""

#`ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`
ans = [x ** 2 for x in range(10) if x%2 == 1]
print(ans)
"""
3\. **Filter list**

"""
example_word_list = ['This', 'is', 'a', 'string', 'with', 'words']

def ShorterWordsInTheList(lst,n):
    return list(filter(lambda x: len(x) < n ,lst))

filteredList = ShorterWordsInTheList(example_word_list,3)
print(filteredList)

"""
4\. **Map dictionary**

"""
def LengthCalculation(x):
    lengthList = list(map(lambda length: len(length),x.keys()))
    return lengthList

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
lst = LengthCalculation(lang)
print(lst)

"""
5\. **Lambda functions**

"""
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda tuple:tuple[0])
print(language_scores)

"""
6\. **Nested functions**

"""
def ReturnSquare(a):
    return a**2

def ReturnCube(a):
    return a**3

def ReturnSixth(a):
    return ReturnCube(ReturnSquare(a))

print(ReturnSixth(5))

"""
7\. **Decorators**

"""
def hello(func):
    def wrapper(a):
        result = func(a)
        print("Hello World!")
    return wrapper


@hello
def square(x):
    return x*x

square = hello(square)
square(5)

"""
8\. **The Fibonacci sequence (part 2)**

"""
def recursiveFibonacci(n):
    if n == 0:  #First element of the Fibonacci Sequence (Zeroth Case)
        return n
    elif n == 1: #Second element of the Fibonacci Sequence (First Case)
        return n
    else: # Recursively call the rest, calculate and return
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)

recursiveFibonacci = [recursiveFibonacci(n) for n in range(20)]
print(recursiveFibonacci)


"""
9\. **The Fibonacci sequence (part 3)**

"""
def loopFibonacci(n):
    FibonacciNumbers = []
    counter = 0
    while counter < n:
        if counter == 0:
            FibonacciNumbers.append(counter)
            counter += 1
        elif counter == 1:
            FibonacciNumbers.append(counter)
            counter += 1
        else:
            FibonacciNumbers.append(FibonacciNumbers[counter-2] + FibonacciNumbers[counter-1])
            counter += 1
    return FibonacciNumbers

%timeit loopFibonacci(20)

def recursiveFibonacci(n):
    if n == 0:  #First element of the Fibonacci Sequence (Zeroth Case)
        return n
    elif n == 1: #Second element of the Fibonacci Sequence (First Case)
        return n
    else: # Recursively call the rest, calculate and return
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)

recursive = [recursiveFibonacci(n) for n in range(20)]
%timeit recursiveFibonacci(20)

"""
10\. **Class definition**

"""
# Class definition
import math

class polygon:
    # Definition of the class attributes, which are common for all instances of the same class
    #In our case only attribute is a tuple that contains the length of the sides of the polygon
    sideLengths = ()
    
    # Definition of the Constructor, a special method that is called every time a new object is created
    # The first argument of the constructor (and also for all other methods in the class) is the instance itself
    def __init__(pol, lengthTuple):
        pol.sideLenghts = lengthTuple
        
        
    # Definition of the methods
    
    # This method allows to get the length of a side with a specific index that attribute 'sideLenghts'
    def GetLengthOfASide(pol, index): 
        return pol.sideLenghts[index]
    
    # This method allows to get the length of all sides that attribute 'sideLenghts'
    def GetLengthOfAllSides(pol): 
        return pol.sideLenghts
    
    # This method allows to set the length of each side that attribute 'sideLenghts'
    def setValue(pol, index, value):
        new_list = list(pol.sideLenghts)
        new_list[index] = value
        sideLengths = tuple(new_list)
        return sideLengths
    
    # This method allows to return the perimeter of the polygon
    def perimeter(pol): 
        perimeter = 0
        for lenght in pol.sideLenghts:
            perimeter += lenght
        return perimeter
    
    # This method allows to return the ordered list of the attribute 'sideLenghts'
    def getOrderedSides(pol,increasing): 
        if increasing == True:
            new_list = [element for element in pol.sideLenghts]
            new_list.sort()
            tuple_list = tuple(new_list)
            return tuple_list
        else:
            new_list = [element for element in pol.sideLenghts]
            new_list.sort(reverse = True)
            tuple_list = tuple(new_list)
            return tuple_list

# End of the class definition

a = polygon((5,8,12,6,7,19))
print("Perimeter of the polygon is: " + str(a.perimeter()))
print("Side Lengths of the polygon in increasing order: " + str(a.getOrderedSides(increasing=True)))
print("Side Lengths of the polygon in decreasing order: " + str(a.getOrderedSides(increasing=False)))

"""
11\. **Class inheritance**

"""

class rectangle(polygon): 
    
    # The constructor here is optional, and can be inherited from the parent class if omitted
    def __init__(rec, sides):
        if len(sides) == 4:
            lengthElection = []
            for i in sides:
                if i not in lengthElection:
                    lengthElection.append(i)
            if len(lengthElection) == 2:
                rec.sideLengths = sides # a list is expected as input
            else:
                print("Creation Error: Sides that are given is not supplying rules of a rectangle")
        else:
            print("Error: number of sides are not 4")
    def area(rec):
        lengthElection = []
        for i in rec.sideLengths:
            if i not in lengthElection:
                lengthElection.append(i)
        area = lengthElection[0] * lengthElection[1]
        return area

b = rectangle((5,2,2,5))    

b_area = b.area()
print("Area of the rectangle: " + str(b_area))