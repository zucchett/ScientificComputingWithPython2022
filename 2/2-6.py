def square(x):
    return x**2
  
def cube(x):
    return x**3

def six_power(x):
    return cube(square(x))

six_power(2)
