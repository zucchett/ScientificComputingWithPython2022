import math

"""
Exercice 1 : THE HELLOWORLD REPLACEMENT
"""
print("Exercice 1 : THE HELLOWORLD REPLACEMENT \n")
"""
Creating the list "HelloWorld" and from this list, changing words and putting it into a tuple
"""

#Fonction to create the list "HelloWorld"
def listHelloWorld(x) :
    #declaring a list
    list = []
    for i in range(1,x+1,1):
        #multiples of three AND five
        if (i%3==0 and i%5==0):
            list.append("HelloWorld")
        #multiples of three
        elif i%3==0:
            list.append("Hello")
        #multiples of five
        elif i%5==0:
            list.append("World")
        #if not, just add the number i to the list   
        else:  
            list.append(i)
    return (list)
print("The HelloWorld list : ")
list_hello = listHelloWorld(100)
print(list_hello)
print("\n")

#Declaration of a tuple
my_tuple = ()
#To modify an item to tuple = convert tuple to list
l = list(my_tuple)

#for every item in the list, we substitute depending on the word
for i in range(1,len(list_hello),1):
    if (list_hello[i] == "Hello"):
        list_hello[i] = "Test"
    elif (list_hello[i] == "World"):
        list_hello[i] = "Works"
    else:
        list_hello[i] = i+1

#converting the list_hello to a tuple
my_tuple = tuple(list_hello)
print("The HelloWorld subsitute : ")
print(my_tuple)

"""
Exercice 2 : THE SWAMP
"""
print("\nExercice 2 : THE SWAMP \n") 

def swapping(a,b):
    print("Value of x :", a, "and y : ", b)
    #Python syntac to swaps value
    a, b = b, a
    print("Swapping...")
    print("Value of x :", a, "and y : ", b)
 
x=input("Enter x:\n")
y=input("Enter y:\n")
swapping(x,y)

"""
Exercice 3 : COMPUTING THE DISTANCE
"""
print("\nExercice 3 : COMPUTING THE DISTANCE \n") 

def computing_distance(u,v):
    #using math.sqrt() for the square root
    return math.sqrt( ((u[0]-v[0])**2) + ((u[1]-v[1])**2) )
    
u = (3,0)
v = (0,4)
print("if u=(3,0) and v=(0,4), the distance is : ", computing_distance(u,v), "\n")

"""
Exercice 4 : COUNTING LETTERS
"""
print("\nExercice 4 : COUNTING LETTERS \n") 

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

def counting_letters(s):
    #We create a dictionary with letters as keys and occurences as values
    letters = {}
    #Ignore differences in capitalization : put everything lower
    s = s.lower()
    #For each letter
    for i in s:
        #If it is in the dictionnary, we increment the value 
        if i in letters:
            letters[i]+=1
        else:
        #else, we add it to the dictionnary with a value of 1
            letters[i] = 1
    print("Counting letters....")                
    print(letters)

counting_letters(s1)
counting_letters(s2)

"""
Exercice 5 : ISOLATING THE UNIQUE
"""
print("\nExercice 5 : ISOLATING THE UNIQUE \n") 


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def isolating_unique(l):
    #We create a dictionary
    numbers = {}
    #a list to put every unique numbers
    list_count = []
    
    #For each number in the list
    for i in l:
        #If the number is already in the dictionnary, we increment the value
        if i in numbers:
            numbers[i]+=1
        else:
        #else, we add it to the dictionnary with a value of 1
            numbers[i] = 1
    
    #For each numbers in the dictionnary (each keys)        
    for j in numbers:
        #We add it to the unique list
        list_count.append(j)
    print("List of unique numbers : ")
    print(sorted(list_count))
    print("How many unique numbers?",len(list_count),"\n")
        

isolating_unique(l)

print("Same fonction but with Python data structures \n") 
def isolating_unique_python(l):
    #Same fonction but with the Python data structures
    unique = set(l)
    print("List of unique numbers : ")
    print(unique)
    print("How many unique numbers?",len(unique))
    
isolating_unique_python(l)

"""
Exercice 6 : CASTING
"""
print("\nExercice 6 : CASTING \n") 
def casting(x,y):
    try:
        sum = x + y
        print(sum)
    except:
        print('sum is not possible')
        
casting(3,'2')
casting(10,23)
casting('hello', 'world')
casting(3.2,4.6)


"""
Exercice 7 : CUBES
"""
print("\nExercice 7 : CUBES \n") 
def cubes_for():
    #List of the cubes
    list_cubes = []
    #For each numbers from 0 to 10
    for i in range(0,11,1):
        #cube the number and add it to the list
        list_cubes.append(i**3)
    return list_cubes
cubesFor = cubes_for()
print('List of the cubes with a for loop : ',cubesFor)

def cubes_list_comprehension():
    #list of the cubes
    list = range(0,11,1)
    #list comprehension
    return [i**3 for i in list]
cubesListComprehension = cubes_list_comprehension()
print('List of the cubes with a for loop : ',cubesListComprehension)


"""
Exercice 8 : LIST COMPREHENSION
"""
print("\nExercice 8 : LIST COMPREHENSION \n") 
print([(i,j) for i in range(3) for j in range(4)])

"""
Exercice 9 : NESTED LIST COMPREHENSION
"""
print("\nExercice 9 : NESTED LIST COMPREHENSION \n") 

def Pythagorean_triple():
    my_tuple = ()
    #a**2 + b**2 = c**2
    #a = m**2 - n**2
    #b = 2*m*n
    #c = m**2 + n**2
    
    c, m = 0, 2
    #while c is under 100
    while c < 100 :
        for n in range(1, m):
            a = m*m-n*n
            b = 2*m*n
            c = m*m + n*n
        c+=1
        if c > 100:
            break
        my_tuple = my_tuple + (a, b,c, ';')
        m+=1
    return my_tuple

def Pythagorean_triple_nested_list():
    #with nested_list
    my_tuple = [(a,b,c) for c in range(100) for b in range(c) for a in range(b) if c**2 == a**2 + b**2]
    return my_tuple
my_tuple = Pythagorean_triple_nested_list()     
print('Pythagorean triple : \n',my_tuple)

import random 
import math

"""
Exercice 10 : NORMALIZATION OF A N-DIMENSIONAL VECTOR
"""
print("\nExercice 10 : NORMALIZATION OF A N-DIMENSIONAL VECTOR") 
def normalization(n):
    #N random numbers in a tuple
    raw = tuple(random.random() for i in range(n))
    #Normalization
    norm = math.sqrt(sum(i**2 for i in raw))
    #we devide the tuple by the norm
    raw_norm = tuple([i/norm for i in raw])
    print(norm)
    print(raw_norm)
    #we make sure that the sum equals to 1
    sum_norm = sum(i**2 for i in raw_norm)
    print(sum_norm)

norm = normalization(5)

"""
Exercice 11 : THE FIBONACCI SEQUENCE
"""
print("\nExercice 11 : THE FIBONACCI SEQUENCE") 

def fibonacci():
    #Fn = F(n-1) + F(n-2)
    #seed values : f0 = 0, f1 = 1
    f = [0,1]
    
    #We have the first two values => we start at the third value
    for i in range(2, 20):
        #we add to the list the result :
        f.append(f[i-1] + f[i-2])
    return(f)

fib = fibonacci()
print(fib)