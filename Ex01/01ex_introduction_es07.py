#7. Cubes
cubelist = []

#a
for x in range(0,11):
    cubelist.append(x**3)

#b
listUsingComprehension = [x**3 for x in range(0,11)]

print("Cubes using For-loop",cubelist)
print("Cubes uing List comprehension",listUsingComprehension)
