import math

#ex1
tmp = []
for i in range(100):

	j = i + 1 
	if(j%5 == 0 and j%3 == 0):
		print("HelloWorld")
		tmp.append("HelloWorld")
	elif(j%3 == 0):
		print("Hello")
		tmp.append("Hello")
	elif(j%5==0):
		print("World")
		tmp.append("World")

	else:
		print(j)
		tmp.append(j)
		
results_original = tuple(tmp)
print(results_original)	

for i in range(len(tmp)):
	if(tmp[i] == "Hello"):
		tmp[i] = "Python"
	elif(tmp[i] == "World"):
		tmp[i] = "Works"
		
result_substituted = tuple(tmp)

print(result_substituted)

print("################################################")

#ex2

x = input("Set the value of x: ") 
y = input("Set the value of y: ") 

print(str(x) + ","+str(y))

x,y = y,x

print(str(x) + ","+str(y))

print("################################################")

#ex3

v=(3,0)
u=(10,5)

print(str(v) + " " + str(u))

dist = math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2 )

print(dist)

print("################################################")

#ex 4

s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

s1 = s1.upper() 
s2 = s2.upper() 

print(s1)

tuples1=[]
for char in s1:

	count = s1.count(char)
	
	tuples1.append((char,count))
	
print(tuples1)

tuples2=[]
for char in s2:

	count = s2.count(char)
	
	tuples2.append((char,count))
	
print(tuples2)

print("################################################")

#ex5

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,85, 63, 47, 56, 42, 70,84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20] 
 
unique = set()
count = []
for element in l:
	
	unique.add(element)

for element in unique:
	
	count.append((element, l.count(element)))

print(count)
	
print("################################################")

#ex6


try:

	x = int(input("Set the value of x: "))
except:
	print("incorrect format of the input")
	
try:

	y = int(input("Set the value of y: "))
except:
	print("incorrect format of the input")

print("################################################")

#ex7

cubes1 = []

for i in range(11):

	cubes1.append(i**3)

cubes2=[x**3 for x in range(11)]

print(cubes1)
print(cubes2)

print("################################################")

#ex8

a = [(i,j) for i in range(3) for j in range (4)]

print(a)

print("################################################")

#ex9

abc_list = []
c = 99

while(c>0):

	for a in range(c):
	
		b = math.sqrt(c**2 - a**2)

		condition1 = (b - int(b)) == 0
		
		condition2 = ((a*b) % 12 == 0 and (a*b*c) % 60 == 0)
		
		if(condition1 and condition2 and b > 0 and a < b and a > 0):
			abc_list.append((a,int(b),c))

	c = c - 1


print(abc_list)

print("################################################")

#ex10

vect = [10,5,11]

norm = 0

for i in vect:
	norm = i**2
	
norm = math.sqrt(norm)

vect = [x/norm for x in vect]

check = 0

for i in vect:
	check = i**2
	
print(check)

print("################################################")

#ex11

fib = [0, 1]

while len(fib)<20:
	
	l = len(fib)

	fib.append(fib[l-1] + fib[l-2])
	
print(fib)


		
