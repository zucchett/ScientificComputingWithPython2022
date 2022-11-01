"""
7. Cubes

Create a list of the cubes of *x* for *x* in *[0, 10]* using:

a) a for loop

b) a list comprehension
"""
cube1 = []

for i in range(11):
    cube1.append(i ** 3)

print("The cubes obtained with the for loop are: \n", cube1)
print()

cube2 = [i ** 3 for i in range(11)]

print("The cubes obtained with the list comprehension are: \n", cube2)
print()
