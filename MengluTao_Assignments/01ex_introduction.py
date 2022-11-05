# %% [markdown]
# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `01ex_introduction.py`.
# 
# In case you need multiple files, name them `01ex_introduction_es01.py`, `01ex_introduction_es02.py` and so on. 
# 
# The exercises need to run without errors in `python3`.

# %% [markdown]
# 1\. **The HelloWorld replacement**
# 
# a) Write a program that:
# - prints the numbers from 1 to 100
# - but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
# - for numbers which are multiples of both three and five print "`HelloWorld`".
# 
# b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".

# %%
# 1
def HelloWorld():
    output_tuple = ()
    output_list = []
    ## a) 
    for i in range(1,101):
        if(i%3==0):
            output_list.append('Hello')
        elif(i%5==0):
            output_list.append('World')
        elif(i%3==0 and i%5==0):
            output_list.append('HelloWorld')
        else:
            output_list.append(i)
    print(output_list)
    ## b)
    length = len(output_list)
    for j in range(length):
        if(output_list[j] == 'Hello'):
            output_list[j] = "Python"
        elif(output_list[j] == 'World'):
            output_list[j] = "Works"
    # print(output_list)    
    output_tuple = tuple(output_list)
    return output_tuple
    
#HelloWorld()


# %% [markdown]
# 2\. **The swap**
# 
# Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).
# 
# Try to do that without using a temporary variable, exploiting the Python syntax.

# %%
def swap():
    x = int(input("Set the value of x: "))
    y = int(input("Set the value of y: "))
    list = [x,y]
    list[0],list[1] = list[1],list[0]
    x = list[0]
    y = list[1]
    return x,y

#swap()


# %% [markdown]
# 3\. **Computing the distance**
# 
# Write a function that calculates and returns the euclidean distance between two points *u* and *v* in a 2D space, where *u* and *v* are both 2-tuples *(x,y)*.
# 
# Example: if *u=(3,0)* and *v=(0,4)*, the function should return 5.
# 
# *Hint:* in order to compute the square root, import the `math` library with `import math` and use `math.sqrt()`.

# %%
import math
def euclidean_distance(u,v,*args):
    distance = 0
    u = list(u)
    v = list(v)
    distance = math.sqrt((u[0] - v[0])**2 + (u[1]-v[1])**2)
    return distance
#euclidean_distance((3,0),(0,4))

# %% [markdown]
# 4\. **Counting letters**
# 
# Write a program that calculates the number of times each character occurs in a given string. Ignore differences in capitalization.
# 
# The strings are in the cell below.

# %%
s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"


def count_letter(s):
    s = s.lower()
    dic = {}
    count = 0
    for i in s:
        if(i.isalpha()):
            if(i in dic):
                dic[i] += 1
            else:
                dic[i] = 1
    return dic

#count_letter(s1)
# count_letter(s2)


# %%

# %% [markdown]
# 5\. **Isolating the unique**
# 
# Write a program that determines and counts the unique numbers in the list:

# %%
l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]

def count_number(l):

    dic = {}
    for i in l:
        if(i in dic):
            # dic[i] += 1
            dic.pop(i)
        else:
            dic[i] = 1
    print(dic)
    return dic.__len__()

#count_number(l)


# %% [markdown]
# Do the same exploiting only the Python data structures.

# %% [markdown]
# 6\. **Casting**
# 
# Write a program that:
# * reads from command line two variables, that can be either `int`, `float`, or `str`.
# * use the `try`/`except` expressions to perform the addition of these two variables, only if possible
# * and print the result without making the code crash for all the `int`/`float`/`str` input combinations.

# %%
'''
import sys

def main(argv):
    try:
        x = int(argv[1])
        y = int(argv[2])
        print (x+y)
        return x+y
    except ValueError:
        try:
            x = float(argv[1])
            y = float(argv[2])
            print (x+y)
            return x+y
        except ValueError:
            print("Please enter a number")
            return 0

if __name__ == "__main__":
    # print(len(sys.argv))
    main(sys.argv)'''

# %% [markdown]
# 7\. **Cubes**
# 
# Create a list of the cubes of *x* for *x* in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# %%
## a) for loop
def cubes_for_loop():
    list = []
    for i in range(11):
        # print(i**3)
        list.append(i**3)
    return list

#cubes_for_loop()

## b) list comprehension
def cubes_list_comprehension():
    list = [i**3 for i in range(11)]
    return list
#cubes_list_comprehension()
    

# %% [markdown]
# 8\. **List comprehension**
# 
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

# %%
# a = []
# for i in range(3):
#     for j in range(4):
#         a.append((i, j))
# print(a)

# %%
def list_comprehension():
    list = [(i,j) for i in range(3) for j in range(4)] 

    return list

#list_comprehension()

# %% [markdown]
# 9\. **Nested list comprehension**
# 
# > A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3, 4, 5).
# 
# Find and put in a tuple all unique Pythagorean triples for the positive integers $a$, $b$ and $c$ with $c < 100$.

# %%
def pythagorean_triples():
    list =[(a,b,c) for a in range (1,100) for b in range (a,100) for c in range(b,100) if(a**2 + b**2 == c**2)]
    # print(list)
    return tuple(list)

#pythagorean_triples()

# %% [markdown]
# 10\. **Normalization of a N-dimensional vector**
# 
# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

# %%
from numpy import linalg as LA

def normalization_n_vector(v):
    norm = LA.norm(v)
    v = v/norm
    return v

#normalization_n_vector([3,4,3,6])




# %% [markdown]
# 11\. **The Fibonacci sequence**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using only `for` or `while` loops.

# %%
def fibonacci_sequence(n):
    sum = 0
    n1 = 0
    n2 = 1
    count = 0

    while(count<n):
        print("The {}th number of fibonacci sequence is {}".format(count+1,n1))
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count +=1
        
    return n1
    
#fibonacci_sequence(20)

# 0 1 1 2 3 5 8
while (True):
    print('---- Menu for exercise 1 ----')
    print('Select the exercise you want to run:')
    print('1. Exercise 1')
    print('2. Exercise 2 ')
    print('3. Exercise 3')
    print('4. Exercise 4')
    print('5. Exercise 5')
    print('6. Exercise 6')
    print('7. Exercise 7')
    print('8. Exercise 8')
    print('9. Exercise 9')
    print('10. Exercise 10')
    print('11. Exercise 11')
    print('0. Exit')
    op = input("=> ")
    if op == '1':    
        HelloWorld()
    elif op == '2':
        print(swap())
    elif op == '3':
        p1 = (3,0)
        p2 = (0,4)
        print("The euclidean distance is ",euclidean_distance(p1, p2))
    elif op == '4':
        s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
        s2 = "The quick brown fox jumps over the lazy dog"
        print("Number of times for each characters appear in the string S1 is: ",count_letter(s1))
        print("Number of times for each characters appear in the string S2 is: ",count_letter(s2))
    elif op == '5':
        l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
                85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
                1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
                45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
        print("The unique numbers in the list is as below: ")
        count_number(l)
    elif op == '6':
        print('Please check another file. Since it is a command line program, I cannot run it here.')
    elif op == '7':
        print('Select the exercise you want to run:')
        print('a. a for loop')
        print('b. a list comprehension')
        op = input("=> ")
        if op == 'a':
            print("Using cube_for_loop:",cubes_for_loop())
        elif op == 'b':
            print("Using cube_list_comprehension:",cubes_list_comprehension())
    elif op == '8':
        print("Using list comprehension the result is :",list_comprehension())
    elif op == '9':
        print("All unique Pythagorean triples for the positive integers a, b and c with c < 100 are", pythagorean_triples())
    elif op == '10':
        print("The result of normalization of given vector is :",normalization_n_vector([3,4,3,6]))
    elif op == '11':
        fibonacci_sequence(20)
    elif op == '0':
        break

    input("\nPress Enter to continue...")