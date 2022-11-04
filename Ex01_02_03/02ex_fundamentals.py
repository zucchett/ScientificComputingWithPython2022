
#Professor's code

x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

#Task 1
#my code which avoid changing list

x = 5
def f(alist):
    alist=[i for i in range(x)]
    return alist

alist = [1, 2, 3]
ans = f(alist)
#List created in the function
print(ans)
#Original non-changed list
print(alist) 
#########################################################################

#Task 2
#Rewritten expression ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))
odd_squares=[x*x for x in range(10) if x%2==1]
print(odd_squares)

#########################################################################

#Task 3

def filter_length_of_words(list1,n):
    return list(filter(lambda i : len(i)<n, list1 ))

list1=['jajajaj','haha','tri','emilija','radi','zadatke']
print(filter_length_of_words(list1,5))

#########################################################################

#Task 4

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}


def len_of_keys(x):
    list1=list(x.keys())
    list2=[]
    
    for i in map(lambda y: len(y),list1):
        list2.append(i)
    return list2    
    

print(len_of_keys(lang))

#########################################################################

#Task 5

#Alphabetic sort of list of tuple based on the keys
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key= lambda x : x[0])
print(language_scores)
#########################################################################

#Task 6
def square(num):
    return num*num

def cube(num):
    return num*num*num

def powSix(num):
    return cube(square(num))

print(powSix(2))

#########################################################################

#Task 7

#Task 7
def hello(func):
    def wrapper(x):
        
        func(x)
        print('Hello World!')
    return wrapper

@hello
def square(x):
    return x*x

square(5)

#########################################################################

#Task 8
#Recursive Fibonacci

def fibonacci_recursive(n):
    if n in {0,1}:
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2) 

print([fibonacci_recursive(n) for n in range(20)])

#########################################################################
#Task 9

#Recursive Fibonacci
import timeit
code1="""
def fibonacci_recursive(n):
    if n in {0,1}:
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2) 
"""
print(timeit.timeit(stmt=code1, number=1000000))
#the time for Recursive Fibonacci:0.1330652


#Looped Fibonacci

code2="""
def loopFibonacci(n):
    i = 1
    num1, num2=0,1
    while(i<=n):
        
        print(num1)
        next=num1+num2
        
        num1=num2
        num2=next
        i+=1
"""

print(timeit.timeit(stmt=code2, number=1000000))
#Time for the Looped Fibonacci: 0.0433113

#Comment on the Task 9

#The more efficient is looped Fibonacci in this case for ~ 0.09
#It just proofs that recursive algorithms need more time to execute due algorithm complexity


#########################################################################

#Task 10

#Definition of the class Polygon 

import math

class Polygon:
    #Definition of the polygon class atributes, all instances of the class polygon has atribute sides
    
    sides=()
    
    #Definition of the constructor which is called everytime new instance of the Polygon class is created
    
    def __init__(self, components):
        if len(components)>=3:
            self.sides=components 
        else:
            print('It is not polygon, please try to increase number of sides!')
    
    # Definition of the destructor, but it is often omitted
    def __del__(self):
        print("Goodbye")
        
    #Getter methode    
    def get(self):
        return self.sides
    
    
    # This method allows to get individial elements of the 'sides' attribute 
    def getX(self, n): # n is the component index
        return self.sides[n]
    
    # This method allows to set individial elements of the 'sides' attribute 
    def setX(self, n, xi): # n is the component index, and xi is the value
        if n < len(self.sides):
            tmp=list(self.sides)
            tmp[n]=xi
            self.sides=tuple(tmp)
            
    #Create a method perimeter
    
    def perimeter(self):
        sum=0
        for side in self.sides:
            sum=sum+side
        return sum    

    #Method getOrderedSides
    
    def getOrderedSides(self, increasing=True):
        tmp=list(self.sides)
        tmp.sort(reverse=not(increasing))
        return tmp
    
#Creating instances of the class Polygon

#creating an instances that is not a Polygon
x1=Polygon((2,4))

#creating Polygon 

x2=Polygon((3,5,6,4))
print("Perimeter of the polygon: ", x2.perimeter())
print("Sorted sides of the polygon:", x2.getOrderedSides(increasing=True))
##########################################################################

#Task 11

class Rectangle(Polygon): #class Rectangle inherits class Polygon
        
    def __init__(self, components):
        if len(components)==4 and components[0]==components[1] and components[2]==components[3]:
            self.sides=components 
        else:
            print('Error: Check the number of sides or their length! Sides have to be added in format aabb!')  
    
    def area(self):
        return self.getX(0)*self.getX(2)
#Creating instances of the class Rectangle

a=Rectangle((2,2,3,3))
print(a.area())

s=Rectangle((2,4,5,3))
x=Rectangle((1,2,3))        