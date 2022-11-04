# 2. The swap
# Write a program that swaps the values of two input variables x and y from command line (whatever the type).
# Try to do that without using a temporary variable, exploiting the Python syntax.


def Switch(x, y):
    x, y = y, x
    return print("x =", x, "y=", y)


print(Switch(9.2, 2))

# x = x ^ y
# y = y ^ x
# x = x ^ y
# 以上也可用于交换
