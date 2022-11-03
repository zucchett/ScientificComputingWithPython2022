import math
print("you can also enter a=0.001, b=1000 and c=0.001")
a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

#formula
delta = (b**2) - (4*a*c)
print(delta)
x1 = ((b* -1) - math.sqrt(delta)) /( 2 * a)
x2 = ((b* -1) + math.sqrt(delta)) /(2 * a)
print("(a)")
print(x1)
print(x2)

print("(b)")
x11 = ((b* -1) - math.sqrt(delta)) 
x22 = ((b* -1) + math.sqrt(delta)) 
print(x11)
print(x22)
# in compaire with last answer, this time as there is no /2a, so the numbers got bigger
print("c")
def findRoot(a,b,c):
    delta = (b**2) - (4*a*c)
    x1 = ((b* -1) - math.sqrt(delta)) /( 2 * a)
    x2 = ((b* -1) + math.sqrt(delta)) /(2 * a)
    print("x1 as first root: ", x1)
    print("x2 as secound root: ", x2)
findRoot(a,b,c)