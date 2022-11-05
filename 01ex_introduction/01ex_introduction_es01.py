#a)
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        number = "HelloWorld"
    elif (number % 3 == 0):
        number = "Hello"
    elif (number % 5 == 0):
        number = "World"
    print(number)

#b)
total,final_total = tuple(), tuple()

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        number = "HelloWorld"
    elif (number % 3 == 0):
        number = "Hello"
    elif (number % 5 == 0):
        number = "World"
    total += (number,) 

for number in total:
    if number == "Hello":
        number = "Python"
    elif number == "World":
        number = "Works"
    final_total += (number,)

print(final_total)