import math 
#a)
print("\nStep A")
a = 0.001
b = 1000
c = 0.001
d = float((b**2) - (4*a*c)) 
su1 = (-b - math.sqrt(d))/(2*a)  
su2 = (-b+math.sqrt(d))/(2*a)  
print(f'The solution can be {su1} and {su2}') 
#b)
print("\nSTEP B")

d = float((b**2) - (4*a*c))  
fc = (-b - math.sqrt(d))
su1 = ((-b - math.sqrt(d)) *fc) /((2*a) * fc)  
su2 = ((-b+math.sqrt(d))* fc)/((2*a) *fc)

print(f'The solution can be {su1} and {su2}') 
print('Because we are multiplying both the numerator and the denominator,\n both multiplied components are lost in the division part and we have the same answer in parts a and b.')



#c)

def ans(a,b,c):
    d = float((b**2) - (4*a*c)) 
    print("\nSTEP C")
    if d > 0:
        roots = 2
        x1 = (((-b) + math.sqrt(d))/(2*a))     
        x2 = (((-b) - math.sqrt(d))/(2*a))
        print(f'The one root is : {x1} and the other root is :{x2}\n')
    elif d == 0:
        roots = 1
        x = (-b) / 2*a
        print(f"this show one root: {x}\n")
    else:
        roots = 0



ans(0.001,1000,0.001)

