def f(x):#part A
    return (x - 1) * x
def Differentiation_of_f(x, i):
    return (f(x + i) - f(x)) / i

x = 1
derivative = Differentiation_of_f(1, 10 ** (-2))
print("derivative calculated normally: ", 1.01)
print("derivative calculated by program: ", derivative)
# true analytical is 1.01 but the program result is : 1.01000000000000089706020,
#   due to round-off error, we must consider the possibility of small errors being introduced in every computed value.
#because of many basic calculations and each one must be analyzed and,

for i in range(-4, -16, -2):# Part B
    delta = 10 ** i
    print("Derivative with " + str(delta) + " = " + str(Differentiation_of_f(x, delta)))

# Numerically unstable algorithms.so, part B result has various outcomes