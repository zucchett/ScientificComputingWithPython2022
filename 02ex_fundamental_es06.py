square = (lambda x: x**2)
cube = (lambda x: x**3)
power_6 = (lambda x : square(cube(x))) 
print(power_6(2))