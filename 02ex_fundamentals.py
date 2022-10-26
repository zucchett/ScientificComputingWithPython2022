#You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `02ex_fundamentals.py`.

#In case you need multiple files, name them `02ex_fundamentals_es01.py`, `02ex_fundamentals_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `02ex_fundamentals`.

#The exercises need to run without errors with `python3`.

#1\. **Global variables**

#Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list
x = 5

def f(alist):
    list2=alist[:]
    for i in range(x):
        list2.append(i)
    return list2, alist

alist = [1, 2, 3]
ans,alist2 = f(alist)
print(ans)
print(alist2) 

#2\. **List comprehension**

#Write the following expression using a list comprehension:

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
ans2=[x**2 for x in range(10) if x%2==1]
print(ans2)

#3\. **Filter list**

#Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

    
def filter2(l,n):
    return_list=list(filter(lambda x:len(x)<n,l))
    return return_list
print(filter2(['anais','papa','famille','maman','anticonstitutionnellement'],6))

#4\. **Map dictionary**

#Consider the following dictionary:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

#Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

def map2(dic):
    list_result=list(map(len,dic.keys()))
    return list_result
print(map2(lang))
#5\. **Lambda functions**

#Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

#*Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

sorted_list=sorted(language_scores, key=lambda score: score[0])
print(sorted_list)

#6\. **Nested functions**

#Write two functions: one that returns the square of a number, and one that returns its cube.

def square(x):
    return x*x
def cube(x):
    return x*x*x
#Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.
def sixth(x):
    return square(cube(x))

print(sixth(4))
#7\. **Decorators**

#Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.
def hello(func):
    def wrapper(x):
        func(x)
        print("Hello world!")
    return wrapper
#The wrapped function should look like:


@hello
def square(x):
 return x*x

square(4)
#8\. **The Fibonacci sequence (part 2)**

#Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.
def recursiveFibonacci(n):
    if n<=1:
        return n
    else:
        return (recursiveFibonacci(n-1)+recursiveFibonacci(n-2))

print('fibo_recurs: ',[recursiveFibonacci(i) for i in range(20)])
#9\. **The Fibonacci sequence (part 3)**

#Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
def loopFibonacci(n):
    l=[]
    f=0
    fp=1
    for i in range(20):
        if i<=1:
            l.append(i)
        else:
            fpp=f+fp
            f=fp
            fp=fpp
            l.append(fpp)
    return l
print('fibo_ex1: ',loopFibonacci(10))
#Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
import timeit

time1=timeit.timeit('recursiveFibonacci(5)',globals=globals())
time2=timeit.timeit('loopFibonacci(5)',globals=globals())

#which one is the most efficient implementation? By how much?

print('The Recursive function is the fastest so the most efficient by: ', time2/time1)
#10\. **Class definition**

#Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

class polygon:

    def __init__(self, tuple):
        self.lengths=tuple
        
#- Create appropriate methods to get and set the length of each side
    def getLength(self):
        return self.lengths

    def setLenghts(self,lenght):
        for i in (lenght):
            self.lengths+(i,)

#- Create a method `perimeter()` that returns the perimeter of the polygon
    def perimeter(self):
        p=0
        for l in self.lengths:
            p=p+l
        return p
#- Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
    def getOrderedSides(self,increasing = True):
        if increasing:
            ordered_tuple= sorted(self.lengths)
        else:
            ordered_tuple=sorted(self.lengths,everse=True)
        return ordered_tuple
#Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.
p= polygon((4,5,3))
print("Perimeter: ",p.perimeter())
print("ordered side: ", p.getOrderedSides(increasing=True))
#11\. **Class inheritance**

#Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
class rectangle(polygon):
    def __init__(self, tuple):
        if len(tuple)==4:
            self.lengths=tuple
        else:
            print("Error")
#- Create a method `area()` that returns the area of the rectangle.
    def area(self):
        area=1
        for l in self.lengths:
            area=area*l
        return area
#Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.
#p2=polygon()
rect=rectangle((4,3,6,5))
print('aire du rect: ', rect.area())