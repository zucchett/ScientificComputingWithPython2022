

print("**********EXERCISE 1**************")

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        result = "HelloWorld"
        print(result)
    elif num % 3 == 0:
        result = "Hello"
        print(result)
    elif num % 5 == 0:
        result = "World"
        print(result)
    else:
         print(num)

result = []

for num_1 in range(1, 100):
    if num_1 % 3 == 0 and num % 5 == 0:
        result.append("Python Works")
#         print(result)
    elif num_1 % 3 == 0:
        result.append("Python")
#         print(result)
    elif num_1 % 5 == 0:
        result.append("Works")
#         print(result)
    else:
         result.append(num_1)
            

print(tuple(result))


print ("***********EXERCISE 2*************")

x = 52
y = 14
print("x =", x )
print("y =", y )

x, y = y, x
print("New value of x =", x)
print("New value of y =", y)

print("***********EXERCISE 3***********")
import math
u = (3, 0)
v = (0, 4)

def eucl_distance(u, v):
    return math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2)

print("Euclidean distance :", eucl_distance(u, v))


print("************EXERCISE 4*************")
# we iterate through the string and create a key in a dictionary for each newly occurring element. 
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"
freq_s1 = {}
freq_s2 = {}
  
for i in s1:
    if i in freq_s1:
        freq_s1[i] += 1 #If the element has already appeared, increase its value by 1 instead.

    else:
        freq_s1[i] = 1
print ("Count of each character in s1 is :\n ",  str(freq_s1))

for i in s2:
    if i in freq_s2:
        freq_s2[i] += 1 #If the element has already appeared, increase its value by 1 instead.

    else:
        freq_s2[i] = 1
print ("Count of each character in s2 is :\n ",  str(freq_s2))


print("***********EXERCISE 5*********")
# Program that counts unique numbers in the list

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
new_l = []

count = 0

for i in l:
    if i not in new_l:
        count = count + 1
        new_l.append(i)

print("No. of unique numbers are:", count)

print("************EXERCISE 6*************")
#CASTING
#var_1 = int(input("1st variable: "))
#var_2 = int(input("2nd variable: "))
#var_3 = str(input("3rd variable: "))

#print("Addition: ", var_1 + var_2)

print("***********EXERCISE 7***********")
#list of cubes with for loop
cube_1 = []
for i in range(1, 11):
    cube_1.append(i**3)
print (cube_1)

#list of cubes with list comprehension

cube_2 = [i**3 for i in range(1, 11)]
print(cube_2)

#print(map(lambda x: x**3, range(1, 11)))

print("*********EXERCISE 8************")

print([(i, j) for i in range(3) for j in range(4)])

print("**********EXERCISE 9*************")

pythgn_trpls = [(a, b, c) for a in range(1, 100)for b in range(1, 100)for c in range(1, 100)if a**2 + b**2 == c**2]
print ("unique Pythagorean triples;" "\n", tuple(pythgn_trpls))


#pythgn_trplss = [(a, b, c) for a in range(1, 100)for b in range(a, 100)for c in range(b, 100)if a**2 + b**2 == c**2]
#print(pythgn_trplss)

print("**************EXERCISE 10*************")
#Normalizaiton

def f(norm):
    s = 0
    for x in norm:
        s += x
    return [x/s for x in norm]

norm = [1,2,3,4]
print(f(norm))


print ("************EXERCISE 11**************")
#Fibonacci Sequence using for loop

def loopFibonacci(num):
  #store the first two fixed terms in a list
    fib = [0, 1]
    for i in range(2, num+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib
 
print("1st 20 numbers of fibonacci sequence: ", "\n", loopFibonacci(20))


