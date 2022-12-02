#ex_08

#Write, using the list comprehension, 
#a single-line expression that gets the same result as the code in the cell below.

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

#answer

ans = [(x,y) for x in [0,1,2] for y in [0,1,2,3]]
print (ans)
