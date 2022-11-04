"""
01ex_introduction
Name and surname: Mattia Sabatini
Number of matricola: 2092001
Istitutional email adress: mattia.sabatini@studenti.unipd.it
Your curriculum: single courses
"""



###########################################################################################################################################



'''
1. The HelloWorld replacement

a) Write a program that:

    prints the numbers from 1 to 100
    but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
    for numbers which are multiples of both three and five print "HelloWorld".

b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".
'''



# Ex. 1.

# a)

print("\n\n\nEx. 1.")
print("\na)\n")

#Function that returns "Hello" for numbers multiples of three, "World" for multiples of five and "HelloWorld" for multiples of three and five. In all other cases, it returns the input value.
def HelloWorld(a):
        if a % 3 == 0 and a % 5 == 0:
            return "HelloWorld"
        elif a % 3 == 0:
            return "Hello"
        elif a % 5 == 0:
            return "World"
        else: 
            return a

#The function is applied to all numbers from 1 to 100 and the results are inserted into a tuple
result1 = tuple([HelloWorld(x) for x in range(1,101)])

print(result1)



# b)

print("\n\n\nEx. 1.")
print("\nb)\n")

#Function that returns "Python" for the string "Hello", "Works" for "World" and "PythonWorks" for "HelloWorld". In all other cases, it returns the input value.
def PythonWorks(b):
    if b == "Hello":
        return "Python"
    elif b == "World":
        return "Works"
    elif b == "HelloWorld":
        return "PythonWorks"
    else:
        return b

#The function is applied to all objects of the previous tuple and the results are inserted into a tuple
result2 = tuple([PythonWorks(y) for y in result1])

print(result2)



###########################################################################################################################################



'''
2. The swap

Write a program that swaps the values of two input variables x and y from command line (whatever the type).

Try to do that without using a temporary variable, exploiting the Python syntax.

'''



# Ex. 2.

print("\n\n\nEx. 2.")

x = input("Set the value of x: ")
y = input("Set the value of y: ")

#x and y are swapped
x,y = y,x

print("\nx =", x)
print("y =", y)



###########################################################################################################################################



'''
3. Computing the distance

Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).

Example: if u=(3,0) and v=(0,4), the function should return 5.

Hint: in order to compute the square root, import the math library with import math and use math.sqrt().
'''



# Ex. 3.

print("\n\n\nEx. 3.\n")

import math

#Function that returns the euclidean distance between two points u and v in a 2D space
def dist(a,b):
    x2 = (a[0] - b[0])**2
    y2 = (a[1] - b[1])**2
    return(math.sqrt(x2 + y2))

u = (3,0)
v = (0,4)
print("u =", u)
print("v =", v)
print("Euclidean distance =", dist(u,v))



###########################################################################################################################################



'''
4. Counting letters

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

The strings are in the cell below.

'''



# Ex. 4.

print("\n\n\nEx. 4.\n")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

#Function that inserts each character of the string into a dictionary (as a key) and associates with it the number of times it occurs in the string
def count(s):
    dictionary = {}
    for x in s.lower():
        if x in dictionary: 
            dictionary[x] += 1
        else: 
            dictionary[x] = 1
    return dictionary

print(count(s1))
print("\n",count(s2))



###########################################################################################################################################



'''
5. Isolating the unique

Write a program that determines and counts the unique numbers in the list:

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
     85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
     1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
     45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
    
Do the same exploiting only the Python data structures.
'''



# Ex. 5.

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# a)

print("\n\n\nEx. 5.")
print("\na)\n")

#Function that returns a list without equal values
def unique(a):
    count_list = []
    for x in a:
        if x not in count_list:
            count_list.append(x)    
    return count_list
     
result1 = unique(l)

print("There are", len(result1), "unique numbers in the list:\n", result1)



# b)

print("\n\n\nEx. 5.")
print("\nb)\n")

#Using set the identical elements of the list are not taken into account
result2 = set(l)

print("There are", len(result2), "unique numbers in the list:\n", result2)



###########################################################################################################################################



'''
6. Casting

Write a program that:

    reads from command line two variables, that can be either int, float, or str.
    use the try/except expressions to perform the addition of these two variables, only if possible
    and print the result without making the code crash for all the int/float/str input combinations.
'''


# Ex. 6.

print("\n\n\nEx. 6.")

x,y = input("Set the value of x: "), input("Set the value of y: ")

try:
    print("\nx + y =", int(x) + int(y))
except:
    try:
        print("\nx + y =", float(x) + float(y))
    except:
        try:
            print("\nx + y =", str(x) + str(y))  
        except:
            print("Error! Insert: int, float or string variables")
            
            

###########################################################################################################################################



'''
7. Cubes

Create a list of the cubes of x for x in [0, 10] using:

a) a for loop

b) a list comprehension

'''



# Ex. 7.

# a)

print("\n\n\nEx. 7.")
print("\na)\n")

cubes1 = []

#List of the cubes of x using a for loop
for i in range(11):
    cubes1.append(i**3)

print(cubes1)



# b)

print("\n\n\nEx. 7.")
print("\nb)\n")

#List of the cubes of x using a list comprehension
cubes2 = [j**3 for j in range(11)]

print(cubes2)



###########################################################################################################################################



'''
8. List comprehension

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

'''



# Ex. 8.

print("\n\n\nEx. 8.\n")

a = []

for i in range(3):
    for j in range(4):
        a.append((i, j))
        
print(a)
print('\n')

#List comprehension
l = [(i,j) for i in range(3) for j in range(4)]

print(l)



###########################################################################################################################################



'''
9. Nested list comprehension

    A Pythagorean triple is an integer solution to the Pythagorean theorem a2+b2=c2. The first Pythagorean triple is (3, 4, 5).

Find and put in a tuple all unique Pythagorean triples for the positive integers a, b and c with c<100.
'''



# Ex. 9.

print("\n\n\nEx. 9.\n")

#Set is used to obtain the unique Pythagorean triples, i.e. without repetitions
triplets = set( (i,j,k) for i in range(1,100) for j in range(1,100) for k in range(1,100) if i**2+j**2==k**2 )
result = tuple(triplets)
print(result)



###########################################################################################################################################



'''
10. Normalization of a N-dimensional vector

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).
'''



# Ex. 10.

print("\n\n\nEx. 10.\n")

#Function that normalizes an N-dimensional vector and returns a tuple
def norm(x):
    sum_squares = 0
    for i in x:
        sum_squares += i**2
    norm_list = [j/(sum_squares**0.5) for j in x]
    return tuple(norm_list)

v = (1,2,3)
print(norm(v))



###########################################################################################################################################



'''
11. The Fibonacci sequence

Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.
'''



# Ex. 11.

# a)

print("\n\n\nEx. 11.")
print("\na)\n")

#Function that calculates the first n numbers of the Fibonacci sequence using the for loop and returns a list
def Fibonacci_for(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(2, n):
            sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print(Fibonacci_for(20))



# b)

print("\n\n\nEx. 11.")
print("\nb)\n")

#Function that calculates the first n numbers of the Fibonacci sequence using the while loop and returns a list
def Fibonacci_while(n):
    sequence = []
    if n == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        count = 2
        while count < n:
            sequence.append(sequence[count-1] + sequence[count-2])
            count += 1
    return sequence

print(Fibonacci_while(20))
