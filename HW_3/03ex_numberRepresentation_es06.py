# (a) calculate derivative
def func(x):
    return x * (x - 1)


def calc_derivative(x, doh_value):
    solution = (func(x + doh_value) - func(x)) / doh_value
    return solution


x = 1
print(calc_derivative(x, 10 ^ -2))
# (b)  Repeat the calculation for  𝛿=10−4,10−6,10−8,10−10,10−12  and  10−14
print(calc_derivative(x, 10 ^ -4))
print(calc_derivative(x, 10 ^ -6))
print(calc_derivative(x, 10 ^ -8))
print(calc_derivative(x, 10 ^ -10))
print(calc_derivative(x, 10 ^ -12))
print(calc_derivative(x, 10 ^ -14))

