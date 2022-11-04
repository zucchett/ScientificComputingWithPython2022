def f(x):
    return x * (x - 1)


def derivative_of_f(x, d):
    return (f(x + d) - f(x)) / d


x = 1
derivative = derivative_of_f(1, 10 ** (-2))
print("derivative calculated analytically: ", 1.01)
print("derivative calculated by program: ", derivative)
# The true analytical value of the derivative is 1.01 but the program gives the answer: 1.01000000000000089706020,
# so they are not agreeing perfectly. This is because the derivative function of f(x) consists of many basic
# calculations and each one must be analyzed and, due to round-off error, we must consider the possibility of small
# errors being introduced in every computed value.

# Part B
for d in range(-4, -16, -2):
    delta = 10 ** d
    print("Derivative with " + str(delta) + " = " + str(derivative_of_f(x, delta)))

# Numerically unstable algorithms tend to amplify approximation errors due to computer arithmetic over time. Because
# of this the output of part B has various outcomes which are different from the true values of the calculation of
# derivative analytically. (If delta ---> 0 then the derivative should ---> 1.0)
