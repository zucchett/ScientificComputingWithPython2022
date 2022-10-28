# Q.1

def f(alist):
    x = 5
    alist = alist.copy()
    for i in range(x):
        alist.append(i) 
    return alist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has not been changed

# Q.2

ans = [pow(x,2) for x in range(10) if x % 2 ==1]
print(ans)

# Q.3

def shorter_than(words, n):
    filtered_words = filter(lambda word: len(word)<n, words)
    return list(filtered_words)

print(shorter_than(["wow","ahahahah"],4))

# Q.4

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def lengths(dictionary):
    lengths = map(lambda key: len(key),dictionary.keys())
    return list(lengths)
print(lengths(lang))

# Q.5

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])

print(language_scores)

# Q.6

def square(number):
    return number**2

def cube(number):
    return number**3

def sixth_power(number):
    return square(cube(number))

print(sixth_power(2))

# Q.7

def hello(func):
    def wrapper(*args):
        print("Hello World!")
        return func(*args)

    return wrapper

@hello
def square(x):
    return x*x

print(square(2))

# Q.8

def recursiveFibonacci(n):
    if n <= 1:
        return n
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
print([recursiveFibonacci(n) for n in range(20)])

# Q.9

def loopFibonacci(n):
    initial = [0,1]
    while len(initial) < n:
        initial.append( initial[-1] + initial[-2] )
    return initial

import timeit

time1 = timeit.Timer(lambda: loopFibonacci(20))
print(time1.timeit(1000))

time2 = timeit.Timer(lambda: recursiveFibonacci(20))
print(time2.timeit(1000))


class Polygon:
    def __init__(self, sides: tuple):
        if len(sides) != 4:
            raise ValueError("Doesn't have 4 sides!")
        self.sides = sides

    def get_side(self, side_index):
        return self.sides[side_index]

    def set_side(self, side_index, new_value):
        sides = list(self.sides)
        sides[side_index] = new_value
        self.sides = tuple(sides)

    def perimeter(self):
        return sum(list(self.sides))

    def getOrderedSides(self, incresing = True):
        sides = list(self.sides)
        if incresing:
            sides.sort()
        else:
            sides.sort(reverse=True)
        return sides

a = Polygon(sides = (3,4,5))
print("Perimeter of the polygon is:" , a.perimeter())
print("Sides of the polygon in ascending order are:", a.getOrderedSides())
print("Sides of the polygon in descending order are:", a.getOrderedSides(incresing=False))
print("Setting first side as 15")
a.set_side(side_index=0, new_value=15)
print("New length of first side is", a.get_side(0))
print("New parameter after changing the length of the first side is:", a.perimeter())
try:
    b = Polygon(sides=(1,9))
except Exception as e:
    print("When creating a polgon with fewer sides than 3 we get error:\n", e)

print("here")