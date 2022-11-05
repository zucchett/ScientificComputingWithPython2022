# first two terms
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < 20:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1