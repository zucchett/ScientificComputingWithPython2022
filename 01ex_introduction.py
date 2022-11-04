
print("ex. 1")

list=[]
for i in range (1,101,1):
	if i%3==0 and i%5==0:
		print("HelloWorld")
		list.append("HelloWorld")
	elif i%3==0:
		print("Hello")
		list.append("Python")
	elif i%5==0:
		print("World")
		list.append("Works")
	else:
		print(i)
		list.append(i)
		
print("This is the original list: ", list)
        
print("This is the tuple with substitution: ", tuple(list))





print("ex. 2")

x=input("Enter value x: ")
y=input("Enter value y: ")
x, y = y, x

print(x, y)





print("ex. 3")

import math
print("This program calculate the distance between two points u and v in a 2D euclidean space.")

u=(int(input("Write the x coordinate of the point u: ")), int(input("Write the y coordinate of the point u: ")))
v=(int(input("Write the x coordinate of the point v: ")), int(input("Write the y coordinate of the point v: ")))

d=math.sqrt( (v[0]-u[0])**2 + (v[1]-u[1])**2 )

print("This is the calculate distance between u and v insered: ", d)




print("ex. 4")

s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

#ignore differences in capitalization
s1, s2 = s1.lower(), s2.lower()

#create an empty set to count characters (set do not support duplicates)
numberchars1=set()

for i in s1:
	ripetitions1=s1.count(i)
	charwithrips1=str(i)+"="+str(ripetitions1)
	numberchars1.add(charwithrips1)

#same thing for s2
numberchars2=set()

for i in s2:
	ripetitions2=s2.count(i)
	charwithrips2=str(i)+"="+str(ripetitions2)
	numberchars2.add(charwithrips2)

print(numberchars1)
print(numberchars2)





print("ex. 5")

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85, 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

#create an empty set to count characters (set do not support duplicates)
numbercharl=set()

for i in l:
	ripetitionl=l.count(i)
	charwithripl=str(i)+"="+str(ripetitionl)
	numbercharl.add(charwithripl)
	
print(numbercharl)

print("ex. 5 - second part2")

charunique= { }

for i in l:
	
	charunique[i]=l.count(i)
	
print(charunique)





print("ex. 6")

x1 = input("Inser first variable: ")
x2 = input("Inser second variable: ")

try:
	x1 = float(x1)
	x2 = float(x2)
	
except:
	print("Insert two floating number.")
	




print("ex. 7 - Using loop.")

cubes1=[]
for x in range(11):
	cubes1.append(x**3)
	
print(cubes1)

print("ex. 7 - Using list comprehension.")

cubes2=[x**3 for x in range(11)]

print(cubes2)





print("ex. 8")

a=[(i, j) for i in range(3) for j in range(4)]

print(a)




print("ex. 9")

pytTriplet = [(a,b,c) for a in range(1, 100) for b in range(a, 100) for c in range (b, 100) if a**2 + b**2 == c**2]
	
tuple(pytTriplet)

print(pytTriplet)




print("ex. 10")

import random
from math import sqrt

dim=int(input("Inser the vector dimension: "))

vector=[]

for i in range (dim): #creation of an n-dimentional vector
	singularDimention=random.randint(0, 10)
	vector.append(singularDimention)
	
print(vector)

normFactor=0
for i in vector:
    normFactor += i**2

normFactor = sqrt(normFactor)

versor= []

for i in range (dim):
    versor.append(singularDimention/normFactor)
    
print(versor)
	
	


print("ex. 11")

listFib = [0, 1] #The sequence commonly starts from 0 and 1

i=2

while i < 20:
	listFib.append(listFib[i-1]+listFib[i-2])
	i += 1
	
print(listFib)


