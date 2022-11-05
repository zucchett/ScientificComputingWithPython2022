#8. List Comprehension

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

b = [ (x,y) for x in range(3) for y in range(4)]
print(b)