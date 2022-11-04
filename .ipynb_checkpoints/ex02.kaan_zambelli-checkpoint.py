""" 

Q1 

"""

x = 5

def f(alist):
    temp = x
    blist = [element for element in alist]
    for i in range(temp):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed


""" 

Q2

""" 

ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)

"""

Q3 

""" 

random = ["ashdasdaa", "ldfklskfaf", "jahdsjad", "abc", "aa", "c", "abcdefg"]
def ShorterThan(lst,n):
    shorter_list = list(filter(lambda x: len(x) < n,lst))
    return shorter_list

lst = ShorterThan(random,7)
print(lst)

"""

Q4 

""" 

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
def LengthOfKeys(dic):
    lst = list(map(lambda x: len(x) , dic.keys()))
    return lst
lst = LengthOfKeys(lang)
print(lst)


""" 

Q5 

""" 

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x: x[0])
print(language_scores)


"""

Q6

"""

def square(x): 
    
    return x*x 
    
def cube(x):   
    
    return x*x*x

def sixth(x): 
    
    return square(cube(x))
    
   
    
    
""" 

Q7

""" 

def hello(func):
    def wrapper(x):
        print("Hello World!")
        func(x) # runs the function
       
    return wrapper

@hello
def square(x):
    return x*x
    
square = hello(square)
square(31)


""" 

Q8 

""" 

def fibonacci_recursive(n):
    if n <= 1 :
        return n 
    else:
        return(fibonacci_recursive(n-1) + fibonacci_recursive(n-2))
numbers= 20 
for i in range(numbers):
    print(fibonacci_recursive(i))

    
""" 

Q9 

"""

def loopFibonacci(n):
    x = 0
    y = 1
    z = 0 
    fibonacci = []
    fibonacci.append(x)
    fibonacci.append(y)

    z = x + y 
    n = n - 2 

    while n > 0:
        fibonacci.append(z)
        x = y
        y = z
        z = x+y
        n = n-1
    return fibonacci
%timeit loopFibonacci(20)
#print("The Fibonacci Sequence : " +  str(loopFibonacci(20)))


def recursiveFibonacci(n):
    if n <= 1 :
        return n 
    else:
        return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))
numbers= 20 
%timeit recursiveFibonacci(20)

for i in range(numbers):
    print(recursiveFibonacci(i))

"""

Q10 

""" 

import math

class polygon:
    
    sides = ()
    
    def __init__(self, components):
        self.sides = components 
    
    def getSides(self): 
        return self.sides
    
    def getSidesWithIndex(self, n):
        return self.sides[n]
    
    def setSides(self, n, value): 
        lst = list(self.sides)
        lst[n] = value
        tup = tuple(lst)
        self.sides = tup
        return self.sides
    
    def perimeter(self):
        perimeter_sum = 0
        for i in range(0,len(self.sides)):
            perimeter_sum = perimeter_sum + self.sides[i]
        return perimeter_sum
    
    def getOrderedSides(self,increasing):
        if increasing == True:
            lst = list(self.sides)
            lst.sort(reverse=False)
            tup = tuple(lst)
            self.sides = tup
            return self.sides
        else:
            lst = list(self.sides)
            lst.sort(reverse=True)
            tup = tuple(lst)
            self.sides = tup
            return self.sides
        
pol = polygon((4,3,5,6,7,3,2,8))
per = pol.perimeter()
print(per)

ordered_increasing = pol.getOrderedSides(increasing=True)
print(ordered_increasing)

ordered_decreasing = pol.getOrderedSides(increasing=False)
print(ordered_decreasing)

settedPol = pol.setSides(2,10)
print(settedPol)

indexOfSide = pol.getSidesWithIndex(2)
print(indexOfSide)

allSides = pol.getSides()
print(allSides)        
        
""" 

Q11 

""" 

class rectangle(polygon):
    def __init__(self, components):
        if len(components) == 4:
            counterCheck = 0
            for element in components:
                if element == components[0]:
                    counterCheck = counterCheck + 1
                else:
                    counterCheck = counterCheck
            if counterCheck == 2:
                print("You have successfully created a rectangle!")
                self.sides = components
            else:
                print("You could not have created rectangle")
        else:
            print("Error: number of components is not 4")
    
    def area(self):
        sides = []
        for element in self.sides:
            if element not in sides:
                sides.append(element)
        return sides[0] * sides[1]
    
    
rec = rectangle((2,4,4,2))
area = rec.area()
print(area)