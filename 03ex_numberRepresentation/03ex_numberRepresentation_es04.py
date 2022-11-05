# ex_04: machine precision

x = float(1.0)
x1 = float(0)
i = 0
while x != x1:
    x1 = x
    x = x + 2**(-i)
    i = i + 1

print (2**(-i))
