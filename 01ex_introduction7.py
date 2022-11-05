# Cubes
# Create a list of the cubes of x for x in [0, 10] using:
# a) a for loop
# b) a list comprehension

#Loop

print('List with loop')
cubes = list()


for i in range(10):
  cubes.append(i**3)
print(cubes)


#List Comprehension
print('='*42)
print('List Comprehension')

cubes_comprehension = [ i**3 for i in range(10)] 
print(cubes_comprehension)

print('='*42)

#1 line List Comprehension print
[print([i**3 for i in range(10)])]
