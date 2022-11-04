import re
i = input("Please enter your number: ")
number =  re.match("0b([1,0]*)", i)
number2 = re.match("0x([0-9 a-f]*)", i)
number3 = re.match("[0-9]+", i)
if number:
    x = number.groups(0)
    print(int(x[0], 2))
if number2:
    x = number2.groups(0)
    print(int(x[0],16))
if number3:
    print(number3.group(0))
else:
    print('You have not enter any types of numbers')
