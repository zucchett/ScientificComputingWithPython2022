# 01ex_introduction by Alberto Merotto 208117 v2
#*************************************************************
#Exercise 01:
mylist = []
for i in range(1,101):
	if (i%3 == 0 and i%5==0):
		print('HelloWorld')
		mylist.append('PythonWorks')
	else:
		if (i%3 == 0):
			print('Hello')
			mylist.append('Python')
		else:
			if (i%5 == 0):
				print('World')
				mylist.append('Works')
			else:
				print(i)
				mylist.append(i)
				
mytuple = tuple(mylist)
print('++++++++++++++++++++++++++++++++++++')
print(mytuple)
#*************************************************************				
#Exercise 02:
x = input()
y = input()
print(x,y)

x, y = y, x

print(x, y)
#*************************************************************				
#Exercise 03:
import math
u = (3, 0)
v = (0, 4)
print(u[0])
def euclidean_distance(u, v):
	distance = math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)
	return distance

print(euclidean_distance(u,v))

#*************************************************************				
#Exercise 04:
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def counting_letters(s):
	s = s.lower()
	mydict = {}
	for i in range(len(s)):
		if s[i] in mydict:
			mydict[s[i]] = mydict[s[i]] + 1
		else:
			mydict[s[i]] = 1
	return mydict

print(counting_letters(s1))
#*************************************************************				
#Exercise 05:
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 
def unique_isolator(l):
 	ue_list = []
 	for item in l:
 		if (l.count(item)==1):
 			ue_list.append(item)
 			
 	return ue_list

print(unique_isolator(l))
print(len(unique_isolator(l))) 	  		 	


#*************************************************************				
#Exercise 06:
x = input("insert the first variable: ")
try:
	#first, we try to see if the input is an integer:
	value_x = int(x)
except ValueError:
	#second, we try to see if it is a float:
	try:
		value_x = float(x)
	except ValueError:
		#eventually we check if it was a string:
		try:
			value_x = str(x)
		except Exception:
			#the input is totally wrong
			print("You inserted a value which is not an int, a float or a string!") 

y = input("insert the second variable: ")
try:
	#first, we try to see if the input is an integer:
	value_y = int(y)
except ValueError:
	#second, we try to see if it is a float:
	try:
		value_y = float(y)
	except ValueError:
		#eventually we check if it was a string:
		try:
			value_y = str(y)
		except Exception:
			#the input is totally wrong
			print("You inserted a value which is not an int, a float or a string!") 
try:
	print(value_x+value_y)
except TypeError:
	print('input values types do not match')
	

#*************************************************************				
#Exercise 07:
output_list = []
for x in range (11):
	output_list.append(x**3)
print(output_list)

output_list_v2 = [x**3 for x in range(11)]
print(output_list_v2)

#*************************************************************				
#Exercise 08:

a = [(i, j) for i in range (3) for j in range(4)]
print(a)

#*************************************************************				
#Exercise 09:

l = [(a, b, c) for a in range (1, 100) for b in range(1, 100) for c in range(1, 100) if (a**2 + b**2 == c**2)]
print(l)

#*************************************************************				
#Exercise 10:

import math
v = (2, 3, 5)


def normalize(v):
	s = int()
	for i in range(len(v)):
		s = s + v[i]**2
	norm = math.sqrt(s)
	o = []
	for i in range(len(v)):
		o.append(v[i]/norm)
	return o

print(normalize(v))

#*************************************************************				
#Exercise 11:


def fibonacci_numbers(n):
	fib = [0, 1]
	for i in range(2, n):
		fib.append(fib[i-1]+fib[i-2])
	return fib
	
print(fibonacci_numbers(20))



