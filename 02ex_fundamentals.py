# Exercise 2

# Part 1.
def f(alist, x):
    result = alist.copy()
    for i in range(x):
        result.append(i)
    return result

alist = [1, 2, 3]
ans = f(alist, 5)
print("ans: ", ans)
print("alist: ", alist) # alist has NOT been changed

# Part 2.
ans = [x ** 2 for x in range(10) if x % 2 == 1]
print(ans)

# Part 3.
example_list = ["This", "is", "an", "example", "list", "of", "words"]
def func(words, n):
    result = filter(lambda word: len(word) < n, words)
    return list(result)

print(func(example_list, 5))

# Part 4.
lang = {"Python": 3, "Java": '', "Cplusplus": 'test', "Php": 0.7}

def get_length(key):
    return len(key)

def func(lang):
    return list(map(get_length, lang.keys()))

print(func(lang))

# Part 5.
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda tup: tup[0])
print(language_scores)

# Part 6.
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def third_func(x):
    return square(cube(x))

print(third_func(3))

# Part 7.
def hello(func):
    def wrapper(*args):
        print("Hello World!")
        return func(*args)
    return wrapper
@hello
def square(x):
    return x*x

print(square(2))

# Part 8.
def fibonacci(n):
    if n < 0:
        print("n cannot be smaller than 0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(20):
    print("Element", i + 1, ":", fibonacci(i))

# Part 9.
import time
# First algorithm
def fibonacci_seq(n):
    if n < 0:
        print("You cannot enter value smaller than 0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        first = 0
        second = 1
        fibonacci_sequence = [first, second]

        for i in range(2,n):
            third = first + second
            fibonacci_sequence.append(third)
            first = second
            second = third
        return fibonacci_sequence



# Second algorithm
def fibonacci(n):
    if n < 0:
        print("n cannot be smaller than 0")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def helper(n):
    for i in range(n):
        # print("Element", i + 1, ":", fibonacci(i))
        fibonacci(i)

# Suggested %timeof does not work in a .py file so I used time.time()
start = time.time()
fibonacci_seq(20)
end = time.time()
print("Time of first algoritm:", end - start, "ms")

start = time.time()
helper(20)
end = time.time()
print("Time of second algorithm", end - start, "ms")
# First algorithm is more efficient

# Part 10.
class Polygon:
    def __init__(self, sides: tuple):
        if len(sides) < 3:
            raise ValueError("Shouldn't be less sides than 3")
        self.sides = sides

    def set_side(self, index, new_side):
        sides = list(self.sides)
        sides[index] = new_side
        self.sides = tuple(sides)
        return self.sides[index]

    def get_side(self, index):
        return self.sides[index]

    def perimeter(self):
        return sum(list(self.sides))

    def getOrderedSides(self, increasing=True):
        if increasing:
            sides = list(self.sides)
            sides = sorted(sides)
            self.sides = tuple(sides)
            return self.sides
        else:
            return self.sides

# Testing the class
polygon = Polygon((2,4,5))
print(polygon.set_side(0,10))
print(polygon.get_side(1))
print(polygon.perimeter())
print(polygon.getOrderedSides(False))

# Part 11.
class rectangle(Polygon):
    def __init__(self, sides: tuple):
        rect_sides = sorted(list(sides))
        if rect_sides[0] != rect_sides[1] or rect_sides[2] != rect_sides[3]:
            raise ValueError("This is not a propriate rectange")
        elif len(sides) != 4:
            raise ValueError("There should be 4 sides")
        self.sides = sides
    
    def area(self):
        sides = sorted(list(self.sides))
        area = sides[0] * sides[len(sides) - 1]
        return area
    
rect = rectangle((3,10,10,3))
print("Area of the rectangle is:", rect.area())