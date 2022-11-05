import math
x=[(a,b,int(c)) for a in range(1,101) for b in range (a,101) if (c:=math.sqrt(a**2+b**2))%1==0 and c<=100]
print(x)
