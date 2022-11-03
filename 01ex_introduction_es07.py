mylist=[]
#a) For loop:
for x in range(0,10):
    mylist.append(x**3)
print(f"For loop result is: {mylist}")

#b) List comprehension:
print(f"\nList comprehension result is: {[x**3 for x in range(0,10)]}")

