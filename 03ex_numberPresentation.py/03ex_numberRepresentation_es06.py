# 6. The derivative

def f(x):
    return x * (x - 1)


def derivative(x, delta):  # derivative
    return (f(x+delta)-f(x))/delta


print("f'(x) = 2x-1 ")
print("f'(2) = 3")
for i in range(-2, -15, -2):  #  delta = 10ˆ(-4), 10ˆ(-6), 10ˆ(-8), 10ˆ(-10), 10ˆ(12), 10ˆ(-14)
    print(f"Delta = 1e{i} f'(1)= {derivative(2, 10**(i))}")