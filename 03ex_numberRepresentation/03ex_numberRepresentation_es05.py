import math
a = .001
b = 1000
c = .001
def do_math(a,b,c):
    x1 = (-b + math.sqrt(pow(b,2) - (4*a*c))) / (2* a)
    x2 = (-b - math.sqrt(pow(b,2) - (4*a*c))) / (2* a)
    return x1,x2

def do_math2(a,b,c):
    fix_part = math.sqrt(pow(b,2) - (4*a*c))
    x1 = (-b + fix_part )*(-b - fix_part) / (2* a)/(-b - fix_part) 
    x2 = (-b - fix_part)*(-b + fix_part) / (2* a)/(-b + fix_part) 

    return x1,x2


x1,x2 = do_math(a, b, c)
print("The solution is:\nx1 = ", x1,"\nx2 = ",x2)
x1,x2 = do_math2(a, b, c)
print("-------------------------------------------------------")
print("The re_expressed solution is:\nx1 = ", x1,"\nx2 = ",x2)
