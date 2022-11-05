def f(x):       # Implementing the function f(x) = x (x-1)
    return x*(x-1)

def derivative(x, delta):  # Calculate the derivative
    return (f(x+delta)-f(x))/delta

print("Analytically:  1")   # Analytically
for i in range(-2, -15, -2):  # calculation for delta = 10ˆ(-4), 10ˆ(-6), 10ˆ(-8), 10ˆ(-10), 10ˆ(12), 10ˆ(-14)
    print(f"delta = 1e{i} ---> f'(1)= {derivative(1, 10**(i))}")   # x = 1