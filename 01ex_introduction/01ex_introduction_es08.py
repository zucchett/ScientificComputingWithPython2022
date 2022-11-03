#8.List comprehension

#initial code
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

#Same code with diffrent expression(List comprehension)
a=[(i,j) for i in range(3) for j in range(4)]
print(a)
