"""
Author : Ömer Cem Tabar
Exercise Document 01 Solution File

This file only includes the codes that is required to solve the questions
You can also check the outputs from the notebook

"""

"""
1)The HelloWorld replacement

a) Write a program that:
- prints the numbers from 1 to 100
- but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
- for numbers which are multiples of both three and five print "`HelloWorld`".



"""
Collection = []
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("HelloWorld")
        Collection.append("HelloWorld")
    elif i % 3 == 0:
        print("Hello")
        Collection.append("Hello")
    elif i % 5 == 0:
        print("World")
        Collection.append("World")
    else:
        print(i)
        Collection.append(i)
        
"""
1)The HelloWorld replacement
b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

"""

for i in range(len(Collection)):
    if Collection[i] == "HelloWorld":
        Collection[i] = "PythonWorks"
    elif Collection[i] == "Hello":
        Collection[i] = "Python"
    elif Collection[i] == "World":
        Collection[i] = "Works"
    else:
        Collection[i] = Collection[i]
tupleList = tuple(Collection)
print(tupleList)


"""
2) **The swap**

Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).

Try to do that without using a temporary variable, exploiting the Python syntax.

"""

x = input("Please enter the first input variable: ")
y = input("Pleaser enter the second input variable: ")

x_before = x
y_before = y

x,y = y,x
print("Before the swap operation x was: " + x_before + ", after the swap operation the new value of x is: " + x)
print("Before the swap operation x was: " + y_before + ", after the swap operation the new value of x is: " + y)


"""
3) **Computing the distance**

Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.

Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.

*Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

"""
import math
def EuclidianDistance(u,v):
    result = math.sqrt(((v[0]-u[0])**2)+((v[1]-u[1])**2))
    return int(result)
a = input("Please enter the x-value of the first input variable:")
b = input("Please enter the y-value of the first input variable:")
c = input("Please enter the x-value of the second input variable:")
d = input("Please enter the y-value of the second input variable:")
u = (int(a),int(b))
v = (int(c),int(d))
returnedResult = EuclidianDistance(u,v)
print("Euclidian Distance between two points : " + str(returnedResult))


"""
4) **Counting letters**

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

The strings are in the cell below.
"""

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def CountCharacterOccurencesInSentence(s):
    OccuredList = []
    OccurenceDictionary = {}
    s = s.lower()
    for i in range(len(s)):
        if s[i] not in OccuredList:
            OccuredList.append(s[i])
            OccurenceDictionary[s[i]] = 1
        else:
            
            OccurenceDictionary[s[i]] = OccurenceDictionary[s[i]] + 1
    for i in OccurenceDictionary.keys():
        print("Number of occurence of the character '" + i + "' occured " + str(OccurenceDictionary[i]) + " time(s) in the sentence.")
        
print("Occurences in the first sentence can be shown as follows:")
CountCharacterOccurencesInSentence(s1)
print("")
print("Occurences in the second sentence can be shown as follows:")
CountCharacterOccurencesInSentence(s2)

"""
5)**Isolating the unique**

Write a program that determines and counts the unique numbers in the list:
"""

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def CountUniqueNumbers(mixedList):
    Unique = []
    for element in mixedList:
        if element not in Unique:
            Unique.append(element)
    print("There are " + str(len(Unique)) + " unique numbers which are: " + str(Unique))

CountUniqueNumbers(l)

"""
6) **Casting**

Write a program that:
* reads from command line two variables, that can be either `int`, `float`, or `str`.
* use the `try`/`except` expressions to perform the addition of these two variables, only if possible
* and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

"""

a = input("Please enter the first value for addition: ")
b = input("Please enter the second value for addition: ")

try:
    #Check whether the input 'a' is float/int
    #Since both int and float can be converted into float
    x = float(a)
    if a == str(float(a)):
        
        print("First input is a float!")
        try:
                
            #Check whether the input 'a' is float/int
            #Since both int and float can be converted into float
            y = float(b)
            if b == str(float(b)):
                print("Second input is also a float!")
                print("Addition operation will result in a float number: " + str(float(a)+float(b)))
            else:
                print("Second input is an integer!")
                print("Addition operation will result in a float number: " + str(float(a)+int(b)))

        except:
            print("Second input is a string!")
            #Input 'b' is not a float or int, hence it is string
            #You cannot add float with string
            print("You cannot do the addition operation between float and string!!!!")
    else:
        print("First input is an integer!")
        try:
           #Check whether the input 'b' is float/int
           #Since both int and float can be converted into float
            y = float(b)
            if b == str(float(b)):
                print("Second input is a float!")
                print("Addition operation will result in a float number: " + str(float(a)+float(b)))
            else:
                print("Second input is also an integer!")
                print("Addition operation will result in a integer number: " + str(int(a)+int(b)))

        except:
            #Input 'b' is not a float or int, hence it is string
            #You cannot add integer with string
            print("Second input is a string!")
            print("You cannot do the addition operation between integer and string!!!!")


except:
    #Input 'a' is not a float, hence it is string
    print("First input is a string!")
    try:
        #Check whether the input 'b' is float/int
        #Since both int and float can be converted into float
        y = float(b)
        if b == str(float(b)):
            print("Second input is a float!")
            print("You cannot do the addition operation between a string an a float!!!!")
        else:
            print("Second input is an integer!")
            print("You cannot do the addition operation between a string and an integer!!!!")


    except:
        print("Second input is also a string!")
        #Input 'b' is not a float or int, hence it is string
        #Concatanate the string then
        print("Both of the inputs are strings hence result will be concatanated as follows: " + str(a+b) )           

"""
7) **Cubes**
Create a list of the cubes of *x* for *x* in *[0, 10]* using:
a) a for loop
"""
cubesListwithLoop = []
for i in range(0,11):
    cubesListwithLoop.append(i**3)
print(cubesListwithLoop)
    

"""
7) **Cubes**

Create a list of the cubes of *x* for *x* in *[0, 10]* using:
b) a list comprehension
"""
cubesListwithComprehension = [i**3 for i in range(0,11)]
print(cubesListwithComprehension)

"""
8) **List comprehension**

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
"""

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

ListComprehension = [(x,y) for x in range(3)  for y in range(4)]
print(ListComprehension)

"""
9) **Nested list comprehension**

> A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).

Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.
"""

PythagoreanTriple = [d for d in [(x,y,z) for x in range(1,100) for y in range(1,100) for z in range(0,100)if x**2 + y**2 == z**2 and x < z and y < z] if d[0] < d[1]]
print(PythagoreanTriple)

"""
10) **Normalization of a N-dimensional vector**

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).
"""

import math as m
vector = (1083, 1406, 585, 812, 1301, 1147, 246, 427, 1385, 699, 254, 1417, 1477, 148, 1068, 306, 954, 5, 1362, 1416, 1247, 1287, 1216, 250, 693, 1284, 843, 944, 1362, 1442, 1208, 149, 601, 425, 96, 1065, 3, 721, 903, 627, 746, 292, 474, 375, 1259, 618, 123, 145, 139, 174, 1012, 608, 769, 841, 612, 1090, 1257, 356, 1233, 1411, 295, 471, 1145, 150, 1208, 357, 904, 207, 343, 803, 671, 402, 508, 126, 934, 649, 1221, 71, 1015, 1257, 1414, 643)
v = list(vector)
squared_summation = 0

for i in range(0,len(v)):
    squared_summation += v[i]**2
    
rooted_squared_sum = m.sqrt(squared_summation)

for i in range(0,len(v)):
    v[i] = v[i] / rooted_squared_sum
    
vector = tuple(v)
print("After the normalization process we retrieved norms as follows:")
print(vector)
    
probabilistic_sum = 0
for i in range(0, len(vector)):
    probabilistic_sum += vector[i]**2

print("After the normalization process, summation of the norms are: " + str(probabilistic_sum))

"""
11) **The Fibonacci sequence**

Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.
"""

FibonacciNumbers = []
counter = 0
while counter < 20:
    if counter == 0:
        FibonacciNumbers.append(counter)
        counter += 1
    elif counter == 1:
        FibonacciNumbers.append(counter)
        counter += 1
    else:
        FibonacciNumbers.append(FibonacciNumbers[counter-2] + FibonacciNumbers[counter-1])
        counter += 1
print(FibonacciNumbers)

