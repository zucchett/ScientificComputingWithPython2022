# %% [markdown]
# You can solve these exercises in the room or at home. For this week, and the next 3 weeks, exercises have to be solved by creating a dedicated `.py` file (or files) called `02ex_fundamentals.py`.
# 
# In case you need multiple files, name them `02ex_fundamentals_es01.py`, `02ex_fundamentals_es02.py` and so on. In this case, it's convenient to create a dedicated directory, to be named `02ex_fundamentals`. 
# 
# The exercises need to run without errors with `python3`.

# %% [markdown]
# 1\. **Global variables**
# 
# Convert the function $f$ into a function that doesn't use global variables and that does not modify the original list

# %%
#x = 5
import timeit


def f(alist):
    x = 5   # local variable
    new_list = list(alist) # deep copy of list construct a new compound object
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3] # original list
ans = f(alist) 
print(ans)
print(alist) # alist is not changed

# %% [markdown]
# 2\. **List comprehension**
# 
# Write the following expression using a list comprehension:
# 
# `ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10)))`

# %%



# %% [markdown]
# 3\. **Filter list**
# 
# Using the `filter()` hof, define a function that takes a list of words and an integer `n` as arguments, and returns a list of words that are shorter than `n`.

# %%
list_of_words = ['word','hello','nice','wolf','print','hi','I','love','python']
print(list(filter(lambda x:len(x) < 3, list_of_words)))

    

# %% [markdown]
# 4\. **Map dictionary**
# 
# 
# Consider the following dictionary:
# 
# `lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}`
# 
# Write a function that takes the above dictionary and uses the `map()` higher order function to return a list that contains the length of the keys of the dictionary.

# %%

def length_of_key(x):
    return list(map(lambda x: len(x), x.keys()))
#length_of_key(lang)

# %% [markdown]
# 5\. **Lambda functions**
# 
# Write a Python program that sorts the following list of tuples using a lambda function, according to the alphabetical order of the first element of the tuple:
# 
# `language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]`
# 
# *Hint*: use the method `sort()` and its argument `key` of the `list` data structure.

# %%
language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
def sort_by_alphabetical(x):
    return x.sort(key = lambda x: x[0])

#sort_by_alphabetical(language_scores)
print(language_scores)


# %% [markdown]
# 6\. **Nested functions**
# 
# Write two functions: one that returns the square of a number, and one that returns its cube.
# 
# Then, write a third function that returns the number raised to the 6th power, using only the two previous functions.

# %%
def square(x):
    return x * x

def cube(x):
    return x * x * x

def sixth_power(x):
    return cube(square(x))





# %% [markdown]
# 7\. **Decorators**
# 
# Write a decorator named `hello` that makes every wrapped function print “Hello World!” each time the function is called.
# 
# The wrapped function should look like:
# 
# ```python
# @hello
# def square(x):
#     return x*x
# ```

# %%
def hello(func):
    def wrapper(x):
        print("Hello World!")
        return func(x)
    return wrapper

@hello # decorator
def square(x):
    return x*x

square(2)


# %% [markdown]
# 8\. **The Fibonacci sequence (part 2)**
# 
# Calculate the first 20 numbers of the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) using a recursive function.

# %%
def recursive_func(x):
    if x <= 1:
        return x
    else:
        return recursive_func(x-1) + recursive_func(x-2)
       



# %% [markdown]
# 9\. **The Fibonacci sequence (part 3)**
# 
# Run both the Fibonacci recursive function from the previous exercise, and the Fibonacci function from 01ex that use only `for` and `while` loops.
# 
# Measure the execution code of the two functions with `timeit` ([link to the doc](https://docs.python.org/3/library/timeit.html)), for example:
# 
# `%timeit loopFibonacci(20)`
# 
# `%timeit recursiveFibonacci(20)`
# 
# which one is the most efficient implementation? By how much?

# %%
def fibonacci_sequence_for_loop(n):
    sum = 0
    n1 = 0
    n2 = 1
    count = 0

    while(count<n):
        print(n1)
        sum = n1 + n2
        n1 = n2
        n2 = sum
        count +=1
        
    return n1
    





# %% [markdown]
# **Anwser:**
# From the result above we can see that using for-while loop is more effiecient, the time consumes a lot less than using recursive one. The recurisve one takes 2.93ms, however the non-recursive one takes only 75.4µs .

# %% [markdown]
# 10\. **Class definition**
# 
# Define a class `polygon`. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
# 
# - Create appropriate methods to get and set the length of each side
# 
# - Create a method `perimeter()` that returns the perimeter of the polygon
# 
# - Create a method `getOrderedSides(increasing = True)` that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method
# 
# Test the class by creating an instance and calling the `perimeter()` and `getOrderedSides(increasing = True)` methods.

# %%
class polygon:
    side_length = () #define the tuple contains the length of each side, at least 3 items

    def  __init__(self, lengths):
        if len(lengths) < 3:
            raise ValueError("Polygon must have at least 3 sides")
        else:
            self.side_length = lengths
    
    def __del__(self):
        print("This is the destructor")
    
    def perimeter(self):
        sum = 0
        for i in self.side_length:
            sum += i
        return sum

    def getOrderedSides(self,incresing = True):
        if incresing:
            return sorted(self.side_length)
        else:
            return sorted(self.side_length,reverse=True)
        
    

a = polygon((9,6,3,4,5))
#b = polygon((1,3))
print(a.perimeter())
print(a.getOrderedSides())
    

# %% [markdown]
# 11\. **Class inheritance**
# 
# Define a class `rectangle` that inherits from `polygon`. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.
# 
# - Create a method `area()` that returns the area of the rectangle.
# 
# Test the `rectangle` class by creating an instance and passing an appropriate input to the constructor.

# %%
class rectangle(polygon):
    
    side_length = ()

    def __init__(self,lengths):
       
        if len(lengths) != 4:
            raise ValueError("Rectangle must have 4 sides")
        elif lengths[0] != lengths[1] and lengths[0] != lengths[2] and lengths[0] != lengths[3]:
            raise ValueError("Rectangle must have 2 equal sides")
        else:
             self.side_length = lengths
            
    def area(self):
        ordered_list = sorted(self.side_length)
        return max(ordered_list[0] * ordered_list[1], ordered_list[0] * ordered_list[2])

#rec = rectangle((2,4,4,2))
#print(rec.area())

        
while (True):
    print('---- Menu for exercise 2 ----')
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
        alist = [1, 2, 3] # original list
        ans = f(alist) 
        print("changed list: ",ans)
        print("alist is not changed",alist) # alist is not changed
        
    elif op == '2':
        
        ans = [x*x for x in range(10) if x % 2 == 1 ]
        print("List comprehension version of the expression",ans)
    elif op == '3':
        list_of_words = ['word','hello','nice','wolf','print','hi','I','love','python']
        print("The word that satisfied the condition in the list is")
        print(list(filter(lambda x:len(x) < 3, list_of_words)))
        
    elif op == '4':
       lang = {"Python" : 3, "Java" : '', "Cplusplus" : 'test', "Php" : 0.7}
       print("List that contains the length of the keys of the dictionary: ",length_of_key(lang))
       
    elif op == '5':
       language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
       sort_by_alphabetical(language_scores)
       print("After sorted using alphabetical order:", language_scores)
    elif op == '6':
        print("The six power of 2 is:",sixth_power(2))
        print("The six power of 9 is:",sixth_power(9))
    elif op == '7':
        print("Using warpped function: ", square(2))
       
    elif op == '8':
        print("The first 20 numbers of fibonacci are:") 
        for i in range(20):
            print(recursive_func(i))
    elif op == '9':
        start = timeit.default_timer()
        fibonacci_sequence_for_loop(20)        
        stop = timeit.default_timer()
        print('Time used in for loop: ', stop - start)
        start = timeit.default_timer()
        recursive_func(20)
        stop = timeit.default_timer()
        print('Time used in recursive: ', stop - start)

    elif op == '10':
        a = polygon((9,6,3,4,5))
        #b = polygon((1,3))
        print("perimeter is",a.perimeter())
        print("Sides ordered by length: ", a.getOrderedSides())
    elif op == '11':
        rec = rectangle((2,4,4,2))
        print("The area of the rectangle is: ", rec.area())
    elif op == '0':
        break


    input("\nPress Enter to continue...")

    
        



