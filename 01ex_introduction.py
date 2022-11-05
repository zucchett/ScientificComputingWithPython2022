import math

"""
Exercise 1, points a and b
"""

print("Exercise 1, points a and b")
print()

hundred_numbers = [x for x in range(1, 101)]

for i in range(len(hundred_numbers)):
    if hundred_numbers[i] % 5 == 0 and hundred_numbers[i] % 3 == 0:
        hundred_numbers[i] = "HelloWorld"
    elif hundred_numbers[i] % 5 == 0:
        hundred_numbers[i] = "World"
    elif hundred_numbers[i] % 3 == 0:
        hundred_numbers[i] = "Hello"
        
print("The answer to point a) is: \n", hundred_numbers)
print()

for i in range(len(hundred_numbers)):
    if hundred_numbers[i] == "Hello" :
        hundred_numbers[i] = "Python"
    elif hundred_numbers[i] == "World" :
        hundred_numbers[i] = "Works"    
               
tuple_numbers = (*hundred_numbers,)             # to put a list content in a tuple content

print("The answer to point b) is: \n", tuple_numbers)
print()

"""
Exercise 2
"""

print("Exercise 2")
print()

x = input("Set the value of x: ") # remember to type Enter
y = input("Set the value of y: ") # remember to type Enter

x, y = y, x

print("x =", x, ", y =", y)
print()

"""
Exercise 3
"""

print("Exercise 3")
print()

u_list = []  
v_list = []

u_list = [float(item) for item in input("Enter the coordinates of the first point as x,y: ").split(",")]
v_list = [float(item) for item in input("Enter the coordinates of the second point as x,y: ").split(",")] 
print()

u = (*u_list,)
v = (*v_list,)

distance = math.sqrt( (u[0]-v[0])**2 + (u[1]-v[1])**2 )
 
print("The Euclidean distance between the points is: ", distance)
print()

"""
Exercise 4

"""

print("Exercise 4")
print()

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

list_s1 = list(s1.lower())
list_s2 = list(s2.lower())
list_s3 = list_s1

counter1 = {i:list_s1.count(i) for i in list_s1}
counter2 = {i:list_s2.count(i) for i in list_s2}

for i in range(len(list_s2)):
    list_s3.append(list_s2[i])
    
counter3 = {i:list_s3.count(i) for i in list_s3}

print("The number of each character in the first string: \n", counter1)
print()
print("The number of each character in the second string: \n", counter2)
print()
print("The number of each character in total: \n", counter3)
print()



"""
Exercise 5
"""

print("Exercise 5")
print()

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

unique_numbers=[]

for i in range(len(l)):
    j = 0
    count = 0
    while j < len(l):
        if l[i] == l[j]:
            count = count + 1
        j = j+1
    if count == 1:
        unique_numbers.append(l[i])

print("The unique numbers in the list are", len(unique_numbers), "and they are: \n", unique_numbers)
print()

counter_unique = {i:l.count(i) for i in l}
unique_values = [i for i in counter_unique if counter_unique[i]==1]

print("The unique values found exploiting the python data structures are", len(unique_values), "and they are: \n", unique_values)
print()

"""
Exercise 6
"""

print("Exercise 6")
print()

p = input("Set the first variable: ") 
q = input("Set the second variable: ")


try:
    p = int(p)
except:
    try:
        p = float(p)
    except:
        p = str(p)
       
try:
    q = int(q)
except:
    try:
        q = float(q)
    except:
        q = str(q)        
        
if (type(p)==int or type(p)==float) and (type(q)==int or type(q)==float):
    print("You are summing two numbers, the sum is: ", p+q) 
elif type(p)==str and type(q)==str:
    print("You are summing two strings, the sum is: ", p+q)
else:
    p = str(p)
    q = str(q)
    print("You are summing one string and one number, the number will be treated as a string. The sum is: ", p+q)       

print()
   
"""
Exercise 7
"""

print("Exercise 7")
print()

cubes1 = []

for i in range(11):
    cubes1.append(i**3)
    
print("The cubes obtained with the for loop are: \n", cubes1)
print()

cubes2 = [i**3 for i in range(11)] 

print("The cubes obtained with the list comprehension are: \n", cubes2) 
print() 

"""
Exercise 8
"""

print("Exercise 8")
print()

a = [(i, j) for i in range(3) for j in range(4)]

print(a)
print()

"""
Exercise 9
"""

print("Exercise 9")
print()

pitagora = []

pitagora = [(a, b, c) for a in range(1,101) for b in range(a+1,101) for c in range(101) if a**2+b**2==c**2]

print("The Pythagorean triples are: \n", pitagora)
print()

"""
Exercise 10
"""

print("Exercise 10")
print()

vector = []
sum = 0

vector = [int(item) for item in input("Enters the vectors components separated only by commas : ").split(",")]
print()

for i in range(len(vector)):
    sum = sum + vector[i]**2
    
norm = math.sqrt(sum)
    
vector_normalized = [vector[i]/norm for i in range(len(vector)) ]

print("The norm of your vector is: \n", norm)
print()
print("The normalized vector is: ", vector_normalized)
print()

sum2=0
for i in range(len(vector_normalized)):
    sum2 = sum2 + vector_normalized[i]**2
    
norm2 = math.sqrt(sum2)

print("The norm of this new vector is: ", norm2)
print()



"""
Exercise 11
"""
print("Exercise 10")
print()

fibonacci = [0]

n1 = 0
n2 = n1 +1

for i in range(19):
    fib = n1+n2
    fibonacci.append(fib)
    n1 = n2
    n2 = fib
    
print("The first 20 numbers of the Fibonacci sequence are: \n", fibonacci)
