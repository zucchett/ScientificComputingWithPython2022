
import timeit
# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `02ex_fundamentals.py`.
# 
# In case you need multiple files, name them `02ex_fundamentals_es01.py`, `02ex_fundamentals_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `02ex_fundamentals`. 
# 
# The exercises need to run without errors with `python3`.


#Ex 1 ===========================================================================================================================================================
print("Ex 1 **Global variables**")
# 
# Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list


x = 5

def f(alist):
    for i in range(x):
        alist.append(i)
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed




def funct(numlist: list, number: int | float) -> list:
   ''' Accepts a list and a number.\n
   Returns a list which has as its element(s)
   - the element(s) of the original list
   - the number(s) in the range between 0 and number-1\n
 Ex. funct([1,2,3], 3) => [1,2,3,0,1,2] '''

   ans = numlist.copy()           #shallow copy
   for num in range(number):
      ans.append(num)
   print(f"lista: {numlist}")
   return ans
   

print(funct([1, 2, 3, 7, 90], 5))



#Ex 2 ==========================================================================================================================================
print("Ex 2 **List comprehension**")
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`


ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)



nums = [n*n for n in range(10) if n%2==1]
print(nums)

#Ex 3 ========================================================================================================================================================================
print("3 **Filter list**")
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.


def lenwords_less_than_n(wordlist: list, n: int) -> list:
    return list(filter(lambda x: len(x) < n, wordlist))

print(lenwords_less_than_n(["alvo", "stella", "mestolo", "bollitore", "turlupinare"], 8))


#Ex 4 ===========================================================================================================================================================================
print("Ex 4 **Map dictionary**")
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.


def lenkeys(dictionary: dict) -> list:
    return list(map(lambda x: len(x), dictionary.keys()))


lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print(lenkeys(lang))



#Ex 5 ==============================================================================================================================================================================
print("5 **Lambda functions**")
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key = lambda x: x[0])
print(language_scores)



#same thing as above, but using the sorted built-in function
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
print(sorted(language_scores))


#Ex 6 =================================================================================================================================================
print("6 **Nested functions**")
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.



def square(number):
    return number*number

def cube(number):
    return number**3



def sixthpow(number):
    return cube(square(number))

print(3**6,sixthpow(3))

# Ex 7 =====================================================================================================================================
print("7 **Decorators**")
# 
# Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.
# 
# The wrapped function should look like:
# 
# ```python
# @hello
# def square(x):
#     return x*x
# ```



def hello(func):
    def inner(*args, **kwargs):
        
        print("Hello World!")

        return func(*args, **kwargs)

    return inner

@hello
def square(x):
    return x*x



print(square(5))


#Ex 8 ====================================================================================================================================================
print("8 **The Fibonacci sequence (part 2)**")
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.


def recursiveFibonacci(index,a = 0, b = 1, lista = []):
    '''accepts an index and returns a list with the fibonacci sequence until that index'''
    
    if index == len(lista) :
        lista.insert(0,0)
    
    else:
        a, b= b,a+b
        lista.append((a))
        recursiveFibonacci(index,a,b,lista)
    return lista

print(recursiveFibonacci(19))


#Ex 9 =========================================================================================================================================================
print("9 **The Fibonacci sequence (part 3)**")
# 
# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
# 
# Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
# 
# `%timeit loopFibonacci(20)`
# 
# `%timeit recursiveFibonacci(20)`
# 
# which one is the most efficient implementation? By how much?



def loopFibonacci(index, a = 0, b = 1 ):
    '''accepts an index and returns a list with the fibonacci sequence until that index'''
    lista = []
    for n in range(0, index+1): 
        lista.append(a)
        a, b= b,a+b
        
        
        
    return lista



print(timeit.timeit('recursiveFibonacci(19,a = 0, b = 1, lista = [])', globals = globals()), "seconds")
print(timeit.timeit('loopFibonacci(19)', globals = globals()), "seconds")


#Ex 10 ===============================================================================================================================================================================================================================
print("Ex 10 **Class definition**")
# 
# Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
# 
# - Create appropriate methods to get and set the length of each side
# 
# - Create a method `perimeter()` that returns the perimeter of the polygon
# 
# - Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
# 
# Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.


class polygon():
    def __init__(self, sides:tuple):
        if len(sides) >= 3:                                          #checking number of sides
            self.sides = list(sides) 
        else:
            print("Error: number of sides has to be at least 3")

    def perimeter(self):
        return sum(self.sides)  

    def getOrderedSides(self,increasing = True):
        if not increasing:
            decr = sorted(self.sides)[::-1]
            return tuple(decr)
        
        return tuple(sorted(self.sides))



poli = polygon((2,6,9))
print(poli.perimeter())
print(poli.getOrderedSides())


#Ex 11 ======================================================================================================================================================================================================
print("Ex 11 **Class inheritance**")
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.



class rectangle(polygon):
    def __init__(self, sides):
        self.sides = []
    
        if len(sides) < 4:                                                       #checking number of sides
            print(f"Not enough sides")
        elif len(sides) > 4:
            print(f"Error: extra sides")
        
        
        else:
            for side in sides:
                if sides.count(side) != 2:
                    print("Error: in rectangles there are 2 pairs of equal sides") # checking sides to be equal in pairs
                else:
                    self.sides.append(side)
    
    def area(self):
        if len(self.sides) == 4:
            return min(self.sides)*max(self.sides)
        
        else:
            print("Error: wrong number of sides")




rec = rectangle((2,4,2,4))
print(f"area:{rec.area()}, perimeter: {rec.perimeter()}")
