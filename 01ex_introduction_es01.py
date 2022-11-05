list_1= list()
for j in range(1,101):
    if j%5==0 and j%3==0:
        j = "HelloWorld"
        list_1.append(j)
    elif j%5==0:
        j = "World"
        list_1.append(j)
    elif j%3==0:
        j = "Hello"
        list_1.append(j)
    else:
        list_1.append(j)
print(f"The answer of part a is: \n{list_1}")
for j in range(len(list_1)): 
        if list_1[j] == "Hello":
        list_1[j] = "Python"
    elif list_1[j] == "World":
        list_1[j] = "Works"
    elif list_1[j] == "HelloWorld":
        list_1[j] == "PythonWorks"
print(f"\nThe answer of part b is: \n{tuple(list_1)}")
