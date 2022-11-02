# List comprehension

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

print([(i,j) for i in range(3) for j in range(4)])
