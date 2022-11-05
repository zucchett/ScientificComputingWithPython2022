# a for loop
total = [] 

for num in range(11):
    total.append(num**3)

print(total)

#)b a list comprehension

total_cubes = [number**3 for number in range(11)]

print(total_cubes)