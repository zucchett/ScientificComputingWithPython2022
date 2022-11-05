list_1= list()
for i in range(1,101):
    if i%5==0 and i%3==0:
        i = "HelloWorld"
        list_1.append(i)
    elif i%5==0:
        i = "World"
        list_1.append(i)
    elif i%3==0:
        i = "Hello"
        list_1.append(i)
    else:
        list_1.append(i)
print(f"\nThe answer of part a is: \n{list_1}")
for i in range(len(list_1)): #We can not change or modify tuple,so we use list instead of tuple and then finally we make a tuple with the list.
    if list_1[i] == "Hello":
        list_1[i] = "Python"
    elif list_1[i] == "World":
        list_1[i] = "Works"
    elif list_1[i] == "HelloWorld":
        list_1[i] = "PythonWorks"
print(f"\nThe answer of part b is: \n{tuple(list_1)}\n")
