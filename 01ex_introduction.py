import math
##### 1. The HelloWorld replacement
# a) Write a program that:
#
#     prints the numbers from 1 to 100
#     but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
#     for numbers which are multiples of both three and five print "HelloWorld".
#

result = []
for i in range(1, 101):
    result.append(i)
    if i % 15 == 0:
        result[i-1] = "HelloWorld"
    elif i % 3 == 0:
        result[i-1] = "Hello"
    elif i % 5 == 0:
        result[i-1] = "World"
    else:
        result[i-1] = i
print(result)

# b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works"
for j in range(len(result)):
    if result[j] == "Hello":
        result[j] = "Python"
    elif result[j] == "World":
        result[j] = "Works"
    elif result[j] == "HelloWorld":
        result[j] = "PythonWorks"
tup_result = tuple(result)
print(tup_result)

##### 2. The swap
print("*** Swap ***")
value1 = input("Enter Value1:\n")
value2 = input("Enter Value2:\n")
value1, value2 = value2, value1
print("Value1 is :", value1, "\nValue2 is :", value2)

##### 3. Computing the distance
import math
print("*** Computing The Euclidean Distance ***")
u_tuple = input("Enter First Tuple with space, e.g. tasks=a b:\n")
v_tuple = input("Enter Second Tuple with space, e.g. tasks=a b:\n")
u_tuple = tuple(float(item) for item in u_tuple.split())
v_tuple = tuple(float(item) for item in v_tuple.split())
d = math.sqrt((u_tuple[0] - v_tuple[0]) ** 2 + (u_tuple[1] - v_tuple[1]) ** 2)
print("The Euclidean Distance : ", d)

#### 4. Counting letters
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
input_string = input("Enter the String:\n")
counter_dic = {}
def character_counter(input_string):
    for i in input_string:
        if i not in counter_dic.keys():
            counter_dic[i] = 1
        else:
            counter_dic[i] += 1
    return counter_dic
print(character_counter(input_string))
print("s1: \n", character_counter(s1))
print("s2: \n", character_counter(s2))

#### 5. Isolating the unique
print("*** Isolating the unique ***")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
input_list = input("enter a list: \n")
def unique_counter(input_list):
   return set(input_list)
print("The Unique Elements are:\n", unique_counter(input_list),
      "\n The Num Of Unique Elements: ", len(unique_counter(input_list)))
print("The Unique Elements in l:\n", unique_counter(l),
      "\n The Num Of Unique Elements in l: ", len(unique_counter(l)))

#### 6. Casting
print("*** Casting ***")
value1 = input("Enter 1st Value:\n")
value2 = input("Enter 2nd Value:\n")
try:
    value1 = float(value1)
    value2 = float(value2)
    result = value1 + value2
    print(result)
except ValueError:
    print("No.. input is not a number. It's a string")

#### 7. Cubes
# using loop
print("*** Cubes ***")
print("Result for loop")
for x in range(11):
    x_cube = pow(x, 3)
    print(x_cube)

# using list comprehension
print("Result for list comprehension")
[print(pow(x, 3))for x in range(11)]


#### 8. List comprehension
print([(i, j)for i in range(3) for j in range(4)])

#### 9. Nested list comprehension
print([(a, b, c) for a in range(1, 100) for b in range(1, 100)
       for c in range(100) if a**2 + b**2 == c**2])

#### 10. Normalization of a N-dimensional vector
n_vector_tuple = input("Enter the n_dimension Vector with space between elements:\n").split()
s= 0 # sum of the square of all elements
for i in n_vector_tuple:
    s += float(i)**2
print([float(j)/s for j in n_vector_tuple])


#### 11. The Fibonacci sequence
sequence = [0,1]
for i in range(1, 19):
    sequence.append(sequence[i-1] + sequence[i])
print("Fibonacci Sequence:\n", sequence)