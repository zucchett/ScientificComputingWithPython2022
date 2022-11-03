n = 1
x= 2.0
while x > 1.0:
    x = 1.0 + (0.1)**n
    print(x)
    n = n + 1
print('machine precision is: ', (.1)**n)
