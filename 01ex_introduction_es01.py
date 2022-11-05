#EXERCISE 1

print("----- Exercise 1: Part A ----")

for x in range (1, 101):
	if x%3 == 0 and x%5 == 0:
			print("Hello World")
	elif x%3== 0:
  			print("Hello")
	elif x%5== 0:
    		print("World")
	else:
  			print(x)

print("----- Exercise 1: Part B ----")

list_t = []
for one in range(101):
    if one%3 == 0 and one%5 == 0:
        list_t.append("Python Works");
        #print("Python Works")
    elif one%3 == 0:
        list_t.append("Python");
        #print("Python")
    elif one%5 == 0:
        list_t.append("Works");
        #print("Works")
    else:
        list_t.append(one);
        #print(one)
        
print("Tuple = ", tuple(list_t))

