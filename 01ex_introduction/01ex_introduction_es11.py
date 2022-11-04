fibonacci = []
for i in range(20):
    if (len(fibonacci) < 2):
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)