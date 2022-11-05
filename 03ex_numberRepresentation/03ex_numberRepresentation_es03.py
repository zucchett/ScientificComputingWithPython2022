x = 1.0
n = 0
last_x = 0
while x != float('inf'):
    last_x = x
    x = x * 2
print("The overflow limit:\n", last_x)
x = 1.0
while x != 0.0:
    last_x = x
    x = x / 2
print("The underflow limit:\n", last_x)
