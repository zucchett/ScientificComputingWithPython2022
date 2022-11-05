#list with for loop
list_1 = []
for x in range(0,11):
    y = x **3
    list_1.append(y)
    x += 1

print (list_1)

#list with list comprehension

print([ x ** 3 for x in range (0,11)])

