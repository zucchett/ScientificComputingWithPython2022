#The Hello World Replacement
#a)
print("===========a==========")
list1 = []
for x in range(1, 101):
    str1 = ''
    if x % 3 == 0: 
        str1 += "Hello"
        list1.append('Hello')
    if x % 5 == 0:
        str1 += "World"
        list1.append("World")
    elif x % 3 != 0 and x % 5 != 0:
        str1 += str(x)
        list1.append(x)
    print(str1)


# b)
print("===========b==========")
def convert(list1):
    return tuple(list1)

print(tuple(list1))
for i in range(len(list1)):
    if list1[i] == 'Hello':
        list1[i] = 'Python'
    if list1[i] == 'World':
        list1[i] = 'Works'
print(tuple(list1))


#2-The Swap
nr1 = 1
nr2 = 2
nr1, nr2 = nr2, nr1
print("nr1 = ", nr1)
print("nr2 = ", nr2)

#3-Computing distance
import math
t1 = (3,0)
t2 = (0,4)
distance = math.sqrt(((t1[0]-t2[0])**2)+((t1[1])-t2[1])**2)
print(distance)

#4-Counting letters
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

#each character occuerrencies for the frist string
print("The original first sentence is: " +s1)
x=[]
res = dict()
for i in s1:
    x.append(i.lower())
a = list(set(x))
for i in a:
    res[i] = x.count(i)
    
print("Occurencies are: " + str(dict(res)))

#each character occuerrencies for the second string
print("The original second sentence is: " +s2)
x=[]
res = dict()
for i in s2:
    x.append(i.lower())
a = list(set(x))
for i in a:
    res[i] = x.count(i)
    
print("Occurencies are: " + str(dict(res)))


#5-Isolating the unique
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

#will be used to store the unique values
l1 = []

count = 0

for i in l:
    if i not in l1:
        count += 1
        l1.append(i)
print("The unique values in the list are:", count)

#Second method using python data structures
unique_value = len(set(l))
print("The values that are unique are:", unique_value)



#6-Casting
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
    print("The addition of the two variables:", variable1 + variable2)  # if possible
except:
    print("The addition of these two variables is not possible.")


#7-Cubes
list = [1,2,3,4,5,6,7,8,9,10]

#using a for loop
cubes = []
for i in list:
    cubes.append(i**3)
print("Cubes using a for loop:", cubes)    
    
#using a list comprehension
list_cube = [i**3 for i in list]
print("Cubes using a list comprehension:", list_cube)



#8-List comprehension
a = [(i,j) for i in range(3) for j in range(4)]
print(a)


#9-Nested list comprehension
lis=[]
for a in range(1, i):
    for b in range(a + 1, i// 2):
        for c in range (b + 1, i - a - b):
            lis.append([a,b,c])
print(lis) 



#10-Normalization of a N-dimensional vector
def normalize(vector):
    sqrsum = sum([i*i for i in vector])
    return tuple([i/math.sqrt(sqrsum) for i in vector])

print("The normalization of the vector", normalize((5, 6, 7)))



#11-The Fibonacci sequence
     
fibonacci = [0,1]
for i in range(2, 21):
    nr = fib[i-1] + fib[i-2]
    fibonacci.append(nr)
print(fibonacci)    


