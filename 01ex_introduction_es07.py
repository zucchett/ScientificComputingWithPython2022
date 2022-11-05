list_1=[]
#a) For loop:
for x in range(11):
    list_1.append(x**3)
print(f"\nFor loop result is: {list_1}")

#b) List comprehension:
print(f"\nList comprehension result is: {[x**3 for x in range(11)]}\n")

