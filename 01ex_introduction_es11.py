a = 0
b = 1
k = 0
c = 0

while k <= 20:
    c = a + b
    print(k, ": ", c , " ")
    a = b
    b = c
    k = k+1
