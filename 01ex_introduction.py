#Matteo Cogato
#2026966

#es1
print("\n###################### ES1 ##########################")

list1=[]
for i in range(100):
	x = i+1
	if((x%5 == 0) and (x%3 == 0)):
		print("HelloWorld")
		list1.append("HelloWorld")
	elif (x%3 == 0):
		print("Hello")
		list1.append("Hello")
	elif (x%5 == 0):	
		print("World")
		list1.append("World")
	else:
		print(x)
		list1.append(x)

tuple_original = tuple(list1)

for i in range(len(list1)):
	if(type(list1[i]) == str):
		list1[i] = list1[i].replace( "Hello","Python")
		list1[i] = list1[i].replace( "World","Works")
	
tuple_final = tuple(list1)
print("Substituted tuple:",tuple_final)

#es2
print("\n###################### ES2 ##########################")

print("Insert values:")
x=input("x: ")
y=input("y: ")
x,y = y,x
print("Swap values:")
print("x:", x)
print("y:", y)

#es3
print("\n###################### ES3 ##########################")

import math

u=(3,0)
v=(0,4)
print("Input points:")
print("u:",u)
print("v:",v)


def distance(u,v):
	
	x1 = (u[0]-v[0])**2
	x2 = (u[1]-v[1])**2
	d = math.sqrt(x1+x2)
	print("Distance: ", d)
	return d
	
distance(u,v)

#es4
print("\n###################### ES4 ##########################")

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.lower()
characters = set([x for x in s1])
count1 = []
for x in characters:
	occurences = s1.count(x)
	count1.append((x,occurences))
print("OCCURENCES s1:\n", count1)

s2 = s2.lower()
count2 = []
characters = set([x for x in s2])
for x in characters:
	occurences = s2.count(x)
	count2.append((x,occurences))
print("\nOCCURENCES s2:\n", count2)


#es5
print("\n###################### ES5 ##########################")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
set1 = set(l)
unique = []
for x in set1:
	occurences = l.count(x)
	if(occurences==1):
		unique.append(x)

print("The unique numbers in the list are: ", len(unique))
print("They are:", unique)

#es6
print("\n###################### ES6 ##########################")

x=input("x: ")
y=input("y: ")


try:
	x = float(x)
	print("x is a number")

except:
	print("x is a string")		
try:
	y = float(y)
	print("y is a number")

except:
	print("y is a string")	

try:
	c=x+y
	print("c=x+y=",c)

except:
	print("x and y are incompatible types")

#es7
print("\n###################### ES7 ##########################")

cubes1 = []
for x in range(11):
	cubes1.append(x**3)
print("Using a for loop:")
print(cubes1)

cubes2 = [x**3 for x in range(11)]
print("Using a a list comprehension:")
print(cubes2)

#es8
print("\n###################### ES8 ##########################")

print([(x,y) for x in range(3) for y in range(4)])

#es9
print("\n###################### ES9 ##########################")

print("Pythagorean triple with c<100:")

tuple1 = tuple([(a,b,c) for a in range(1,100) for b in range(1,100) for c in range (1,100) if (a**2+b**2==c**2) and a<=b]) #to avoid (3,4,5) and (4,3,5)
print(tuple1)


#es10
print("\n###################### ES10 ##########################")

vect = (1,2,1,6)
print("Vector:", vect)

total = 0
for x in vect:
	total = total + x**2


root_total = math.sqrt(total)

norm_vect = [x/root_total for x in vect]
print("Nomalized vector:" , norm_vect)

check = 0
for x in norm_vect:
	check = check + x**2
	
print("Check: ", check)

#es11
print("\n###################### ES11 ##########################")

x1 = 0
x2 = 1
fibonacci = [x1,x2]
while len(fibonacci)<20:
	x2,x1 = x1+x2,x2
	fibonacci.append(x2)
print("First 20 numbers of the Fibonacci sequence:\n",fibonacci)

































