#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# 
# Python is an **interpreted** high-level, general-purpose programming language.
# 
# Its design philosophy emphasizes code readability with the use of **significant indentation**.
# 
# Python is **dynamically-typed** (the type of a variable is checked at runtime) and **garbage-collected** (to avoid manual memory management).
# 
# It supports multiple programming paradigms, including structured, object-oriented and functional programming.
# 
# It is often described as a "batteries included" language due to its comprehensive standard library.
# 
# Reference website: [https://www.python.org/](https://www.python.org/). Check it for documentation!
# 
# Online documentation on [jupyter](http://nbviewer.jupyter.org/urls/bitbucket.org/ipre/calico/raw/master/notebooks/Documentation/Reference%20Guide/Reference%20Guide.ipynb) is also available. Remember, Jupyter allows to edit and run Python code interactively, but Jupyter **is not** python!

# In[ ]:


print("This is python, programming is fun again")


# ## Variables and base types

# In[ ]:


# This is a comment

variable = "2" # this is also a comment
print(variable, "is a", type(variable))

variable = 2 # "2" and 2 are not the same thing
print(variable, "is a", type(variable))

variable = 2. # also 2 differs from 2.
print(variable, "is a", type(variable))

variable = True
print(variable, "is a", type(variable))


# The function `print` allows also more powerful way of printing numbers:

# In[ ]:


print("Art: %5d, Price per unit: %8.2f" % (453, 59.058))


# In[ ]:


a, b = 5, "1" # a compact notation to assign values to more than one variable
print(a, b)


# ## Basic operations
# 
# Operations between variables are intuitive:

# In[ ]:


a, b = 2, 5
c = a + b
print(c)


# However, the result may vary depending on the type of the variable:

# In[ ]:


a, b = "2", "5"
c = a + b
print(c)


# Pay special attention when the type of the two variables is not the same:

# In[ ]:


a, b = 4, 7.2
c = a + b
print(c)
print(type(a), type(b), type(c))


# In[ ]:


a, b = 2, "5"
c = a + b


# In these cases, **casting** the variables to the correct type is necessary:

# In[ ]:


c = a + int(b)
print(c)


# same applies to `float()`, `str()` and so on. Sometimes it's automatic:

# In[ ]:


a, b = 3, True
c = a + b
print(c)


# But it's not always possible!

# In[ ]:


a = "Python3"
int(a)


# In[ ]:


x = y = z = 7 # multiple assignment
print(x, y, z)


# It's also possible to pass a value from command line (rarely used and discouraged):

# In[ ]:


x = input("Set the value of x: ") # remember to type Enter
print("x =", x)


# The boolean operations are even more explicit than other languages:

# In[ ]:


a, b = True, False

aandb = a and b
print("and:", aandb)

aorb = a or b
print("or:", aorb)

nota = not a
print("not:", nota)


# ## Math operators
# 
# Python includes by default the most common math operators.
# 
# Note: square root requires to import the `math` module. More on this later on.
# 
# For those used to C/C++: you can use the `**` operator for power.
# 
# Pay attention to the type of the variables, as they may yield unexpected results. One of the most common cases, the ambiguity in the division between two `int`, is no longer an issue in Python3:

# In[ ]:


x = 1
print(type(x))
y = 1.0
print(type(y))
a, b = int(3), int(4)
print(a / b)
print(float(a) / float(b))


# In[ ]:


print(3 / 4) # division between ints
print(3.0 / 4.0) # division between floats
print(3 % 4) # modulus
print(3 // 4) # floor division
print(3**4) # exponentiation
print(pow(3, 4)) # power function


# ## Pointers in Python? 
# 
# 
# Pointers are widely used in C and C++. Essentially, they are variables that hold the memory address of another variable.  Are there pointers in python? Essentially no.
# Pointers go against the [Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3):
# 
# *Pointers encourage implicit changes rather than explicit. Often, they are complex instead of simple, especially for beginners. Even worse, they beg for ways to shoot yourself in the foot, or do something really dangerous like read from a section of memory you were not supposed to. Python tends to try to abstract away implementation details like memory addresses from its users. Python often focuses on usability instead of speed. As a result, pointers in Python doesn’t really make sense.*
# 
# 
# It's all about two basics python concepts:
# 1. Mutable vs Immutable objects
# 2. Variables and Names
# 
# Mutable objects can be changed, immutable cannot. I.e. when a new value is assigned to a given immutable "variable", a new object is in reality created. This as "variable" in python are actually just names bound to objects (PyObject).
# 
# For more details about all this refer e.g. to [this review](https://realpython.com/pointers-in-python/).

# ## Lists
# Lists are exactly as the name implies. They are lists of objects. The objects can be any data type (including lists), and it is allowed to mix data types. In this way they are much more flexible than arrays. It is possible to append, delete, insert and count elements and to sort, reverse, etc. the list.

# In[ ]:


a_list = [1, 2, 3, "this is a string", 5.3]
b_list = ["A", "B", "F", "G", "d", "x", "c", a_list, 3]
print(b_list)


# Accessing and setting elements in lists is intuitive with the [] operator.
# 
# Python allows very efficient selection of ranges:

# In[ ]:


a = [7, 5, 3, 4, 10]
print("[0] ->", a[0]) # access 0-th element of the list
print("[-1] ->", a[-1]) # start counting from the end

# a[start:stop:step]

print("[2:4] ->", a[2:4]) # range (in this case, 3rd and 4th element)
print("[:3] ->", a[:3]) # range, up to (4th element excluded)
print("[3:] ->", a[3:]) # range, starting from (4th element included)
print("[-3:] ->", a[-3:]) # range, starting from (3th element included)
print("[3:len(a)] ->", a[3:len(a)]) # range, until the end of the list
print("[1::3] ->", a[1::3]) # range in steps (of 3)


# There are also several *methods* of the list objects that can be used to perform several operations:

# In[ ]:


a = [7, 5, 3, 4, 10]
print(a)
a.insert(0, 1000) # position, value
print(a)
a.append(99) # value to append at the end of the list
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.pop() # remove last element
print(a)
a.remove(10) # remove by value
print(a)
a.remove(a[2]) # same as before
print(a)


# Very compact notations are possibile. For example, the [list comprehensions](https://docs.python.org/2/tutorial/datastructures.html?highlight=comprehensions) allow to create in a single line non-trivial lists:

# In[ ]:


even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)


# Strings feature all operations permitted on lists, including comprehensions:

# In[ ]:


first_sentence = "It was a dark and stormy night."
characters = [x for x in first_sentence]
print(characters)


# The opposite is also possible, but in a different way:

# In[ ]:


second_sentence = ''.join(characters)
print(second_sentence)


# ### Strings and String Handling
# 
# One of the most important features of Python is its powerful and easy handling of strings. Defining strings is simple enough in most languages. But in Python, it is easy to search and replace, convert cases, concatenate, or access elements. We’ll discuss a few of these here. For a complete list, see this [tutorial]( http://www.tutorialspoint.com/python/python_strings.htm).

# In[ ]:


a = "A string of characters, with newline \n CAPITALS, etc."
print(a)
b = 5.0
newstring = a + "\n We can format strings for printing %.2f"
print(newstring % b)


# Operations are easy (remember strings are lists!)

# In[ ]:


a = "ABC DEFG"
print(a[1:3])
print(a[0:5])


# In[ ]:


a = "ABC defg"
print(a.lower())
print(a.upper())
print(a.find('d'))
print(a.replace('de', 'a'))
print(a)
b = a.replace('def', 'aaa')
print(b)
b = b.replace('a', 'c')
print(b)
b.count('c')


# In[ ]:


# of course, strings can be summed:
b = "XYZ"
c = a + b
print(c)


# ## Tuples
# 
# Tuples are like lists with one very important difference. Tuples not only are immutable, but they *cannot be changed*.

# In[ ]:


a = (1, 2, "3", 4)
print(a)
a[1] = 2


# ## Dictionaries
# 
# Dictionaries are unordered, **keyed** lists.
# 
# They are of paramount importance and a major asset of Python.

# In[ ]:


a = {'key1' : "anItem", 2 : ["a,bc"], 3.4 : "C", 'fourthkey' : 7} # dictionary example
print(a['key1'])
print(a[3.4])


# In[ ]:


for i in a: print(i, a[i])


# In[ ]:


print("Keys:", a.keys())
print("Values:", a.values())


# The keys can be of several types, but they must be a **hashable** type:
# 
#  - hashable types are: `int`, `float`, `str`, `tuple`
#  - unhashable data types: `dict`, `list`, and `set` 

# In[ ]:


a = {[2, 3] : "value"} # does not work: a list is not an hashable type


# ## Sets

# Sets are used to store multiple items in a single variable, but differently from lists and dictionaries, they are *unordered* and **do not support duplicates**.

# In[ ]:


a = {"apple", 2, "cherry", 2}
print(a)


# In[ ]:


print(a[1])


# In[ ]:


a.add("3")
print(a)
a.update({7, "banana"})
print(a)


# ## Conditional Statements
# 
# Conditionals perform different computations or actions depending on whether a programmer-defined boolean condition evaluates to `True` or `False`.
# 
# In addition to the usual `if` and `else`, Python also provides the `elif` statement which is equivalent to *else if*.
# 
# Note that in Python blocks of code are separated only through the **indentation**.

# In[ ]:


a = 21
if a >= 22: 
    print("if")
elif a >= 21:
    print("elif")
else:
    print("else")


# ## Exceptions
# 
# `try`/`except`: a very important and powerful type of conditional expression that is often used to avoid runtime errors. Use it, and use it with care. 

# In[2]:


a = "1"
try:
    b = a + 2
    print(b)
except:
    print(a, " is not a number")


# ## Loops and Iterators
# 
# Both the `for` and `while` loops are present in Python. The `for` loop, for instance, requires an iterable object to loop on:

# In[ ]:


for i in [1, 3, 5]:
    print(i)


# The behaviour of iterators (an object that enables to run through a container) in Python is very similar to all other languages. Start exploring the `range` function:

# In[ ]:


print(type(range(10)))
print(list(range(10)))

for i in range(2, 10, 2):
    print(i) # note the indented block of code and the lack of {}


# Similary to other programming languages, the `while` loop requires just a boolean statement:

# In[ ]:


i = 1
while i < 10:
    print(i)
    i += 1


# For lists, there is a convenient way to get both the index and the value at the same time with the `enumerate` function:

# In[ ]:


for i in enumerate([4, 5, 2, 7]): print(i) # returns pairs of values (a tuple)


# In[ ]:


for i, j in enumerate([4, 5, 2, 7]): print(i, j) # unpack the tuple on-the-fly


# For dictionaries, the `iteritems` method allows to get both the key and the values of each item of the dict:

# In[ ]:


d = {'a' : "first", 2 : "second"}
# although not exactly an iterator, items() allows to run on the content of a dict
for key, value in d.items():
    print(key, value, d[key])


# In[ ]:




