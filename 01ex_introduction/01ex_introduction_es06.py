
a = input("Insert first value ")
b = input("Insert second value ")

try:
    a = float(a)
    b = float(b)
    if (a+b)%1==0:
        print(int(a+b))
    else: print(a+b)
except:
    a = str(a)
    b = str(b)
    print(a+' '+b)