print("#####################EX1#####################")
#ex1

def f(alist, x):
	copy = [x for x in alist]
	
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

ans = [x**2 for x in range(10) if(x**2 % 2 == 1)]

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
	
	length = list(map(lambda x : len(x), list(lang.keys())))
	return length
	
print(counter(lang))

print("#####################EX5#####################")
#ex5

def sorting(x):
	return x[0]

language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]

language_scores.sort(key = sorting)

print(language_scores)

print("#####################EX6#####################")
#ex6

def square(x):

	return x**2
	
def cube(x):

	return x**3
	
def xPower6(x):

	return(square(cube(x)))
	
x = 2

print(xPower6(x))

print("#####################EX7#####################")
#ex7

def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)    
    return wrapper
    
@hello 
def square(x):
    return x*x
    
print(square(5))

print("#####################EX7#####################")
#ex7

def fibonacci(n, sequence):

	if n < 0:
		return
	if(n == 0):
   		sequence.append(0)
   		return	
	
	if(n == 1):
   		sequence.append(1)
   		return	
	
	if(n == 2):
   		sequence.append(1)
   		return	
	
	fibonacci(n-1,sequence)
	l = len(sequence)
	sequence.append((sequence[l-1] + sequence[l-2]))
	return
	
	
emptylist = []
fibonacci(20, emptylist)
print(emptylist)
