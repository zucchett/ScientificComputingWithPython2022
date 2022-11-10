"""
2. The swap

Write a program that swaps the values of two input variables *x* and *y* from command line (whatever the type).

Try to do that without using a temporary variable, exploiting the Python syntax.
"""
x = input("Set the value of x: ")  # remember to click Enter after inputting the string
y = input("Set the value of y: ")  # remember to click Enter after inputting the string

x, y = y, x

print("x =", x, ", y =", y)
print()
