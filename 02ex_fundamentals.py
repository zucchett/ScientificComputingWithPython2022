#ex1
print("#####################EX1#####################")
def f(alist, x): 
	copy = [] #empy list
	for element in alist:
		copy.append(element) #copy the elements in the new list
	
	for i in range(x):
		copy.append(i) #append the new elements
		
	return copy

alist = [1, 2, 3]
new_list = f(alist, 5)
print(new_list)
print(alist) 

#ex2
print("#####################EX2#####################")
ans = [x**2 for x in range(10) if(x**2 % 2 == 1)] 

print(ans)

#ex3
print("#####################EX3#####################")
words = ["zlatan", "ibrahimovic", "rafa", "leao", "sandro", "tonali", "olivier", "giroud", "mike", "maignan", "matteo"] #list of words
n=5
def newfilter(words, n):
	new_words = list(filter(lambda x : len(x) < n, words)) #lambda function to filter words 
	return new_words

print("words before filtering: ", words)
print("words after filtering", newfilter(words,n))
#ex4
print("#####################EX4#####################")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7} 

def counter(dic):
	
	length = list(map(lambda x : len(x), list(dic.keys()))) #lambda function
	return length

print(counter(lang))
#ex5
print("#####################EX5#####################")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = (lambda x : x[0])) #sorting using the first element 

print(language_scores)


#ex6
print("#####################EX6#####################")
def x_power_2(x): #definition of the first function

	return x**2
	
def x_power_3(x): #definition of the second function

	return x**3
	
def x_power_6(x): #defintion of the third function that calls the two previous ones in its execution

	return(x_power_2(x_power_3(x))) 
	

print("2 to the power of 6 is ",x_power_6(2))

#ex7
print("#####################EX7#####################")

def hello(func):
    def wrapper(x): #wrapper
        print("Hello World!")
        return func(x)    
    return wrapper
    
@hello 
def square(x):
    return x*x
    
print("the square of 5 is ",square(5))

#ex8
print("#####################EX8#####################")

def fib(n):
	if(n<0):
		return
	if(n==0):
		return 0		#base cases
	if(n==1 or n==2):
		return 1
	else:
		return fib(n-1)+ fib(n-2) 	#recursive calls

def myfib(n,seq_list):
	for i in range (n):
		seq_list.append(fib(i))		#appending to the list the first n elements of the fibonacci sequence
	return seq_list

my_list=[]
print(myfib(20,my_list))

#ex9
print("#####################EX9#####################")
import timeit	#importing timeit library



start_time_iterative=timeit.default_timer() #calculating the starting time of the execution of the iterative funcion
fib_list=[0,1] ##default case
while len(fib_list)<20:
	fib_list.append(fib_list[len(fib_list)-1]+fib_list[len(fib_list)-2])	#calling the iterative funcion

duration_iterative=timeit.default_timer() - start_time_iterative	#calculating the operation time of the execution of the iterative funcion 

start_time_rec=timeit.default_timer()	#calculating the starting time of the execution of the recursive funcion
myfib(20,[])	#calling the recursive funcion
duration_rec=timeit.default_timer() - start_time_rec	#calculating the operation time of the execution of the recursive funcion 



print("the duration of the recursive algorithm is ",duration_rec, "and the duration of the iterative one is",duration_iterative )

if(duration_rec<duration_iterative):
	print("so the duration of the recursive one is shorter")
else:
	print("so the duration of the iterative one is shorter")


#ex9
print("#####################EX9#####################")

class polygon:
	sides=[]
	def __init__(self, my_sides):	#constructor
		if(len(my_sides)<3):
			print("wrong data")
			return
		else:
			self.sides=list(my_sides)
	def get_sides(self):
		return self.sides
	def set_sides(self,my_sides):
		if(len(my_sides)!= len(sides)):		#methods of the class
			print("wrong data")
			return
		else:
			self.sides= list(my_sides)	
	def get_perimeter(self):
		perimeter=0
		for element in self.sides:
			perimeter=perimeter+element
		return perimeter
	
	def getOrderedSides(self, increasing):
		new_list=[element for element in self.sides]	#creating a new list containing the sides of the polygon
		new_list.sort(reverse=(not increasing))		#sorting the list using the sort function
		return tuple(new_list)



my_polygon= polygon([10,15,20])
print(my_polygon.get_perimeter())
print(my_polygon.get_sides())
print(my_polygon.getOrderedSides(True))
#ex10
print("#####################EX10#####################")

class rectangle(polygon):
	def __init__ (self,new_sides):	#class constructor
		if(len(new_sides) == 2): 
			self.sides = list(new_sides)
		else:
			print("wrong data")
	def area(self):
		return self.sides[0] * self.sides[1]
	

my_rect= rectangle([10,20])
print(my_rect.area())	
	
		
	







