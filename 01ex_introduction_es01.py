# a
a = []

print("section a: ")
for i in range(1 , 101):
    if i % 3 == 0 and i % 5 == 0:
        print('HelloWorld')
        a.append('PythonWorks')
    elif i % 3 == 0:
        print('Hello')
        a.append('Python')

    elif i % 5 == 0:
        print('World')
        a.append('Works')

    else:
        print(i)
        a.append(i)

#b
print('\n section b: ')


s = tuple(a)
print(s)