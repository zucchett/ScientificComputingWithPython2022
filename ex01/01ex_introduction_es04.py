s = input("Insert the string: ")
number = {}
for i in s :
    if i.isalpha() == True :
        i = i.upper()
        number[i] = number.get(i,0) + 1
print(number)