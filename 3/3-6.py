def f(x):
    return x * (x - 1)


def derivative_of_f(x, d):
    return (f(x + d) - f(x)) / d


x = 1
derivative = derivative_of_f(1, -2)
print("derivative calculated analytically: ", 1.01)
print("derivative calculated by program: ", derivative)

# Part B
for d in range(-4, -16, -2):
    print("Derivative with " , d , " = " , derivative_of_f(x, d))
    