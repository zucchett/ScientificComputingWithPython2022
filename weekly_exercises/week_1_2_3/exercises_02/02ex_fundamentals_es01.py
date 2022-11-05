#Zuccolo Giada, matr. 2055702
#EXE 1

def f(alist, x):
    for i in range(x):
        alist.append(i)
    return alist


alist = [1, 2, 3]
ans = f(alist, 5)
print(ans)
print(alist)  