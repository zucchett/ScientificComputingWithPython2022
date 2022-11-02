#11. The Fibonacci sequence

fibonacci = []

for i in range(0,20):
    if(i == 0):
        fibonacci.append(0)
    elif(i == 1):
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])

print(fibonacci)
