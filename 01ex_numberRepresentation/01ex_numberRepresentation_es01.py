''' Created by Pedram on 10/19/2022 AD. '''

# Local Variable
numberList = []

# Use Separate Functions for Dependency Injection 
# The Function that Checks the Multiples of Three
def multiplesOfThree(number):
    if number % 3 == 0 and number % 5 != 0:
        return True
    else: 
        return False

# The Function that Checks the Multiples of Five
def multiplesOfFive(number):
    if number % 5 == 0 and number % 3 != 0:
        return True
    else: 
        return False

# The Function that Checks the Multiples of Three and Five
def multiplesOfThreeAndFive(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else: 
        return False

# The Function that Checks the Multiples
def checkNumber(number, numberList):
    if multiplesOfThree(number):
        numberList.append("Hello")
    elif multiplesOfFive(number):
        numberList.append("World")
    elif multiplesOfThreeAndFive(number):
        numberList.append("HelloWorld")
    else:
        numberList.append(str(number))

# The Function that Convert List to Tuple
def convert(list):
    return tuple(list)

# Input Numbers 1 ... 100
for number in range(1, 101):
    checkNumber(number, numberList)
print("A) ", numberList)
l_replace = [arg.replace('Hello', 'Python') for arg in numberList]
l_replace = [arg.replace('World', 'Works') for arg in l_replace]
print("B) ", convert(l_replace))