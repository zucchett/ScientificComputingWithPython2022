#Zuccolo Giada, matr. 2055702
#EXE 2

# ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
ans = [x * x for x in range(10) if x % 2 == 1]
print(ans)