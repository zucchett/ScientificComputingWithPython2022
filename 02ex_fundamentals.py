# ********** Question 1 **********
import math

print("Question 1")
x = 5
def f(alist):
    alist = list(alist) # Creates a copy
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist)


# ********** Question 2 **********

print("Question 2")
ans = [x**2 for x in range(10) if x % 2 == 1]
print(ans)


# ********** Question 3 **********

print("Question 3")
def checkLength(word, n): # checks if the length of word is smaller than n
    if len(word) < n:
        return True
    return False

def filterList(words, n): # filter traverses through the list and puts every word into checkLength function
    filtered_list = list(filter(lambda word: checkLength(word, n), words))
    return filtered_list


l = ['KinderBuenoMini', 'ChockfullONuts', 'SanBenedetto', 'Rizla', 'LuckyStrike', 'Ezgi']
print("Initial list: ", l)
print("Filter by 12")
print("Filtered list: ", filterList(l, 12))


# ********** Question 4 **********

print("Question 4")
def lengthFunc(a):
    return len(a)

def mapDictionary(x):
    new_list = map(lengthFunc,x)
    return new_list

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

length_list = mapDictionary(lang)
print(length_list)
print(list(length_list))


# ********** Question 5 **********

print("Question 5")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = lambda x: x[0]) # lambda function returns the first index and sort takes that as key
print(language_scores)


# ********** Question 6 **********

print("Question 6")
def squareFunc(a):
    return a**2

def cubeFunc(a):
    return a**3

def sixthFunc(a):
    return squareFunc(cubeFunc(a))

print(sixthFunc(4))


# ********** Question 7 **********

print("Question 7")
def hello(func):
    def wrapper(x):
        print("Hello World.")
        print(func(x)) # runs the function based on the argument x
    return wrapper

@hello
def square(x):
    return x*x

square(4)


# ********** Question 8 **********

print("Question 8")
def loopFibonacci(x):
    term1 = 0
    term2 = 1
    count = 0
    while count < x:
        print(term1)
        termlast = term1 + term2
        # update values
        term1 = term2
        term2 = termlast
        count += 1

def recursiveFibonacci(n): # every iteration calls for the same function twice to find two preceeding number
   if n <= 1:
       return n
   else:
       return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))

n = 20
print('recursive: ')
for i in range(n):
    print(recursiveFibonacci(i))

print('loop: ')
loopFibonacci(n)

# ********** Question 9 **********

import timeit
input('enter anything to continue to speed test')
print('Question 9')
start_time = timeit.default_timer()
print('start time: ', start_time)
loopFibonacci(20)
print("difference: ", timeit.default_timer() - start_time) # checks the time by recording the difference between start time and current time
start_time = timeit.default_timer()
print('start time: ', start_time)
for i in range(20):
    print(recursiveFibonacci(i))
print("difference: ", timeit.default_timer() - start_time)

## Loop is more efficient and faster than the recursive version

# ********** Question 10 **********

print('Question 10')
class polygon:

    sides = ()

    def __init__(self, components):
        self.sides = components
    
    def perimeter(self):
        result = sum(self.sides)
        return result
    
    def getOrderedSides(self, increasing):
        if increasing:
            result = sorted(self.sides)
            return result
        return self.sides

def getSides(n):
    sides = []
    for i in range(n):
        print("Enter the length of side ", i+1, " ")
        sides.append(int(input()))
    sides_tup = tuple(sides)
    return sides_tup

n = int(input("Enter the number of sides"))
if n >= 3:
    sides_tuple = ()
    sides_tuple = getSides(n)
    a = polygon(sides_tuple)
    print(a.perimeter())
    print(a.getOrderedSides(True))
else:
    print("Number of sides should be greater than 3")

# ********** Question 11 **********

print('Question 11')
class rectangle(polygon):

    def __init__(self, components):
        temp_set = set(components)
        if len(components) == 4 :
            if( (components[0] == components[1] and components[2] == components[3]) or 
            (components[0] == components[2] and components[1] == components[3]) or
            (components[0] == components[3] and components[1] == components[2])):
                self.sides = components
        else:
            print("Error: not a rectangle")
    
    def area(self):
        temp_set = set(self.sides)
        unique_sides = tuple(temp_set)
        if len(unique_sides) == 1:
            result = unique_sides[0] ** 2
        else:
            result = unique_sides[0] * unique_sides[1]
        return result

b = rectangle((4, 6, 4, 6))
print(b.area())
print(b.perimeter())
print(b.getOrderedSides(True))