""" 

Q1 - A

"""

n = 1
tuple_list = []
while n < 101:
    if n % 3 == 0 and n % 5 == 0:
        print("HelloWorld")
        tuple_list.append("HelloWorld")
    elif n % 3 == 0:
        print("Hello")
        tuple_list.append("Hello")
    elif n % 5 == 0:
        print("World")
        tuple_list.append("World")
    else:
        print(str(n))
        tuple_list.append(str(n))
    n += 1
    
    
    
    """ 
    Q1 - B 
    """
    
for index in range(0,len(tuple_list)):
    if tuple_list[index] == "HelloWorld":
        tuple_list[index] = "PythonWorks"
    elif tuple_list[index] == "Hello":
        tuple_list[index] = "Python"
    elif tuple_list[index] == "World":
        tuple_list[index] = "Works"
    else:
        tuple_list[index] = tuple_list[index]
tuple_formation = tuple(tuple_list)
print(tuple_formation)

"""
Q2 

"""

x = input("Please enter the first variable: ")
y = input("Please enter the second variable: ")

before_x = x
before_y = y
x,y = y,x
print("Before swapping x value was " + before_x + ", after swapping x value is " + x)
print("Before swapping y value was " + before_y + ", after swapping x value is " + y)

""" 
Q3

""" 

import math as m
u = (3,0)
v = (0,4)

euclidian_distance = m.sqrt(((v[0] - u[0])**2) + ((v[1] - u[1])**2))
print(euclidian_distance)

""" 
Q4 

"""

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

new_sentence = s1.lower()
new_sentence_second = s2.lower()
unique = []
unique_second = []

for element in new_sentence:
    if element not in unique:
        unique.append(element)
for el in unique:
    print("Current character of " + el +" occured " + str(new_sentence.count(el)) + " time(s) in the sentence.")
print("")
for element in new_sentence_second:
    if element not in unique_second:
        unique_second.append(element)
for el in unique_second:
    print("Current character of " + el +" occured " + str(new_sentence_second.count(el)) + " time(s) in the sentence.")
    
    
""" 

Q5 

""" 

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


unique = []
for element in l:
    if element not in unique:
        unique.append(element)

print("Unique Numbers: " + str(unique))
print (" ")
print("Number of unique numbers are " + str(len(unique)))


"""

Q6 

"""

import math

a = input()
b = input()
try:
    a=float(a)
    if a%1==0:
        a=int(a)
        print(a,"=Int")
    else: 
        print(a,"=Float")
    try:
        b = float(b)
        if b%1==0:
            b=int(b)
            print(b,"=Int")
        else:
            print(b,"=Float")
        print(a+b)
    except:
        b = str(b)
        print(b,"= String")
        print("Values of different types exist.")
except:
    a = str(a)
    print(a,"= String")
    try:
        b = float(b)
        if y%1==0:
            b=int(b)
            print(b,"=Int")
        else:
            print(b,"=Float")
        print("Values of different types exist.")
    except:
        b = str(b)
        print(b,"= String")
        print(a+b)
    
            
""" 

Q7 - A 

"""

l =[]
for x in range(0,11):
    l.append(x*x*x)
    
print(l)    

""" 

Q7 - B 

""" 
cube = [x*x*x for x in range(11)]
print(cube) 


""" 
Q8 

"""

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)


a= [(i, j) for i in [0,1,2] for j in [0,1,2,3]]
print (a)

"""

Q9 

""" 


pyt =[el for el in [(a,b,c) for c in range(0,100) for a in range(1,100) for b in range(1,100) if c*c == a*a + b*b] if el [0]< el [1]]

tlist = tuple(pyt)
print (tlist)


""" 
Q10 

""" 

import math as m

def Normalization(V):
    squared_sum = 0
    for el in range(0,len(V)):
        squared_sum += V[el]**2
    Vlen= m.sqrt(squared_sum)

    normalized_list = []
    for el in range(0,len(V)):
        normalized_list.append(V[el]/Vlen)
    V = tuple(normalized_list)
    print(V)
    normalized = 0
    for el in range(0,len(V)):
        normalized += V[el]**2
    print("Normalized process is achieved since all squared sums equal to: " + str(normalized)) 


V = (1049,786,1231,123141,354536,6786786,34234234,7538475,1123235234)
Normalization(V)



""" 
Q11

""" 

x = 0
y = 1
z = 0 
n = 20
fibonacci = []
fibonacci.append(x)
fibonacci.append(y)

z = x + y 
n = n - 2 

while n > 0:
    fibonacci.append(z)
    x = y
    y = z
    z = x+y
    n = n-1

print("The Fibonacci Sequence : " +  str(fibonacci))



