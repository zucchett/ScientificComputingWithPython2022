def square(x):
    return x**2
def cube(x):
    return square(x)*x

def third_function(x):
    return cube(x)**2

print(third_function(3))