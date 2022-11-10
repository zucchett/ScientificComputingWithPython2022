my__list=[]

# loop:
for x in range(0,10):
    my__list.append(x**3)
print(f"loop result: {my__list}")

# List comprehension:
print(f"\nList comprehension result: {[x**3 for x in range(10)]}")

