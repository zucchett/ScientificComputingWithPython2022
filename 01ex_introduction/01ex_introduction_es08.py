a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

#Second Part

list_comprehension = [(i, j) for i in range(3) for j in range(4)]
print(list_comprehension)
