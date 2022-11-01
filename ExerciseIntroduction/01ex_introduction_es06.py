"""
6.Casting

Write a program that:
* reads from command line two variables, that can be either `int`, `float`, or `str`.
* use the `try`/`except` expressions to perform the addition of these two variables, only if possible
* and print the result without making the code crash for all the `int`/`float`/`str` input combinations.
"""

p = input("Set the first variable: ")
q = input("Set the second variable: ")

try:
    p = int(p)
except:
    try:
        p = float(p)
    except:
        p = str(p)

try:
    q = int(q)
except:
    try:
        q = float(q)
    except:
        q = str(q)

if (type(p) == int or type(p) == float) and (type(q) == int or type(q) == float):
    print("You are summing two numbers, the sum is: ", p + q)
elif type(p) == str and type(q) == str:
    print("You are summing two strings, the sum is: ", p + q)
else:
    p = str(p)
    q = str(q)
    print("You are summing one string and one number, the number will be treated as a string. The sum is: ", p + q)

print()
