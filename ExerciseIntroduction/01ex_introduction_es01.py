"""
a) Write a program that:
- prints the numbers from 1 to 100
- but for multiples of three print "`Hello`" instead of the number and for the multiples of five print "`World`"
- for numbers which are multiples of both three and five print "`HelloWorld`".

b) Put the result in a tuple and substitute "`Hello`" with "`Python`" and "`World`" with "`Works`".
"""

m = [x for x in range(1, 101)]

for i in range(len(m)):
    if m[i] % 5 == 0 and m[i] % 3 == 0:
        m[i] = "HelloWorld"
    elif m[i] % 5 == 0:
        m[i] = "World"
    elif m[i] % 3 == 0:
        m[i] = "Hello"

print("Results to point (a)) is: \n", m)
print()

for i in range(len(m)):
    if m[i] == "Hello":
        m[i] = "Python"
    elif m[i] == "World":
        m[i] = "Works"

tuple_mynumbers = (*m,)  # to put a list content in a tuple content

print("(b) Put the result in a tuple and substitute Hello with Python and World with Works ): \n", tuple_mynumbers)
print()
