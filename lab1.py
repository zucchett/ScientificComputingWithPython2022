
import math

print("******************* Question 1 *********************")

my_list = []

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("HelloWorld!")
        my_list.append("HelloWorld!")
    elif i%3 == 0 and i%5 != 0:
        print("Hello")
        my_list.append("Python")
    elif i%3 != 0 and i%5 == 0:
        print("World")
        my_list.append("Works")
    else:
        print(i)
        my_list.append(i)
        
print("-------------------------------------------------")

my_tupple = ()

my_tupple = tuple(my_list)

print(my_tupple)

print("******************* Question 2 *********************")

y = input("Give me value of x: ")
x = input("Give me value of y: ")

print("x: " +  x)
print("y: " +  y)

print("******************* Question 3 *********************")

x = (0, 4)
y = (3, 0)

distance = math.sqrt(pow(abs(x[0] - y[0]), 2) + pow(abs(x[1] - y[1]), 2))
print(distance)

print("******************* Question 4 *********************")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

my_list = list()
my_flag = 0

for i in s1.upper():
    if len(my_list) != 0:
        for j in my_list:
            if j[0] == i:
                j[1] = j[1] + 1
                my_flag = 1
        if my_flag == 0:
            my_list.append([i, 1])
        my_flag = 0
    else:
        my_list.append([i, 1])

print(my_list)

print("******************* Question 5 *********************")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

my_list = []

for i in l:
    my_list.append(str(i))
    
my_uniques = []

for i in my_list:
    if (len(set(i)) == len(i)):
        my_uniques.append(int(i))
    else:
        continue

print(my_uniques)

print("******************* Question 6 *********************")

x = input("Give me value of x: ")
y = input("Give me value of y: ")

try:
    z = int(x) + int(y)
    print(z)
except:
    try:
        z = float(x) + float(y)
        print(z)
        
    except:
        try:
            z = str(x) + str(y)
            print(z)
            
        except:        
            print("You can not add string and integer or string and float")

print("******************* Question 7 *********************")

my_list = []

for i in range (0, 11):
    my_list.append(pow(i, 3))
print(my_list)

print("******************* Question 8 *********************")

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

my_list = [(i, j) for i in range(3) for j in range(4)]
print(my_list)

print("******************* Question 9 *********************")

my_list = []
for c in range(1, 100):
    for a in range(1, c):
        for b in range(1, c):
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                my_list.append((a, b, c))
        
print(my_list)

print("******************* Question 10 *********************")

def vectorLength(vec):
    length = 0
    for i in vec:
        length = length + i**2
    return math.sqrt(length)

def normalise(vec, length):
    new_list = []
    frequency = 1/length
    for i in vec:
        new_list.append(i*frequency)
    return new_list

vec = (1, 2, 3, 4, 7)

length = vectorLength(vec)

vector_norm = normalise(vec, length)

print("Vector: ", vec)
print("Normalised Vector:", vector_norm)

print("******************* Question 11 *********************")

i=0
j=1
count = 0
while count <= 20:
    print(i)
    k = i + j
    i = j
    j = k
    count += 1