# Q6 Function that returns two values
def square(x):
    return x**2

def cube(x):
    return x**3
    
def powsix(x):
    return cube(square(x))

print(square(3))
print(cube(3))
print(powsix(3))