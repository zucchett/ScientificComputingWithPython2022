import itertools


a = []
for i, j in itertools.product(range(3), range(4)):
    a.append((i, j))

print(a)