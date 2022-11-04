import timeit

###########
# PART 1  #
###########
print("PART 1\n")
def f(alist):
    x = 5
    # Create a copy of the input variable and work on it
    alist = alist.copy()
    for i in range(x):
        alist.append(i) 
    return alist

alist = [1, 2, 3]
ans = f(alist)
print("Function returns" , ans)
print("Original list" , alist) # alist has not been changed

###########
# PART 2  #
###########
print("\nPART 2\n")
ans = [pow(x,2) for x in range(10) if x % 2 ==1]
print(ans)

############
# PART 3  #
###########
print("\nPART 3\n")
def shorter_than(words, n):
    # Using a length filtering lambda function on input words
    filtered_words = filter(lambda word: len(word)<n, words)
    return list(filtered_words)

print(shorter_than(["wow","ahahahah"],4))

###########
# PART 4  #
###########
print("\nPART 4\n")
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def lengths(dictionary):
    # Create a mapping of each key in the list and its length
    lengths = map(lambda key: len(key),dictionary.keys())
    return list(lengths)
print(lengths(lang))

###########
# PART 5  #
###########
print("\nPART 5\n")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
language_scores.sort(key=lambda x: x[0])

print(language_scores)

###########
# PART 6  #
###########
print("\nPART 6\n")
def square(number):
    return number**2

def cube(number):
    return number**3

def sixth_power(number):
    return square(cube(number))

print(sixth_power(2))

###########
# PART 7  #
###########
print("\nPART 7\n")
def hello(func):
    # Create a wrapper and pass the original methods arguments to it
    def wrapper(*args):
        print("Hello World!")
        return func(*args)

    return wrapper

@hello
def square(x):
    return x*x

print(square(2))

###########
# PART 8  #
###########
print("\nPART 8\n")
def recursiveFibonacci(n):
    # Base case
    if n <= 1:
        return n
    # Recursive case
    else:
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
print([recursiveFibonacci(n) for n in range(20)])

###########
# PART 9  #
###########
print("\nPART 9\n")
# The same function from the first example
def loopFibonacci(n):
    initial = [0,1]
    while len(initial) < n:
        initial.append( initial[-1] + initial[-2] )
    return initial

# Timings
time1 = timeit.Timer(lambda: loopFibonacci(20))
print(time1.timeit(1000))

time2 = timeit.Timer(lambda: recursiveFibonacci(20))
print(time2.timeit(1000))


###########
# PART 10 #
###########
print("\nPART 10\n")
class Polygon:
    def __init__(self, sides: tuple):
        # Check if the object is initiated properly
        if len(sides) < 3:
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

###########
# PART 11 #
###########
print("\nPART 11\n")
class Rectangle(Polygon):
    def __init__(self, sides: tuple):
        # Check if the object is initiated properly
        if len(sides) != 4:
            raise ValueError("Doesn't have 4 sides!")
        self.sides = sides

    def area(self):
        a , b = self.getOrderedSides()[0], self.getOrderedSides()[-1]
        return a * b

c = Rectangle(sides=(2,4,4,2))

print("Rectangle has perimeter:", c.perimeter())
print("Sides of the rectangle in ascending order are:", c.getOrderedSides())
print("Sides of the rectangle in descending order are:", c.getOrderedSides(incresing=False))
print("Area of the rectangle is:",c.area())
print("Setting first side as 25")
c.set_side(side_index=0, new_value=25)
print("New length of first side is", c.get_side(0))
print("New perimeter after changing the length of the first side is:", c.perimeter())