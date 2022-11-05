''' Created by Pedram on 10/26/2022 AD. '''

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

number = int(input("Please input a number: "))
finalPower= cube(square(number))
print("{}\u2076= ".format(number) + str(finalPower))