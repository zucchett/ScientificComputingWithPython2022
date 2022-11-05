"""
Author: Luca Bonaventura Luca Bonaventura matr. 2090005
"""


"""
___________________________EXECRCIZE 1________________________________________

                     1. The HelloWorld replacement

a) Write a program that:

    prints the numbers from 1 to 100
    but for multiples of three print "Hello" instead of the number and for the multiples of five print "World"
    for numbers which are multiples of both three and five print "HelloWorld".

"""
print("___________ESERCIZIO 1___________")

for i in range(1, 100):
	if(i%3 == 0 and i%5 == 0): #multiples of 3 and 5
		print("Hello Word")
	elif(i%3 == 0):            #multiples of 3
		print("Hello")
	elif(i%5 == 0):            #multiples of 3
		print("Word")
	else:                      #others
		print(i)

"""
b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".

"""
# tuple is ammutable, so I use a temporalry list and then put in a tuple
t = list()
for i in range(1, 100):
	if(i%3 == 0 and i%5 == 0): #multiples of 3 and 5
		t.insert(i, "Python Works")
	elif(i%3 == 0):            #multiples of 3
		t.insert(i, "Python")
	elif(i%5 == 0):            #multiples of 5
		t.insert(i, "Works")
	else:                      #others
		t.insert(i, i)
# put in a tuple
t = tuple(t)

# TESTBENCH
#print (t)


"""
___________________________EXECRCIZE 2________________________________________
                           2. The swap

Write a program that swaps the values of two input variables x and y from command line (whatever the type).

Try to do that without using a temporary variable, exploiting the Python syntax.
"""
print("___________ESERCIZIO 2___________")

print ("Type the x value")
x = str(input())
print ("Type the y value")
y = str(input())

"""
#Classic way
temp = x
x = y
y = temp
"""
#Other way
x, y = y, x #swap of the values

# TESTBENCH
#print(x, y)



"""
___________________________EXECRCIZE 3________________________________________
                           
	              3. Computing the distance

Write a function that calculates and returns the euclidean distance between two points u and v in a 2D space, where u and v are both 2-tuples (x,y).

Example: if u=(3,0) and v=(0,4), the function should return 5.

Hint: in order to compute the square root, import the math library with import math and use math.sqrt().
"""
print("___________ESERCIZIO 3___________")

# import the math module 
import math

# Define u and v with the execize values
u = (3,0)
v = (0,4)

# From the definition of euclidean distance we have:
x = (u[0] - v[0], u[1] - v[1])
out = math.sqrt(x[0]**2 + x[1]**2)

print(out)



"""
___________________________EXECRCIZE 4________________________________________
                       4. Counting letters

Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.

The strings are in the cell below.

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


"""
print("___________ESERCIZIO 4___________")

# Define s1 and s2 with the execize values
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

# Lower case all the string
s1 = s1.lower()

# Create empty dictionary
d1 = {}

for i in range(len(s1)):

	# Contained in dictionary
	if( (s1[i] in d1) == True):
		# Update element
		d1[s1[i]] = (d1[s1[i]]+1)
		
	# Not contained in dictionary
	else:
		# Add new element
		d1[s1[i]] = 1

# Order by alphabetic order
d1 = dict(sorted(d1.items()))

# Print the dictionary
print(d1)

"""
___________________________EXECRCIZE 5________________________________________

                      5. Isolating the unique

Write a program that determines and counts the unique numbers in the list:

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

Do the same exploiting only the Python data structures.

"""
print("___________ESERCIZIO 5___________")
# Excercize list
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

# Sort list
l = sorted(l)
# Create ampty list
l_uni = []

i = 0
while (i < len(l)-1):
	if (l[i+1] != l[i]):
		l_uni.append(l[i]) # Element not equal to the following one, so add it to the unique
	count = 1
	# skip all the consecutive elemts equal
	while (i+count < len(l)-1 and l[i+count]==l[i]): 
		count = count + 1
	i = i + count
# Computation for the last element 
if (l[i] != l[i-1]) :
    l_uni.append(l[i])

# Print the dictionary with the unique values
print(l_uni)
# Count them
print(len(l_uni))

"""
Do the same exploiting only the Python data structures.
"""
# Create empty dictionary
d = {}

# Create a dictionary with <key>:<occurances>
for i in range(len(l)):

	# Contained in dictionary
	if( (l[i] in d) == True):
		# Update element
		d[l[i]] = (d[l[i]]+1)
		
	# Not contained in dictionary
	else:
		# Add new element
		d[l[i]] = 1

# Delete item from checked from l with occurance higher than 1
for i in range(len(l)):
	if d.get(l[i], -1) > 1:
		d.pop(l[i])

# Order to better explain the out
d = dict(sorted(d.items()))
# Print the dictionary with the unique values, print only the keys without reporting the repetitions that are 1
print(list(d.keys()))
# Count them
print(len(d))



"""
___________________________EXECRCIZE 6________________________________________
                            6. Casting

Write a program that:

    reads from command line two variables, that can be either int, float, or str.
    use the try/except expressions to perform the addition of these two variables, only if possible
    and print the result without making the code crash for all the int/float/str input combinations.
"""
print("___________ESERCIZIO 6___________")

try: # try to make the sum
	print ("Type the x value")
	x = float(input())
	print ("Type the y value")
	y = float(input())
	#Verify if the output of the sum is int or float making the difference from the float sum with the casted sum
	if((x+y)-int(x+y)==0):
		print(int(x+y))
	else:
		print(x+y)
except:
	print("Wrong type inserted") # in other case print error message

"""
___________________________EXECRCIZE 7________________________________________
                            7. Cubes

Create a list of the cubes of x for x in [0, 10] using:

a) a for loop

b) a list comprehension
"""
print("___________ESERCIZIO 7___________")

# for loop
l = []
for i in range(11):
	l.append(i**2) # add the cubes to the list
print(l)

# list comprehension
l.clear()
l = [i**2 for i in range(11)]
print(l)


"""
___________________________EXECRCIZE 8________________________________________
                        8. List comprehension

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)
"""
print("___________ESERCIZIO 8___________")

# given code
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

# sing list comprehension
a = [(i, j) for i in range(3) for j in range(4)]
print(a)
# They are equal
"""
___________________________EXECRCIZE 9________________________________________
                   9. Nested list comprehension

    A Pythagorean triple is an integer solution to the Pythagorean theorem 

    . The first Pythagorean triple is (3, 4, 5).

Find and put in a tuple all unique Pythagorean triples for the positive integers
, and with .
"""
print("___________ESERCIZIO 9___________")

# return true only if a_ and b_ are prime together
def isPrime(a_, b_):
	#if MCD is greater than 1 the two numbers are not cross prime
	if math.gcd(a_, b_) > 1: return False
	else: return True


# Clear a to reuse it
a.clear()
#    (a, b, c=a^2+b*2) all the Pythagorean triple, use all the a and for the b start after a to find all unique triplet
a = [(a, b, int(math.sqrt(a**2+b**2))) for a in range(1, 100+1) for b in range(1, a+1) if  math.sqrt(a**2+b**2) < 100 and int(math.sqrt(a**2+b**2)) == math.sqrt(a**2+b**2) and isPrime(a, b)]
print(a)


"""
___________________________EXECRCIZE 10________________________________________
             10. Normalization of a N-dimensional vector

Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

"""
print("___________ESERCIZIO 10___________")
#input vector
x = [1, 10, 2, 3, 0]

#squared sum
ssum = 0
# compute the sum of the squares
for i in range(len(x)-1):
	ssum = ssum + x[i]**2
# divide every elemnt for it
for i in range(len(x)-1):
	x[i] = x[i]/ssum
print(x)

"""
___________________________EXECRCIZE 11________________________________________
                       11. The Fibonacci sequence

Calculate the first 20 numbers of the Fibonacci sequence using only for or while loops.

"""
print("___________ESERCIZIO 11___________")

a1 = 0
a2 = 1
fib = [0, 1] # add the first two elements
for i in range(18):
	b = a1 + a2
	a1 = a2
	a2 = b
	fib.append(b) # put the computed fib value on the list
print(fib)
