from warnings import catch_warnings


def square(number):
    return number**2

def cube(number):
    return number**3

def power_of_six(number):
    return square(cube(x))

try:
    x = int(input("Insert a number: "))
    print(power_of_six(x))
except:
    print("Insert an int value!")