import math 
#a)
print("\nStep A")
a = 0.001
b = 1000
c = 0.001
d = float((b**2) - (4*a*c)) 
sol1 = (-b - math.sqrt(d))/(2*a)  
sol2 = (-b+math.sqrt(d))/(2*a)  
print(f'The solution are {sol1} and {sol2}') 
#b)
print("\nSTEP B")

d = float((b**2) - (4*a*c))  
factor1 = (-b + math.sqrt(d))
factor2 = (-b - math.sqrt(d))
sol1 = ((-b - math.sqrt(d)) *factor1) /((2*a) * factor1)  
sol2 = ((-b+math.sqrt(d))* factor2)/((2*a) *factor2)

print(f'The solution are {sol1} and {sol2}') 
print('Because we multiplying both the numerator and the denominator,\nboth multiplyed parts will destroyed in dividing part and we have same answer in parts a & b.')

#c)

def ans(a,b,c):
    d = float((b**2) - (4*a*c)) 
    print("\nSTEP C")
    if d > 0:
        roots = 2
        x1 = (((-b) + math.sqrt(d))/(2*a))     
        x2 = (((-b) - math.sqrt(d))/(2*a))
        print(f'There are 2 roots: {x1} and {x2}\n')
    elif d == 0:
        roots = 1
        x = (-b) / 2*a
        print(f"There is one root: {x}\n")
    else:
        roots = 0



ans(0.001,1000,0.001)