#2. The swap

# Write a program that swaps the values of two input variables x and y from command line (whatever the type).

# Try to do that without using a temporary variable, exploiting the Python syntax.

x = input("Set the value of x: ") # type Enter
print("x = ", x)

y = input("Set the value of y: ") # type Enter
print("y = ", y)

x, y = y, x

print("After the swap we have: x = ", x, " y = ", y)