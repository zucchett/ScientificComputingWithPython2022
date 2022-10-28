# Es01

numbers = []

for i in range(1,101) :
    if i % 3 == 0 and i % 5 == 0:
        print("HelloWorld")
        numbers.append("HelloWorld")
    elif i % 3 == 0 :
        print("Hello")
        numbers.append("Python")
    elif i % 5 == 0 :
        print("World")
        numbers.append("Works")
    else :
        print(i)
        numbers.append(i)

tuple_output = tuple(numbers)
print(tuple_output)