"""
7\. **Integral of a semicircle**

Consider the integral of the semicircle of radius 1:
$$
I=\int_{-1}^{1} \sqrt(1-x^2) {\rm d}x
$$
which is known to be $I=\frac{\pi}{2}=1.57079632679...$.

Alternatively we can use the Riemann definition of the integral:
$$
I=\lim_{N\to\infty} \sum_{k=1}^{N} h y_k
$$

with $h=2/N$ the width of each of the $N$ slices the domain is divided into and where
$y_k$ is the value of the function at the $k-$th slice.

(a) Write a program to compute the integral with $N=100$. How does the result compare to the true value?

(b) How much can $N$ be increased if the computation needs to be run in less than a second? What is the gain in
running it for 1 minute? Use `timeit` to measure the time.
"""
from cmath import phase
from math import pi
import timeit


def semi_circle(x):
    return (1 - (x ** 2)) ** (1 / 2)


def integral(N, UpperLimit, LowerLimit, f):
    result = 0
    h = (UpperLimit - LowerLimit) / N  # 2/N
    for i in range(N):
        result = result + h * f(i)
    return phase(result)


# a)
N = 100
upper_limit = 1
lower_limit = -1
print("Result of integral: " + str(integral(N, upper_limit, lower_limit, semi_circle)))
print("pi / 2 = " + str(pi / 2))
# The difference between the true value and the result of the integral is 0.00020214747626989826

# b)
TimeStarts = timeit.default_timer()
integral(N * 12002, upper_limit, lower_limit, semi_circle)
TimeEnds = timeit.default_timer() - TimeStarts
print("Execution time for integral: " + str(TimeEnds) + " seconds")
# N can be multiplied approximately 12002 times for the computation needs
# to be run in less than a second.

TimeStarts = timeit.default_timer()
res = integral(N * 12002 * 60, upper_limit, lower_limit, semi_circle)
TimeEnds = timeit.default_timer() - TimeStarts
print("Execution time for integral: " + str(TimeEnds) + " seconds")
print("Result of (1 minute) integral: " + str(res))
# The difference between the true value and the result of the integral (1 min) is
# approximately 4.440892098500626e-16,
# the result gets closer to the true value if N is increased (time of the execution
# is increased)
