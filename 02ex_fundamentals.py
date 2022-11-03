#Matteo Cogato
#2026966

#es1
print("\n###################### ES1 ##########################")

x = 5

def f(alist):
	list2 = []
	for y in alist:
		list2.append(y)
	for i in range(x):
		list2.append(i)
	return list2

alist = [1, 2, 3]
print("Initial list:", alist)

ans = f(alist)
print("Returned list by the function: ", ans)
print("Initial list:", alist,"has not been modified") # alist has not been changed

#es2
print("\n###################### ES2 ##########################")



ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print("Objective:",ans)

list_c = [a*a for a in range(10) if a%2 == 1]
print("Using list comprehension:", list_c)


#es3
print("\n###################### ES3 ##########################")



def f(word,n):
	ans = list(filter(lambda x : len(x)<int(n),word))
	return(ans)
	
word = ["CIAO","NO","SI","FORSE"]
print("Words:", word)

n = 3
ans = f(word,n)
print("Words shorter than %d" %(n),"are",ans)

#es4
print("\n###################### ES4 ##########################")


def f(dct):
	ans = list(map(lambda x : len(x),dct.keys()))
	return(ans)
	
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
print("Dictionary:",lang)
	
print("Dictionary keys length:", f(lang))


#es5
print("\n###################### ES5 ##########################")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key=lambda x : x[0])

print("Ordered list:",language_scores)

#es6 
print("\n###################### ES6 ##########################")

def cube(x):
	return x*x*x
	
def square(x):
	return x*x
	
def power6(x):
	y = square(cube(x))
	return y

x=2
print("Initial value:",x)
print("Elevated to the 6th power:",power6(x))


#es7
print("\n###################### ES7 ##########################")

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper


@hello
def square(x):
    return x*x
  
x=3
print("Square:", square(x))

#es8
print("\n###################### ES8 ##########################")

def fib(length, l):
	if (len(l) == length):
		return l
	elif len(l) == 0:
		l.append(0)
		return fib(length,l)
	elif len(l) == 1:
		l.append(1)
		return fib(length,l)
	else:
		y = l[-1] + l[-2]
		l.append(y)
		return fib(length,l)
	        

empty = []
print("First 20 fibonacci numbers:",fib(20,empty))



#es9
print("\n###################### ES9 ##########################")

import timeit
 
#recursive Fibonacci
mysetup = """
def fib(length, l):
	if (len(l) == length):
		return l
	elif len(l) == 0:
		l.append(0)
		return fib(length,l)
	elif len(l) == 1:
		l.append(1)
		return fib(length,l)
	else:
		y = l[-1] + l[-2]
		l.append(y)
		return fib(length,l)
"""
 
# code snippet whose execution time is to be measured
mycode = '''
l = []
fib(20,l)
'''
#execute the function 10000 times for a better approximation
print ("Recursive Fibonacci:", timeit.timeit(setup = mysetup, stmt = mycode, number = 10000))	


# while Fibonacci 
mysetup = """
def loopFibonacci(dimension):
	x1 = 0
	x2 = 1
	fibonacci = [x1,x2]
	while len(fibonacci)<dimension:
		x2,x1 = x1+x2,x2
		fibonacci.append(x2)
	return fibonacci

"""
 
# code snippet whose execution time is to be measured
mycode = '''
loopFibonacci(20)
'''
 
print ("While Fibonacci:    ", timeit.timeit(setup = mysetup, stmt = mycode, number = 10000))
#the loopFibonacci function is more efficient, it requires less than half of the the of the recursiveFibonacci function

#es10
print("\n###################### ES10 ##########################")

class polygon:

	edges = []                   
	
	def __init__(self, components):
		if(len(components)>=3):
			self.edges = list(components)
			print("New polygon created: ", self.edges)
		else:
			print("ERROR: too short list")
			
	def get(self, n): # n is the component index
        	return self.edges[n]
        
	def getAll(self): 
        	return self.edges
      
	def set(self, n, xi): # n is the component index, and xi is the value
        	if n < len(self.edges):
           		self.edges[n] = xi
           		print("New length of side %d is set " %n )

	def perimeter(self):
		tot = 0
		for x in self.edges:
			tot = tot + x
		return tot

	def getOrderedSides(self, increasing = True):
		copy = [x for x in self.edges]
		copy.sort(reverse= not increasing)
		return tuple(copy)

sides = (5,0,6)	
a = polygon(sides)
print("The perimeter is:", a.perimeter())
print("Current sides: ", a.getAll())
print("Sides in increasing order:", a.getOrderedSides(True))



#es11
print("\n###################### ES11 ##########################")

class rectangle(polygon):


	def __init__(self,components):
		if len(components) == 2:
			components = list(components)
			self.edges = components
			print("New rectangle created: ", self.edges)		
		else:
			print("Error: number of components required is 2")
			
	def area(self):
		return self.edges[0]*self.edges[1]
		
	def perimeter(self):
		return (self.edges[0]+self.edges[1])*2
			
	

side = [5,6]
b = rectangle(side)
print("The area of the rectangle is:", b.area())
print("The perimeter of the rectangle is:", b.perimeter())
b.set(0,2)
print("Current sides: ", b.getAll())
print("Sides in decreasing order:", b.getOrderedSides(False))















			

