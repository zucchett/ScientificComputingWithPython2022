# (a) FOR LOOP
cubes = []
start = int(input("enter a value: "))
end = int(input("enter the end value: "))
for num in range(start, end):
    cubes.append(num**3)
print(str(cubes))

# (B) LIST COMPREHENSION
start = int(input("enter a value: "))
end = int(input("enter the end value: "))

cubes_list = [num**3 for num in range(start, end)]
print(str(cubes_list))



