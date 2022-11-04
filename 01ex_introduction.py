# ********** Question 1 **********

print("Question 1")
lst = []
for i in range(1, 101):
<<<<<<< HEAD
    if((i % 3 == 0) and (i % 5 == 0)): # check if they are divisible by 3 and 5
=======
    if((i % 3 == 0) and (i % 5 == 0)):
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
        print("HelloWorld")
        lst.append("HelloWorld")
    elif(i % 3 == 0):
        print("Hello")
        lst.append("Hello")
    elif(i % 5 == 0):
        print("World")
        lst.append("World")
    else:
        print(i)
        lst.append(i)

temp_tuple = tuple(lst)

<<<<<<< HEAD
for i in range(len(lst)): # change the index
=======
for i in range(len(lst)):
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
    if(lst[i] == "HelloWorld"):
        lst[i] = "PythonWorks"
    elif(lst[i] == "Hello"):
        lst[i] = "Python"
    elif(lst[i] == "World"):
        lst[i] = "Works"

result = tuple(lst)
print(result)


# ********** Question 2 **********

print("Question 2")
print('Enter first term')
x = input()
print('First term: ',  x)
print('Enter second term:')
y = input()
print('Second term: ',  y)
<<<<<<< HEAD
x, y = y, x  # changes the variable values
=======
x, y = y, x
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
print('Switched first term: ',  x)
print('Switched second term: ',  y)


# ********** Question 3 **********

print("Question 3")
import math

def euclideanDistance(x, y):
    a = (x[0] - y[0])**2
    b = (x[1] - y[1])**2
    c = math.sqrt(a + b)
    return c

u = (3,0)
v = (0,4)
result = euclideanDistance(u,v)
print(result)


# ********** Question 4 **********

print("Question 4")
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

<<<<<<< HEAD
# number of chars and chars are hold in two seperate lists
=======
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
char_list = []
number_list = []

for i in s1:
    found = 0
    for j in range(len(char_list)):
        if i == char_list[j]:
<<<<<<< HEAD
            number_list[j] += 1 # if the char is found, the number is incremented
            found = 1
    if found == 0: # if the chars is seen for the first time it is added to the list
=======
            number_list[j] += 1
            found = 1
    if found == 0:
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
        char_list.append(i)
        number_list.append(1)

for i in range(len(char_list)):
    print(char_list[i] , ": " , number_list[i])


# ********** Question 5 **********

print("Question 5")
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

<<<<<<< HEAD
unique_set = set(l) # sets do not hold duplicate elements so every element will be unique
=======
unique_set = set(l)
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
print(unique_set)
print("Number of unique numbers: " , len(unique_set))


# ********** Question 6 **********

print("Question 6")
print('Enter first term')
x = input()
print('Enter second term:')
y = input()

try:
    x=float(x)
    y=float(y)
    print(x + y)
except:
    print('addition cannot be done')


# ********** Question 7 **********

print("Question 7")
cubes_a = []
for i in range(11):
    cubes_a.append(i**3)
print(cubes_a)


# ********** Question 8 **********

print("Question 8")
a = [(i, j) for i in range(3) for j in range(4)]
print(a)


# ********** Question 9 **********

print("Question 9")
pythagoras_list = [(i,j,math.sqrt(i*i + j*j)) for i in range(1,100) for j in range(1,100) if math.sqrt(i*i+j*j) % 1 == 0 and math.sqrt(i*i+j*j) < 100 and i < j ]
  
print(pythagoras_list)


# ********** Question 10 **********

print("Question 10")
def normalize( vec ):
    dimension = len(vec)
    length_list = [vec[i]**2 for i in range(dimension)]
    length_total = sum(length_list)
<<<<<<< HEAD
    vector_length = math.sqrt(length_total) # length of vector input is found
    ratio = 1 / vector_length # the ratio between unit vector and input vector is found
    for i in range(dimension):
        length_list[i] = vec[i]*ratio # every component of vector is decreased proportional to that ratio
=======
    vector_length = math.sqrt(length_total)
    ratio = 1 / vector_length
    for i in range(dimension):
        length_list[i] = vec[i]*ratio
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
    return(length_list)

vector_input = (4,6,8,10)
print("vector input: ", vector_input)
print("normalized: ", normalize(vector_input))


# ********** Question 11 **********

print("Question 11")
term1 = 0
term2 = 1
count = 0
<<<<<<< HEAD
while count < 20: # loop repeats 20 times and add two last elements at every iteration
=======
while count < 20:
>>>>>>> ac075f197586ffff6bf50d43c9723a4ea96e2ecb
    print(term1)
    termlast = term1 + term2
    # update values
    term1 = term2
    term2 = termlast
    count += 1