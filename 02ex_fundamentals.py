
import timeit

"""
Exercice 1 : GLOBAL VARIABLES
"""
print("Exercice 1 : GLOBAL VARIABLES \n")
#x = 5
#we don't access the value of the variable outside the function so we don't have global variable

def f(alist):
    #we create a copy of alist to work on so we don't modify alist
    copy_alist = list(alist)
    for i in range(5):
        #we modify the copy of alist
        copy_alist.append(i)
    return copy_alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)

"""
Exercice 2 : LIST COMPREHENSION
"""
print("\nExercice 2 : LIST COMPREHENSION \n")
# list comprehension
print([x*x for x in range (10) if x % 2 == 1])
#using map and filter
ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)

"""
Exercice 3 : FILTER LIST
"""
print("\nExercice 3 : FILTER LIST \n")
list_word = ['cat','snowman','compass','cow','lemon','pen']

#filter : do not take a list but a true or a false
def count(l,n):
    return True if len(l) <= n else False

#use lambda to pass two values to a function using filter
print(list(filter(lambda x: count(x, 3), list_word)))

"""
Exercice 4 : MAP DICTIONARY
"""
print("\nExercice 4 : MAP DICTIONARY \n")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

#Return a list that contains the length of the keys of the dictionary
def map_dictionary(l):
    return (map(lambda x : len(x), lang))
    
print(list(map_dictionary(lang)))

"""
Exercice 5 : LAMBDA FUNCTIONS
"""
print("\nExercice 5 : LAMBDA FUNCTIONS \n")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
#if we write (key= lambda x: x[1] we will sort the tuple according to the second element so numbers)
language_scores.sort(key= lambda x: x[0])
print(language_scores)


"""
Exercice 6 : NESTED FUNCTIONS
"""
print("\nExercice 6 : NESTED FUNCTIONS \n")
#function that returns the square of a number 
def square(x):
    return x * x
#function that returns the cube of a number
def cube(x):
    return x * x * x
#function the returns the number raised to the 6th power
def sixthPower(x):
    return square(x)*cube(x)

res = sixthPower(2)
print(res)

"""
Exercice 7 : DECORATORS
"""
print("\nExercice 7 : DECORATORS \n")
#defining a decorator
def hello(func):
    def wrapper(x):
        print("Hello World!")
        res = func(x)#runs the function and print the result
        print(res)
    return wrapper

@hello
def square(x):
    return x*x
square(2)
square(6)

"""
Exercice 8 : THE FIBONACCI SEQUENCE (PART 2)
"""
print("\nExercice 8 : THE FIBONACCI SEQUENCE (PART 2) \n")
#Fn = F(n-1) + F(n-2)
#seed values : f0 = 0, f1 = 1

def fibonacci(n):
    #if n<=1 the values are 0 is n=0 or 1 if n=1 (so n)
	if n<=1:
		return n
	else: #we call the function itself
		return(fibonacci(n-1) + fibonacci(n-2))

#to display all the numbers in a list
def recursiveFibonacci(n):
    print([fibonacci(n) for n in range(n)])

recursiveFibonacci(20)

"""
Exercice 9 : THE FIBONACCI SEQUENCE (PART 3)
"""
print("\nExercice 9 : THE FIBONACCI SEQUENCE (PART 3) \n")

def loopFibonacci(n):
    #Fn = F(n-1) + F(n-2)
    #seed values : f0 = 0, f1 = 1
    f = [0,1]
    
    #We have the first two values => we start at the third value
    for i in range(2, n):
        #we add to the list the result :
        f.append(f[i-1] + f[i-2])
    return(f)

#Time it takes to execute the recursive Fibonacci
resultat1 = timeit.timeit('recursiveFibonacci(20)', globals=globals(), number=1)
print('Recursive Fibonnacci : ',resultat1)

#Time it takes to execute the loop Fibonacci
resultat2 = timeit.timeit('loopFibonacci(20)', globals=globals(), number=1)
print('Loop Fibonnacci : ',resultat2)

#Difference between recursive and loop Fibonacci
print('Difference :',resultat1-resultat2)

'''
Loop algorithms are more efficient in terms of time. Indeed, it takes only approximetly 8e-06 secondes for the loop algorithm
to execute against 5e-3 secondes for the recursive algorithm. Indeed, it takes time for the recursive algorithm to make the calls to itself
'''

"""
Exercice 10 : CLASS DEFINITION
"""
print("\nExercice 10 : CLASS DEFINITION \n")
#Class definition

class polygon:
    """
    Description of the class : get and set lenght of each side of a polygon
    calculate the perimeter of the polygone 
    returns a tuple with the lenght of the sides arranged in increasing or decrasing order
    """

    #Definition of the class attributes, which are common for all instances
    x = ()

    #Definition of the Constructor
    def __init__(self, components):
        self.x = components
    
    #Definition of the destructor
    def __del__(self):
        print("Destruction of the polygon")

    #Definition of the methods 

    #print the polygon
    def printPolygon(self):
        t = []
        for i in self.x:
            t.append(i)
        print(t)

    #get Lenght of the side n of the polygon
    def getLenght(self,n):
        if (n < len(self.x)):
            return self.x[n]
        else:
            return ('The id of the lenght does not exist')

    #set Lenght of the side n of the polygon
    def setLenght(self,n,val):
        if (n < len(self.x)):
            y = list(self.x)
            y[n] = val
            self.x = tuple(y)
        else:
            return ('The id of the lenght does not exist')

    #returns the perimeter of the polygon
    def perimeter(self):
        res = 0
        for i in self.x:
            res = res + i
        return res

    #returns a tuple containing the lenght of the sides arranged in increasing or descrasing order
    def getOrderedSides(self, increasing):
        if (increasing == True):
            y = list(self.x)
            y.sort()
            self.x = tuple(y)
        elif (increasing == False):
            y = list(self.x)
            y.sort(reverse=True)
            self.x = tuple(y)

a = polygon((22,7,5))
print('Polygon : ')
a.printPolygon()
print('Lenght of the 3nd side : ', a.getLenght(2))
print('Set lenght of the 3nd side to 10. \nPolygon : ')
a.setLenght(3,10)
a.printPolygon()
print('Perimeter of the polygon',a.perimeter())
print('Order the lenght of the sides arranged in increasing order : ')
a.getOrderedSides(increasing=True)
a.printPolygon()

"""
Exercice 11 : CLASS INHERITANCE
"""
print("\nExercice 11 : CLASS INHERITANCE \n")
class rectangle(polygon): #class rectangle that inherits from 'polygon'
    #The constructor as to be redefined 
    def __init__(self, components):
        #here, we make sure that 4 variables are entered 
        if len(components) == 2:
            components = components + components
            self.x = components
        else:
            print("Error : number of components is not 2 (width and height)")
    
    #calculate the area of the rectangle : width * height
    def area(self):
        area = 1
        n = 0
        y = list(self.x)
        #we just take the first two values to have the width and the height
        for i in y[:2]:
            area = area * i
        return area

r = rectangle((3,4))
print("Rectangle : ")
r.printPolygon()
print("Area of the rectangle :", r.area())
print("Perimeter of the rectangle :", r.perimeter())