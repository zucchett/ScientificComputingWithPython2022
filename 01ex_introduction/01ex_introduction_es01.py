# a)
list_a = []
for i in range(1, 101):
    if i % 15 == 0: 
        i = "HelloWorld"  
    elif i % 5 == 0: 
        i = "World"
    elif i % 3 == 0:
            i = "Hello"
    list_a.append(i)     
    
print(list_a, '\n')


# b)
list_b = tuple(list_a)

for j in range(1, 100):
    if list_a[j] == "Hello":
        list_a[j] = "Python"
    elif list_a[j] == "World":
        list_a[j] = "Works"
    elif list_a[j] == "HelloWorld":
        list_a[j] = "PythonWorks"        

list_b_tuple = tuple(list_a) 
print(list_b_tuple)