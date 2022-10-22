print("#####################EX1#####################")
#ex1

def f(alist, x): #added a new argument to the function 
	copy = [x for x in alist] #make a copy of the original list
	
	for i in range(x):
		copy.append(i) 
		
	return copy

alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist) # alist has not been changed

print("#####################EX2#####################")
#ex2

ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))

print("Ans with original code: " + str(ans))

ans = [x**2 for x in range(10) if(x**2 % 2 == 1)] #create a list with the square of the number in [0,10) only if the square%2 = 1

print("Ans with list comprehension: " + str(ans))

print("#####################EX3#####################")
#ex3

words = ["hi", "dog", "cat", "lists", "comprehension", "python", "code", "keyboard", "mouse", "random", "love"]
n=7

print("Not filtered words: " + str(words))
	
def myfilter(words, n):
	filtered_words = list(filter(lambda x : len(x) < n, words)) 
	return filtered_words
	
print("Filtered words (shorter than " + str(n) +"): " + str(myfilter(words,n)))

print("#####################EX4#####################")
#ex4

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def counter(lang):
	
	length = list(map(lambda x : len(x), list(lang.keys()))) #map each element of the list of keys to the length of the key 
	return length
	
print(counter(lang))

print("#####################EX5#####################")
#ex5

def sorting(x): #return the first element of the tuple 
	return x[0]

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = sorting) #sort using the first element of the tuples

print(language_scores)

print("#####################EX6#####################")
#ex6

def square(x):

	return x**2
	
def cube(x):

	return x**3
	
def xPower6(x):

	return(square(cube(x))) #xPower6 return the square of the cube of the input argument 
	
x = 2

print(xPower6(x))

print("#####################EX7#####################")
#ex7

def hello(func):
    def wrapper(x): #wrapper function takes in input the same argument of the original function 
        print("Hello World!")
        return func(x)    
    return wrapper
    
@hello 
def square(x):
    return x*x
    
print(square(5))

print("#####################EX8 and EX9#####################")
#ex8 and ex9

import timeit


def fibonacci(n, sequence):

	if n < 0:
		return
		
	if(n == 0):
	
   		sequence.append(0) #F0 = 0
   		return	
	
	if(n == 1):
	
		fibonacci(n-1,sequence) #i need to add also F0
		sequence.append(1)
		return	
	
	if(n == 2):
		
		fibonacci(n-1,sequence) #i need to add also F0 and F1
		sequence.append(1)
		return	
	
	fibonacci(n-1,sequence) #compute the previous number in the sequence
	l = len(sequence) 
	sequence.append((sequence[l-1] + sequence[l-2])) #append the new value 
	return
	
	
emptylist = []

start_time = timeit.default_timer() #saving the initial time 

fibonacci(20, emptylist) #executing the code


print("Execution time for the recursive version of fibonacci:", timeit.default_timer() - start_time) #compute the difference between final time and initial time

print("First 20 number in the Fiboncci sequence = " + str(emptylist))

#same as before
start_time = timeit.default_timer() 

fib = [0, 1] #base case

l = 2 

while l <= 20: #until there aren't 22 elements in the list (i counted also the base case with F0 = 0)
	
	fib.append(fib[l-1] + fib[l-2]) #fib_i = fib_(i-1) + fib_(i-2)
	l = len(fib) #update the list lenght

print("Execution time for the iterative version of fibonacci:", timeit.default_timer() - start_time)
	
print("First 20 number in the Fiboncci sequence = " + str(fib))

print("#####################EX10#####################")
#ex10

class polygon:

	sides = []

	def __init__(self, newSides):
		
		if(len(newSides) >=3):
			self.sides = list(newSides)
		else:
			print("A polygon must have at least 3 sides!")
	


	def getSides(self):
	
		return self.sides


	def setAllSides(self, newSides):
		
		i = 0
		for side in newSides:
		
			self.sides[i] = side
			i = i + 1 
	
			
	def setSingleSide(self, newSide, position):
		
		self.sides[position] = newSide
	
		
	def perimeter(self):

		perimeter = 0
		
		for side in self.sides:
			perimeter = perimeter +side
		return perimeter 
			
			
	def getOrderedSides(self, increasing):
	
		copy = [side for side in self.sides]
		copy.sort(reverse = (not increasing))
		return tuple(copy)
		
				
pol = polygon([10,15,20])

		
print("The sides list of the polygon is: "  + str(pol.getSides()))
print("\n\n")
newSides = [9,14,21]
print("I want set the sides to "+ str(newSides))
print("\n")
pol.setAllSides(newSides)
print("   After execution of the method setAllSides: " +str(pol.getSides()))
print("\n\n")
print("I want set the new component to [16,11,18] using the setSingleSide method")
print("\n")
pol.setSingleSide(16,0)
print("   After execution of the method setSIngleSide for the first component: " +str(pol.getSides()))
print("\n")
pol.setSingleSide(11,1)
print("   After execution of the method setSIngleSide for the second component: " +str(pol.getSides()))
print("\n")
pol.setSingleSide(18,2)
print("   After execution of the method setSIngleSide for the last component: " +str(pol.getSides()))
print("\n\n")
print("The perimeter of the polygon is: " + str(pol.perimeter()))
print("\n\n")
print("The list of sides in increasing order is: "+str(pol.getOrderedSides(increasing = True)))
print("The list of sides in decreasing order is: "+str(pol.getOrderedSides(increasing = False)))



