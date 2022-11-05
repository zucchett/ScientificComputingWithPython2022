#1-Global variables
def f(alist):
    x=5
    for i in range(x):
        alist.append(i)
    return alist
ans = [1, 2, 3, 4]
print(f(ans))


#2-List comprehension
ans = [x*x for x in range(10) if x % 2 == 1]

#3-Filter list  
def filter(string, nr):
    return [word for word in string if len(word) < nr]

string = ['today', 'is', 'friday', 'the', 'end', 'of', 'the', 'week']
nr = 10
print(filter(string, nr))

#4-Map dictionary
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
length = len(lang.keys())

result = list(map(length))
print(result)

#5-Lambda functions
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
result = sorted(language_scores, key = lambda x: (x[0:]))
print(result)


#6-Nested functions
def square(x):
    return x**2
def cube(x):
    return x**3
def sixth(x):
    return square(cube(x))
num = sixth(2)
print(num)


#7-Decorators
def hello(func):
    def wrapped_func():
        print('-' * 15)
        func()
        print('-' * 15)
    return wrapped_func

@hello
def say_hello():
    print("Hello World!")

say_hello()

#8-The Fibonacci sequence(part 2)
def recursive_f(n):  
   if n <= 1:  
       return n  
   else:  
       return(recursive_f(n-1) + recursive_f(n-2))  
# take input from the user  
nr = int(input("How many terms? "))  
# check if the number of terms is valid  
if nr <= 0:  
   print("Enter a value")  
else:  
   print("The Fibonacci sequence:")  
   for i in range(nr):  
       print(recursive_f(i))  

#9-The Fibonacci sequence (part 3)
def recursive_f(n):
    if n in {0, 1}:
        return n
    return recursive_f(n - 1) + recursive_f(n - 2)
for n in range(20):
    print(recursive_f(n))


def fibonacci_loop(n):
    sequence = []
    if n == 1:
        fib_seq = [0]
    else:
        fib_seq = [0,1]
        count = 1
        while count + 1 < 20:
            fib_seq.append(fib_seq[count-1] + fib_seq[count])
            count = count + 1
    return fib_seq

print(fibonacci_loop(20))

import timeit

result = timeit.timeit('recursive_f(n)', globals=globals(), number=20)
result1 = timeit.timeit('fibonacci_loop(n)', globals=globals(), number=20)
print("The execution time using the recursive function is ", result)
print("The execution time using while loop is ", result1)

# The execution time with the recursion function is shorter compared to the loop, as it take smaller and more steps
#,meanwhile in recursion the steps you take are bigger and fewer.


#10-Class definition
from math import prod
class polygon: 
    def _init_(self, t):
        if not isinstance(t, tuple):
            raise Exception('Input must be a tuple!')
        if len(t) < 3 :
            raise Exception('Polygon must have more than 3 sides!')
        self.lengths = t
    
    def getLengths(self):
        return self.lengths
    
    def setLengths(self,t):
        self.lengths = t
    
    def perimeter(self):
        return sum(list(self.getLengths()))
    def getOrderedSides(self,increasing = True):
        return tuple(sorted(self.lengths,reverse = increasing))
        
t = polygon((7,5,8))
t.setLengths((28,43,24))
print(t.perimeter())
print(t.getOrderedSides(False))

#9-The Fibonacci sequence (part 3)
def recursive_f(n):
    if n in {0, 1}:
        return n
    return recursive_f(n - 1) + recursive_f(n - 2)
for n in range(20):
    print(recursive_f(n))


def fibonacci_loop(n):
    sequence = []
    if n == 1:
        fib_seq = [0]
    else:
        fib_seq = [0,1]
        count = 1
        while count + 1 < 20:
            fib_seq.append(fib_seq[count-1] + fib_seq[count])
            count = count + 1
    return fib_seq

print(fibonacci_loop(20))

import timeit

result = timeit.timeit('recursive_f(n)', globals=globals(), number=20)
result1 = timeit.timeit('fibonacci_loop(n)', globals=globals(), number=20)
print("The execution time using the recursive function is ", result)
print("The execution time using while loop is ", result1)

# The execution time with the recursion function is shorter compared to the loop, as it take smaller and more steps
#,meanwhile in recursion the steps you take are bigger and fewer.
