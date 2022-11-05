square = (lambda x: x**2)
cube = (lambda x: x**3)
power_6 = (lambda x :  cube(square(x))) 
print(power_6(3))