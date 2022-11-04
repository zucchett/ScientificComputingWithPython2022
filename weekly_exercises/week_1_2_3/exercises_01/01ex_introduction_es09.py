#Zuccolo Giada, matr. 2055702
#EXE 9
cub = ()
for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            if ((a**2 + b**2) == (c**2)):
                value = (a, b, c)
                cub += (value, )
cub = list(cub)
for i in cub:
    original = i  #i[0],i[1],i[2]
    find = (i[1], i[0], i[2])
    for n in cub:
        if find == n:
            cub.remove(find)
cub = tuple(cub)
print(cub)