a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

# My code
print("\n")
b = [(x, y) for x in [0, 1, 2] for y in [0, 1, 2, 3]]
print(b)