import math 
"""
## a)
a= float(input("enter number 'a'"))
print(a)
b = float(input("enter number 'b'"))
print(b)
c = float(input("enter number 'c'"))
print(c)
"""
a = 0.001
b = 1000
c = 0.001
d = float((b**2) - (4*a*c)) 
sol1 = (-b - math.sqrt(d))/(2*a)  
sol2 = (-b+math.sqrt(d))/(2*a)  
print('a) The solution are {0} and {1}'.format(sol1,sol2)) 

## b) The result was the sam

d = float((b**2) - (4*a*c))  
factor = (-b - math.sqrt(d))
sol1 = ((-b - math.sqrt(d)) *factor) /((2*a) * factor)  
sol2 = ((-b+math.sqrt(d))* factor)/((2*a) *factor)

print('b) The solution are {0} and {1}'.format(sol1,sol2)) 

## c)

def quadratic(d):
    
    if d > 0:
        num_roots = 2
        x1 = (((-b) + math.sqrt(d))/(2*a))     
        x2 = (((-b) - math.sqrt(d))/(2*a))
        print("c) There are 2 roots: %f and %f" % (x1, x2))
    elif d == 0:
        num_roots = 1
        x = (-b) / 2*a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")
        exit()
        
d = float((b**2) - (4*a*c)) 
quadratic(d)