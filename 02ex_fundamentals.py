# Exercise 1 - Global variables

print("\n")
print("Exercise 1")
def f(alist, x):
    blist = alist.copy()
    for i in range(x):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist)

# Exercise 2 - List comprehension
print("\n")
print("Exercise 2")
list = list()
for i in range(10):
    if i % 2 == 1:
       list.append(i * i)
print(list)

# Exercise 3 - Filter list
print("\n")
print("Exercise 3")
def filtershorterword(string, number):
    return [word for word in string if len(word) < number]

string = ["Php","Java", "JavaScript", "Python", "C++"]
number = 4
print(filtershorterword(string, number))

# Exercise 4 - Map dictionary
print("\n")
print("Exercise 4")
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

map_result = map(len, lang)
for item in map_result:
    print(item)

# Exercise 5 - Lambda functions
print("\n")
print("Exercise 5")
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])
print(" ", language_scores)

# Exercise 6 - Nested functions

print("\n")
print("Exercise 6")
x = int(input("Please enter x: "))

def square(x):
    return x * x

def cube(x):
    return x * x * x

print("Square of", x, "is", square(x))
print("Cube of", x, "is", cube(x))
print("The 6th power of", x, "is", square(cube(x)))

# Exercise 7 - Decorators
print("\n")
print("Exercise 7")
x = int(input("Please enter x: "))

def hello(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        val = func(*args, **kwargs)
        return val

    return wrapper

@hello
def square(x):
     return x * x

print(square(x))

# Exercise 8 - The Fibonacci sequence (part 2)
print("\n")
print("Exercise 8")

def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

for n in range(20):
    print(fibonacci(n))

# Exercise 9 - The Fibonacci sequence (part 3)


print("\n")
print("Exercise 9")

def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

for n in range(20):
    print(fibonacci(n))


def fibonacci_while(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        count = 1
        while count + 1 < 20:
            sequence.append(sequence[count-1] + sequence[count])
            count = count + 1
    return sequence

print(fibonacci_while(20))

import timeit

result = timeit.timeit('fibonacci(n)', globals=globals(), number=20)
result1 = timeit.timeit('fibonacci_while(n)', globals=globals(), number=20)
print("The execution time using the recursive function is ", result)
print("The execution time using while loop is ", result1)

# The execution time with the recursion function is shorter because  with the loop you take smaller (and therefore more)
# steps, while in the recursion you take larger and fewer steps.

# Exercise 10 - Class definition

from math import prod

class polygon:

    def _init_(self, t):
        if not isinstance(t, tuple):
            raise Exception('Input must be tuple')
        if len(t) < 3:
            raise Exception('It must have more than 3 sides')
        self.lengths = t

    def getLengths(self):
        return self.lengths

    def setLengths(self, t):
        self.lengths = t

    def perimeter(self):
        return sum(tuple(self.getLengths()))

    def getOrderedSides(self, increasing=True):
        return tuple(sorted(self.lengths, reverse=increasing))


test = polygon((7, 5, 5))
test.setLengths((28, 43, 24))
print(test.perimeter())
print(test.getOrderedSides(False))

# Exercise 11 - Class inheritance

class rectangle(polygon):
    def _init_(self, t):
        if not isinstance(t, tuple):
            raise Exception('Input must be tuple')
        if len(t) != 2:
            raise Exception('It must have gjatesi e gjeresi')
        self.lengths = t

    def area(self):
        return prod(self.getLengths())

test2 = rectangle((2, 4))
print(test2.area())





