# Exercise 1 - The HelloWorld replacement

print("Exercise 1")
list1 = []
for x in range(1, 101):
    string_to_print = ''
    if x % 3 == 0:  # for multiples of three print 'Hello'
        string_to_print += "Hello"
        list1.append('Hello')
    if x % 5 == 0:
        string_to_print += "World"  # for multiplies of five print 'world'
        list1.append("World")
    elif x % 3 != 0 and x % 5 != 0:
        string_to_print += str(x)
        list1.append(x)
    print(string_to_print)


# b)
def convert(list1):  # function to convert list to tuple
    return tuple(list1)


print("\n")
print(tuple(list1))  # print the result in a tuple
for i in range(len(list1)):  # make the changes on the list (substituting 'Hello' with 'Python' and 'World' with 'Works'
    if list1[i] == 'Hello':
        list1[i] = 'Python'
    if list1[i] == 'World':
        list1[i] = 'Works'
print(tuple(list1))  # print the result in a tuple

# Exercise 2 - The swap
print("\n")
print("Exercise 2")
x = input("Enter x: ")
y = input("Enter y: ")
print(x, y)
x, y = y, x  # swap without using a temporary variable
print(x, y)

# Exercise 3 - Computing the distance
print("\n")
print("Exercise 3")

import math

def euclidean(u, v):  # function that calculates and return the euclidean distance between two points
    return math.sqrt((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2)

u = (3, 0)
v = (0, 4)
print(euclidean(u, v))

# Exercise 4 - Counting letters
print("\n")
print("Exercise 4")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
s1 = s1.lower()  # Ignoring differences in capitalization
s2 = s2.lower()
occurs1 = {x: s1.count(x) for x in set(s1)}
occurs2 = {x: s2.count(x) for x in set(s2)}
print("Occurrence of all characters in the given string is :\n " + str(occurs1))
print("Occurrence of all characters in the given string is :\n " + str(occurs2))

# Exercise 5 - Isolating the unique
print("\n")
print("Exercise 5")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
isolate_the_unique = set(l)  # convert to set - they do not support duplicates
print("The unique numbers in the list: ")
print(isolate_the_unique)
print("The number of unique numbers: ")
print(len(isolate_the_unique))  # len - function that returns the number of items in an object

# Exercise 6 - Casting
print("\n")
print("Exercise 6")
x = input("Please insert variable x: ")
y = input("Please insert variable y: ")

try:
    variable1 = int(x)
except ValueError:
    try:
        variable1 = float(x)
    except ValueError:
        variable1 = x
try:
    variable2 = int(y)
except ValueError:
    try:
        variable2 = float(y)
    except ValueError:
        variable2 = y

try:
    print("Addition:", variable1 + variable2)  # if possible
except:
    print("The addition of these two variables is not possible.")

# Exercise 7 - Cubes
# a)
print("\n")
print("Exercise 7")
a = []
for x in range(0, 11):
    a.append(x * x * x)
print(a)

# b)
print("\n")
cube_list = [x * x * x for x in range(0, 11)]
print(cube_list)

# Exercise 8 - List comprehension
print("\n")
print("Exercise 8")
b = [(x, y) for x in [0, 1, 2] for y in [0, 1, 2, 3]]
print(b)

# Exercise 9 - Nested list comprehension
print("\n")
print("Exercise 9")
pythagorean_triples = tuple([(a, b, c) for a in range(1, 100) for b in range(1, 100) for c in range(1, 100) if a*a+b*b==c*c])
print(pythagorean_triples)

# Exercise 10 - Normalization of N-dimensional vector
print("\n")
print("Exercise 10")

def normalize_vector(vector): # function to normalize the vector to one
    squaredsum = sum([i*i for i in vector])
    return tuple([i/math.sqrt(squaredsum) for i in vector])

print("Normalization of the vector", normalize_vector((7, 3, 2)))

# Exercise 11 - The Fibonacci sequence
# Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.
print("\n")
print("Exercise 11")

def fibonacci_while(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0, 1]
        count = 1
        while count + 1 < 20:
            sequence.append(sequence[count - 1] + sequence[count])
            count = count + 1
    return sequence

print(fibonacci_while(20))