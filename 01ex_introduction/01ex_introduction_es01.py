#ex_01

# a)

numbers = [x for x in range (1, 101)]

for i, v in enumerate (numbers):
    
    if  v % 3 == 0 and v % 5 == 0:
        numbers[i] = "HelloWorld" 
        
    elif v % 3 == 0:
        numbers[i] = "Hello"
        
    elif v % 5 == 0:
        numbers[i] = "World"
        
    
print(numbers)

# b)

for i in range(len(numbers)): #We can't modify tuple,so we use do operations on list and then we make the tuple
    if numbers[i] == "Hello":
        numbers[i] = "Python"
    elif numbers[i] == "World":
        numbers[i] = "Works"
    elif numbers[i] == "HelloWorld":
        numbers [i] == "PythonWorks"
        
print(tuple(numbers))

