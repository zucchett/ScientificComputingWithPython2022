import math
A=input("pleae enter the first point as float. (( exe: <1.1>,<1.02> )) :")
B=input("pleae enter the second point as float. (( exe: <2.1>,<11.02> )) :")

Alist=[float(x) for x in A.split(",")]
print(Alist)
Atuple=tuple(Alist)
print(Atuple)
Blist=[float(m) for m in B.split(",")]
Btuple=tuple(Blist)
print(Blist)
print(Btuple)
#d= (math.sqrt(math.pow(Blist[0] - Alist[0], 2) -
                         #math.pow(Blist[1] - Alist[1], 2))) #does not work for (2,3) and (4,6)
d=str(math.sqrt(((Blist[0] - Alist[0]) ** 2) + ((Blist[1] - Alist[1]) ** 2)))
print(d)
