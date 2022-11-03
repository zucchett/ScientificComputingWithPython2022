import math
#a:
a = 0.001
b = 1000
c = 0.001
d = float ((b**2) - (4*a*c))
ans_1 = (-b - math.sqrt(d)) / (2*a)
ans_2 = (-b + math.sqrt(d)) / (2*a)
print ("the answers are :", ans_1, ans_2)

#b:
d = float((b**2) - (4*a*c))
fac = (-b - math.sqrt(d))
ans_1 = ((-b - math.sqrt(d)) * fac) / ((2*a) * fac)
ans_2 = ((-b + math.sqrt(d)) * fac) / ((2*a) * fac)
print ("\nthe answers are :", ans_1, ans_2)

#c:
def ans(a,b,c):
    d = float((b**2) - (4*a*c))
    if d>0 :
        root = 2
        x1 = (((-b) + math.sqrt(d)) / (2*a))
        x2 = (((-b) + math.sqrt(d)) / (2*a))
        print ("\nthere are two roots :", x1, "and", x2)
    elif d== 0 :
        root = 1 
        x = (-b) / 2*a
        print ("\nthere is one root :", x )
    else :
        print("root = 0")

ans(0.001, 1000, 0.001)