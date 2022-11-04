# Exercise 1

# Part 1.a)
temp_list = []
for i in range(1, 101):
    # Check if its divisible by 15
    if i % 15 == 0:
        print("HelloWorld")
        temp_list.append("HelloWorld")
    # Check if its divisible by 3
    elif i % 3 == 0:
        print("Hello")
        temp_list.append("Hello")
    # Check if its divisible by 5
    elif i % 5 == 0:
        print("World")
        temp_list.append("World")
    # Also add values to a list to use in later part

# Part 1.b)

# For each value we change "Hello" with "Python" and "World" with "Works"
# Then turn that list into a tuple
for i in range(len(temp_list)):
    if temp_list[i] == "Hello":
        temp_list[i] = "Python"
    elif temp_list[i] == "World":
        temp_list[i] = "Works"
temp_list = tuple(temp_list)
print(temp_list)


# Part 2.
x = input("Enter x value")
y = input("Enter y value")

print("x is ", x)
print("y is ", y)
# By using x, y = y, x we can swap values without using a temp variable
x, y = y, x

print("After swap:")
print("x is ", x)
print("y is ", y)

# Part 3.
import math
def calculate_distance(u, v):
    return math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

distance = calculate_distance((3,0), (0,4))
print(distance)

# Part 4.
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def count_letters(sentence):
    dict = {}
    for char in sentence:
        if char.lower() in dict:
            dict[char.lower()] = dict.get(char.lower(), 0) + 1
        else:
            dict[char.lower()] = 1

    return dict

print(count_letters(s1))
print(count_letters(s2))

# Part 5.
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique_numbers = []

for number in l:
    if number in unique_numbers:
        continue
    else:
        unique_numbers.append(number)

print("Unique Numbers are: ", unique_numbers)
print("Count of Unique Numbers is: ", len(unique_numbers))

# Doing the same with Python data structures
unique_numbers = list(set(l))
print("Unique Numbers are: ", unique_numbers)
print("Count of Unique Numbers is: ", len(unique_numbers))

# Part 6.
types = [int, float, str]
result = None
x = input("Enter first variable as either int, float or str")
y = input("Enter second variable as either int, float or str")

# We need to check if types are compatible
for type1 in types:
    for type2 in types:
        try:
            result = sum([type1(x), type2(y)])
            break
        except:
            continue
    if result != None:
        break

if result != None:
    print(result)
else:
    print("You are trying to add values with different types")

# Part 7.a)
list_for_a = []
for i in range(0, 10):
    list_for_a.append(i**3)
print(list_for_a)

# Part 7.b)
list_for_b = [x**3 for x in range(0, 10)]
print(list_for_b)

# Part 8.
a = [(x, y) for x in range(3) for y in range(4)]
print(a)
# Part 9.
unique_pythagorean = [(a, b, c) for a in range(1, 100) for b in range(1, 100) for c in range(1, 100) if (a**2 + b**2 == c**2) and b > a]
print(unique_pythagorean)

# Part 10.
from math import sqrt
def normalization(my_tuple):
    sqrtsum = sqrt(sum(x**2 for x in my_tuple))
    result = tuple(x/sqrtsum for x in my_tuple)
    return result

print(normalization((3,4,5)))

# Part 11.
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

print(fibonacci_seq(20))