#Zuccolo Giada, matr. 2055702
#EXE 1
numbers = ()
for num in range(1, 101):
    if num % 3 != 0 and num % 5 != 0:
        value = num
    if num % 3 == 0 and num % 5 == 0:
        value = "HelloWorld"
    else:
        if num % 3 == 0:
            value = "Hello"
        if num % 5 == 0:
            value = "World"

    numbers += (value, )
result = list(numbers)
#print(numbers)
i=0;
while i < len(result):
    if type(result[i]) == 'int':
        pass
    else:
        if result[i] == "Hello":
            result[i]="Python"
        if result[i] == "World":
            result[i]="Works"
    i+=1
numbers = tuple(result)
print(numbers)