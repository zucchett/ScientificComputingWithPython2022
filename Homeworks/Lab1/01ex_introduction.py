import math

print("#####################EX1#####################")
#ex1
tmp = [] #empty list
for i in range(1,101,1):
 
	if(i%5 == 0 and i%3 == 0): #multiple of 5 and 3
		print("HelloWorld")
		tmp.append("HelloWorld")
	elif(i%3 == 0): #multiple of 3
		print("Hello")
		tmp.append("Hello")
	elif(i%5==0):  #multiple of 5
		print("World")
		tmp.append("World")

	else:  #other cases
		print(i)
		tmp.append(i)
		
results_original = tuple(tmp)  #cast to tuple 	

for i in range(len(tmp)):  #substitute the words 
	if(tmp[i] == "Hello"):
		tmp[i] = "Python"
	elif(tmp[i] == "World"):
		tmp[i] = "Works"
		
result_substituted = tuple(tmp)  #cast to tuple 

print("Results with replacements = " + str(result_substituted))

print("#####################EX2#####################")

#ex2

x = input("Set the value of x: ") 
y = input("Set the value of y: ") 

print("(x,y) = (" + str(x) + ","+str(y)+")")

x,y = y,x

print("(x,y) after swap = (" + str(x) + "," + str(y)+")")

print("#####################EX3#####################")

#ex3

v=(3,0)
u=(10,5)

print("v = " + str(v))
print("\nu = " + str(u))


dist = math.sqrt((v[0] - u[0])**2 + (v[1] - u[1])**2 )

print("\nDistance = " + str(dist))

print("#####################EX4#####################")

#ex 4

s1 = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."

s2 = "The quick brown fox jumps over the lazy dog"

#ignoring differences in capitalization
s1 = s1.upper()  
s2 = s2.upper() 

print(s1)

tuples1=set() #empty set used to avoit duplicates

for char in s1: #for each char in the string 
	
	count = s1.count(char) #count the number of occurrences
	
	tuples1.add((char,count)) #add a tuple with (char, count) to the list 
	
print("\nCounter for string 1 = " + str(tuples1))

print("\n\n")
print(s2)
tuples2=set() #same for string 2


for char in s2: 
	count = s2.count(char)
	
	tuples2.add((char,count))
	
print("\nCounter for string 2 = " + str(tuples2))

print("#####################EX5#####################")

#ex5

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,85, 63, 47, 56, 42, 70,84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91, 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41, 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
unique = set() #empty set
count = [] #empty list
print(l)
for element in l:#avoiding to have duplicates using the set
	
	unique.add(element)

for element in unique: #count the occurrences of the not-duplicated element in the original list
	
	count.append((element, l.count(element)))

print("Counter = "+str(count))
	
print("#####################EX6#####################")

#ex6

#try to cast the input to an integer, if not possible -> error message
try:

	x = int(input("Set the value of x: ")) 
except:
	print("incorrect format of the input for x")
	
try:

	y = int(input("Set the value of y: "))
except:
	print("incorrect format of the input for y")

print("#####################EX7#####################")

#ex7


cubes1 = []

for i in range(11):

	cubes1.append(i**3)

cubes2=[x**3 for x in range(11)]

print(cubes1)
print(cubes2)

print("#####################EX8#####################")

#ex8

a = [(i,j) for i in range(3) for j in range (4)]

print(a)

print("#####################EX9#####################")

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

print("#####################EX10#####################")

#ex10

vect = [10.0,5.0,11.0]

norm = 0 

for i in vect:#norm^2 = x1^2 + x2^2 + ... +xn^2
	norm = norm + i**2 
	
norm = math.sqrt(norm) #norm = (norm^2)^0.5

vect_normalized= [x/norm for x in vect] #normalization, i.e., dividing each element by the norm

check = 0

for i in vect_normalized:
	check = check + i**2

print("Vector = " + str(vect) + "with norm " + str(norm) + "->normalized = " + str(vect_normalized))
	
print("Check the norm of the normalized vector: " + str(check))

print("#####################EX11#####################")

#ex11

fib = [0, 1] #base case

l = 2 

while l < 20: #until there aren't 20 elements in the list
	
	fib.append(fib[l-1] + fib[l-2]) #fib_i = fib_(i-1) + fib_(i-2)
	l = len(fib) #update the list lenght

	
print("FIrst 20 number in the Fiboncci sequence = " + str(fib))


		
