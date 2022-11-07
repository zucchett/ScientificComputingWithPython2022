# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `01ex_introduction.py`.
# 
# In case you need multiple files, name them `01ex_introduction_es01.py`, `01ex_introduction_es02.py` and so on. 
# 
# The exercises need to run without errors in `python3`.



import math

#Ex 1 ===============================================================================================================
print("Ex 1 **The HelloWorld replacement**")
# 
# a) Write a program that:
# - prints the numbers from 1 to 100
# - but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
# - for numbers which are multiples of both three and five print "`HelloWorld`".
# 
# b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

# In[2]:


a = "Hello"
b = "World"
c = ()

for index, element in enumerate(range(1,101)):

    if  element % 3 == 0 and element % 5 == 0:
        c += (a+b,)
        print(c[-1])
    elif element % 3 == 0:
        c += (a,)
        print(c[-1])
    elif element % 5 == 0:
        c += (b,)
        print(c[-1])
    else:
        c += (element,)
        print(c[-1])




e =[]
for index, item in enumerate(c):
    if type(item) == str:
        e.append(str(item).replace("Hello", "Python").replace("World", "Works"))
    else:
        e.append(item)
e


#Ex 2 ============================================================================================================
print("Ex2 **The swap**")
# 
# Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.


x = input("Please, type a value: ")
y = input("Please, type another value: ")

x,y = y,x

print(x,y)


#Ex 3 ===========================================================================================================
print("Ex 3 **Computing the distance**")
# 
# Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.
# 
# Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.



def euclidean_distance(u: tuple, v: tuple)-> int | float:
    '''calculates and returns the euclidean distance between two points.'''
    return math.sqrt((u[0]-v[0])**2 + (u[1] - v[1])**2)

print(euclidean_distance((5,8), (7,8)))


#Ex 4 ==========================================================================================================
print("Ex 4 **Counting letters**")
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The strings are in the cell below.



s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"




def charoccurencies(string: str, spaceoccur = True) -> dict:
    '''calculates the occurencies of each character in a given string not taking into account the case of the character.
    the optional argument spaceoccur controls the count of the spaces'''
    charlist = {}
    
    for character in string.lower():                           #putting all in lower case to avoid case sensibility
        charlist[character] = string.lower().count(character)
        
    if not spaceoccur:
        charlist.pop(" ")
        
    
    return charlist

print(charoccurencies(s1))
print()


#Ex 5 =========================================================================================
print("Ex. 5 **Isolating the unique**")
# 
# Write a program that determines and counts the unique numbers in the list:



l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]



counts = {}
for num in l:
    if num in counts.keys():
        counts[num] +=1
    else:
        counts[num] = 1

uniquescount = len(counts.keys())
print(uniquescount)


# Do the same exploiting only the Python data structures.



uniques = set(l)
print(uniques)
print(len(uniques))
print()


#Ex 6 ============================================================================================================
print("Ex 6**Casting**")
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.



t1, t2= input("Please enter a numeric value: "), input("Please enter another numeric value: ")

if (t1+t2).isnumeric():                                                          
    t1, t2 = int(t1), int(t2)

elif t1.count(".") == 1 or t2.count(".")==1 and (t1+t2).replace(".","").isnumeric():
    t1,t2 = float(t1), float(t2)
    
try:
    print(f"{t1} + {t2} = {t1+t2}")
    
except:
    print(f"Can't add {t1} to {t2}.")
    


# Ex 7 ===========================================================================================
print("Ex 7 **Cubes**")
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension



#with for loop
cubes = []
for n in range(0,11):
    cubes.append(n**3)
cubes




#with list comprehension
cubos = [q**3 for q in range(1,11)]
cubos


#Ex 8 ================================================================================================================
print("8 **List comprehension**")
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)



a = [(i,j) for i in range(3) for j in range(4)]
print(a)


#Ex 9 =============================================================================================================================================
print("Ex 9 **Nested list comprehension**")
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.


triples = tuple(set([(f,g,h) for f in range(100) for g in range(100) for h  in range(99) if h**2 == f**2 + g**2]))
print(triples)



#Ex 10 ===================================================================================================================================================================================================
print("10 **Normalization of a N-dimensional vector**")
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).



def vecnorma(vector: tuple) -> tuple:
    '''Takes an N-dimensional vector and normalizes it.'''

    addic = 0
    for dim in vector:                                     #calculating the norm
        addic += dim**2
    norm = math.sqrt(addic)

    newvector = [(1/norm)*dim for dim in vector]           # using the norm to have a normalized vector
        
    return tuple(newvector)

vector= (1,2,3)
print(vecnorma((1,2,3)))



#Ex 11 ===================================================================================================================================================================
print("Ex 11 **The Fibonacci sequence**")
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.



#using while loop
u = 0
v = 1
fibo = [0,1]
z = 3
while z <= 20:
    u, v = v, u+v
    fibo.append(v)
    z +=1

print(fibo)




#using for loop
u = 0
v =1
fibo = []
for z in range(20):
    if z == 0:
        
        fibo.append(0)
        
    else:
        u, v = v, u+v
        fibo.append(u)
    

print(fibo)




#using a function
def loopFibonacci(index, a = 0, b = 1 ):
    '''accepts an index and returns a list with the fibonacci sequence until that index'''
    lista = []
    for n in range(0, index+1): 
        lista.append(a)
        a, b= b,a+b
        
        
        
    return lista

print(loopFibonacci(19))
