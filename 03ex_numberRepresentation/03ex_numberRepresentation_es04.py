x = 1.0
y = 0.0
n = 1

while x != y:
    y = x + 1.0/10**n
    print(n, x, y)
    n = n+1

print("After", n-2, "decimals the two numbers are considered the same number")
