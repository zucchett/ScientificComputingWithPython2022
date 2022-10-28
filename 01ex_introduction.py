lst = []
for i in range(1, 101):
    if((i % 3 == 0) and (i % 5 == 0)):
        print("HelloWorld")
        lst.append("HelloWorld")
    elif(i % 3 == 0):
        print("Hello")
        lst.append("Hello")
    elif(i % 5 == 0):
        print("World")
        lst.append("World")
    else:
        print(i)
        lst.append(i)

temp_tuple = tuple(lst)

for i in range(len(lst)):
    if(lst[i] == "HelloWorld"):
        lst[i] = "PythonWorks"
    elif(lst[i] == "Hello"):
        lst[i] = "Python"
    elif(lst[i] == "World"):
        lst[i] = "Works"

result = tuple(lst)
print(result)