#8. List comprehension
l = [ (i,j) for i in range(3) for j in range(4)  ]
print(f"With comprehension: {l}")

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(f"With for loop: {a}")