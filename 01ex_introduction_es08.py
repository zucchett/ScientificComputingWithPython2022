# EXCERSICE 8

print ("-------------Excersice 8: List Comprehension-----------------")
print ("-------------INITIAL RESULT-----------------")
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

print ("-------------LIST COMPREHENSION-----------------")

cubes1 = [(i,j) for i in range (3) for j in range(4) ]
print(cubes1)

