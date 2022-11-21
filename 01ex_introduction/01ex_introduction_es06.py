x = input("x =")          
y = input("y =")

try:
    x = float(x)
except ValueError:
    x = x
try:
    y = float(y)
except ValueError:
    y = y
try:
    c = x + y
    print(c)
except TypeError:
    print('not the same type')