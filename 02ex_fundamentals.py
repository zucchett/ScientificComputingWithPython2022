#ex1
print("#####################EX1#####################")
def f(alist, x): 
	copy = []
	for element in alist:
		copy.append(element)
	
	for i in range(x):
		copy.append(i) 
		
	return copy

alist = [1, 2, 3]
new_list = f(alist, 5)
print(new_list)
print(alist) 

#ex2
print("#####################EX2#####################")
ans = [x**2 for x in range(10) if(x**2 % 2 == 1)] 

print("Ans with list comprehension: ", ans)

#ex3
print("#####################EX3#####################")
words = ["zlatan", "ibrahimovic", "rafa", "leao", "sandro", "tonali", "olivier", "giroud", "mike", "maignan", "matteo"]
n=5
def newfilter(words, n):
	new_words = list(filter(lambda x : len(x) < n, words)) 
	return new_words

print("words before filtering: ", words)
print("words after filtering", newfilter(words,n))
#ex4
print("#####################EX4#####################")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}

def counter(dic):
	
	length = list(map(lambda x : len(x), list(dic.keys()))) 
	return length

print(counter(lang))
#ex5
print("#####################EX5#####################")

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = (lambda x : x[0])) #sort using the first element of the tuples (the lambda function extracts it for each tuple)

print(language_scores)


#ex6
print("#####################EX6#####################")
def x_power_2(x):

	return x**2
	
def x_power_3(x):

	return x**3
	
def x_power_6(x):

	return(x_power_2(x_power_3(x))) 
	

print("2 to the power of 6 is ",x_power_6(2))

#ex7
print("#####################EX7#####################")

def hello(func):
    def wrapper(x): 
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
		return 0
	if(n==1 or n==2):
		return 1
	else:
		return fib(n-1)+ fib(n-2)

def myfib(n,seq_list):
	for i in range (n):
		seq_list.append(fib(i))
	return seq_list

my_list=[]
print(myfib(20,my_list))

#ex9
print("#####################EX9#####################")
import timeit



start_time_iterative=timeit.default_timer()
fib_list=[0,1] ##default case
while len(fib_list)<20:
	fib_list.append(fib_list[len(fib_list)-1]+fib_list[len(fib_list)-2])

duration_iterative=timeit.default_timer() - start_time_iterative

start_time_rec=timeit.default_timer()
myfib(20,[])
duration_rec=timeit.default_timer() - start_time_rec



print("the duration of the recursive algorithm is ",duration_rec, "and the duration of the iterative one is",duration_iterative )

if(duration_rec<duration_iterative):
	print("so the duration of the recursive one is shorter")
else:
	print("so the duration of the iterative one is shorter")


#ex9
print("#####################EX9#####################")

class polygon:
	sides=[]
	def __init__(self, my_sides):
		if(len(my_sides)<3):
			print("wrong data")
			return
		else:
			self.sides=list(my_sides)
	def get_sides(self):
		return self.sides
	def set_sides(self,my_sides):
		if(len(my_sides)!= len(sides)):
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
		new_list=[element for element in self.sides]
		new_list.sort(reverse=(not increasing))
		return tuple(new_list)



my_polygon= polygon([10,15,20])
print(my_polygon.get_perimeter())
print(my_polygon.get_sides())
print(my_polygon.getOrderedSides(True))
#ex10
print("#####################EX10#####################")

class rectangle(polygon):
	def __init__ (self,new_sides):
		if(len(new_sides) == 2): 
			self.sides = list(new_sides)
		else:
			print("wrong data")
	def area(self):
		return self.sides[0] * self.sides[1]
	

my_rect= rectangle([10,20])
print(my_rect.area())	
	
		
	







