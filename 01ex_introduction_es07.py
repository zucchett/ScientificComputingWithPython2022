my_list=[]
#a) For loop:
for x in range(10):
    my_list.append(x**3)
print(f"For loop result is: {my_list}")

#b) List comprehension:
print(f"\nList comprehension result is: {[x**3 for x in range(10)]}")

