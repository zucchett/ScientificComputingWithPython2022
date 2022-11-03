import math
print("suggest nimbers: a=0.001, b=1000 and c=0.001")
def cal(a , b , D):
    x1 = ((b* -1) - math.sqrt(D)) /( 2 * a)
    x2 = ((b* -1) + math.sqrt(D)) /(2 * a)  
    return x1 , x2
a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

D = (b**2) - (4*a*c)
x1 , x2 = cal(a , b , D)
print("(a): ")
print(x1)
print(x2)

print("(b): ")
X1 = ((b* -1) - math.sqrt(D)) 
X2 = ((b* -1) + math.sqrt(D)) 
print(X1)
print(X2)
# as we remove the mission of /2a, so the answer got bigger
print("(c): ")
def Root(a,b,c):
    D = (b**2) - (4*a*c)
    x1 = ((b* -1) - math.sqrt(D)) /( 2 * a)
    x2 = ((b* -1) + math.sqrt(D)) /(2 * a)
    print("the root x1:  ", x1)
    print("the root x2:  ", x2)
Root(a,b,c)