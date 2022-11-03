# 02ex_fundamentals by Alberto Merotto 208117
#*************************************************************
#Exercise 01:
x = 5

def f(alist):
    blist = list()
    for item in alist:
    	blist.append(item)
    for i in range(x):
        blist.append(i)
    return blist

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed

#*************************************************************
#Exercise 02:
ans_a = [a**2 for a in range(10) if a%2==1]
print(ans_a)

#*************************************************************
#Exercise 03:
def filter_list(wl, n):
	out_list = filter(lambda x:len(x)<n , wl)
	return out_list

wl = ['pippo', 'pluto', 'paperino', 'a', 'test']
print(list(filter_list(wl, 5)))

#*************************************************************
#Exercise 04:

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def keys_length(dic):
	out_list = []
	return list(map(len, dic))
	
print(keys_length(lang))

#*************************************************************
#Exercise 05:

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x: x[0])
print(language_scores)

#*************************************************************
#Exercise 06:
def square(x):
	return x**2

def cube(x):
	return x**3
	
def sixth_power(x):
	return(cube(square(x)))
	
x = 2

print(square(x))
print(cube(x))
print(sixth_power(x))

#*************************************************************
#Exercise 07:
def hello(func):
	def wrapper(x):
		print('Hello World!')
		return func(x)
	return wrapper

@hello
def square(x):
    return x*x

x = 5
print(square(x))

#*************************************************************
#Exercise 08:

def recursiveFibonacci(n):
	if n <= 1:
		return n
	else:
		return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))

print([recursiveFibonacci(n) for n in range (20)])

#*************************************************************
#Exercise 09:
import timeit
s="""
def recursiveFibonacci(n = 20):
	if n <= 1:
		return n
	else:
		return(recursiveFibonacci(n-1) + recursiveFibonacci(n-2))
recursiveFibonacci()
"""		

t="""
def fibonacci_numbers(n=20):
	fib = [0, 1]
	for i in range(2, n):
		fib.append(fib[i-1]+fib[i-2])
	return fib
fibonacci_numbers()
"""

ex1 = timeit.timeit(s, number = 1)
print(ex1) #ex1 = 0.0008429870003965334

ex2 = timeit.timeit(t, number = 1)
print(ex2) #ex2 = 1.341600000159815e-05

#*************************************************************
#Exercise 10:

class PolygonError(Exception):
	pass

class polygon:
	def __init__(self, sides):
		if len(sides) < 3:
			raise PolygonError('Number of sides must be at least 3')
			
		self.sides = list()
		for side in sides:
			self.sides.append(side)
	
	def perimeter(self):
		p = 0
		for side in self.sides:
			p = p + side
		return p
		
	def getOrderedSides(self, increasing = True):
		self.sides.sort(reverse = not(increasing))
		return tuple(self.sides)
#*************************************************************
#Exercise 10:			
class rectangle(polygon):
	def __init__(self, sides):
		if len(sides) != 2:
			raise PolygonError('number of sides must be exactly 2')
		sl = []
		self.base = sides[0]
		self.height = sides[1]
		for i in range(4):
			sl.append(sides[i%2])
		polygon.__init__(self, sl)
	
	def area(self):
		return self.base * self.height
	

sides = (2, 8, 3.4)
p1 = polygon(sides)
print(p1.perimeter())
print(p1.getOrderedSides(False))		

sides_r = (3, 4.3)
r1 = rectangle(sides_r)
print(r1.perimeter())
print(r1.getOrderedSides())
print(r1.area())
