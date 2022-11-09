Print("************EXERCISE 1**********")
#FUnction that doesn't use global variables
def f(alist):
    x = 5
    arr=alist
    for i in range(x):
         arr.append(i)
    return arr

alist = [1,2,3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed!


print("**********EXERCISE 2**************")
#List comprehension for the expression
print([x*x for x in range(10) if x%2 == 1])

print("**********EXERCISE 3**************")

words = ["apple", "pineapple", "avocado", "peach", "guava", "strawberry", "orange", "carrot"]
n=6
def wordfilter(words, n):
	filtered_words = list(filter(lambda x : len(x) < n, words)) 
	return filtered_words

print("list of words: ", words)
print("filtered words", wordfilter(words,n))

print("**********EXERCISE 4**************")

lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7} 

def counter(dic):

	length = list(map(lambda x : len(x), list(dic.keys()))) 
	return length

print(counter(lang))

print("**********EXERCISE 5**************")


language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = (lambda x : x[0])) #sort 

print(language_scores)


print("**********EXERCISE 6**************")

def square(x): #first function

	return x**2

def cube(x): #2nd function

	return x**3

def power_6(x): #defintion of the third function that calls the two previous ones in its execution

	return(square(cube(x))) 



print("**********EXERCISE 7**************")



def my_decorator(f): 
    def log_f_as_called():
        print(f'{f} was called.')
        f()
    return log_f_as_called

@my_decorator
def hello():
    print('Hello World!')
    
hello()



print("**********EXERCISE 8**************")
#FIbonacci dequence using recursive function

def recur_Fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
print(recur_Fibonacci(20))

print("**********EXERCISE 9**************")

def loopFibonacci(num):
  #store the first two fixed terms in a list
    fib = [0, 1]
    for i in range(2, num+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib
print("fibonacci using loops: ", "\n", loopFibonacci(20))

print("fibonacci using recursion: ", "\n")



def recursiveFibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
print(recursiveFibonacci(20))
print("**********EXERCISE 10**************")

class polygon:
    #class attribute
	side_length=[]
    
    #instance atttributes
	def __init__(self, my_sides):	
		if(len(my_sides)<3):
			print("error")
			return
		else:
			self.side_length=list(my_sides)
	def get_sides(self):
		return self.side_length
	def set_sides(self,my_sides):
		if(len(my_sides)!= len(side_length)):		#methods
			print("error")
			return
		else:
			self.side_length= list(my_sides)
			self.side_length= list(my_sides)	
	def get_perimeter(self):
		perimeter=0
		for element in self.side_length:
			perimeter=perimeter+element
		return perimeter

	def getOrderedSides(self, increasing):
		new_list=[element for element in self.side_length]
		new_list.sort(reverse=(not increasing))
		new_list=[element for element in self.side_length]
		new_list.sort(reverse=(not increasing))		
		return tuple(new_list)


my_polygon= polygon([20, 35, 40])
print(my_polygon.get_perimeter())
print(my_polygon.get_sides())
print(my_polygon.getOrderedSides(True))
#ex10


