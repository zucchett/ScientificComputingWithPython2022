import sys

x = input("Please enter the first number: ")
y = input("Please enter the second number: ")
try:
    print(float(x) + float(y))
except Exception as e:
    print("Sorry! You didn't enter any types of number for the input!")
