#Zuccolo Giada, matr. 2055702
#EXE 6
var1 = input("var1 = ")
var2 = input("var1 = ")
try:
    print(int(var1) + int(var2))
except:
    try:
        print(float(var1) + float(var2))
    except:
        print("operation impossible")