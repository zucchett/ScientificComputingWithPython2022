from math import exp
import timeit
from scipy.integrate import quad


def semi_circle(x):
    return exp((1 - (x ** 2)) ** 1 / 2)


result = quad(semi_circle, -1, 1)  # we use quad for general purpose integration
print("Result of the integral is:", result)

# (a) compute integral with N=100
N = 100


def rienmann_integral(n, fun):
    sol = 0
    h = 2 / N
    for i in range(N):
        sol = sol + h * fun(i)  # Yk value is the value of the function at the kth slice, so func(i)
        return sol


print(rienmann_integral(N, semi_circle))

# (b) how much can n be increased


print(rienmann_integral(N * 10 ** 2, semi_circle))
duration = timeit.default_timer()
print("the time is:", duration)
