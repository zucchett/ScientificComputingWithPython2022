srm, Sh1 , Sh2 , list_1 = 0 , 0 , 1 , []
while srm <= 20:
    ABC = Sh1 + Sh2
    Sh1 = Sh2
    Sh2 = ABC
    srm += 1
    list_1.append(Sh1)
print(list_1)