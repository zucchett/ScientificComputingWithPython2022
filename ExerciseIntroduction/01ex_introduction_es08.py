"""
8\. **List comprehension**

Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
#%%
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
"""

a = [(i, j) for i in range(3) for j in range(4)]

print(a)
print()
