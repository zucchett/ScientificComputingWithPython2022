"""
6\. **The derivative**

Write a program that implements the function $f(x)=x(x−1)$

(a) Calculate the derivative of the function at the point $x = 1$ using the derivative definition:

$$
\frac{{\rm d}f}{{\rm d}x} = \lim_{\delta\to0} \frac{f(x+\delta)-f(x)}{\delta}
$$

with $\delta = 10^{−2}$. Calculate the true value of the same derivative analytically and compare it with the answer
your program gives. The two will not agree perfectly. Why?

(b) Repeat the calculation for $\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 10^{−12}$ and $10^{−14}$. How does the
accuracy scale with $\delta$?
"""

f = lambda x: x * (x - 1)

d = (f(1 + 10 ** -2) - f(1)) / 10 ** -2

print("a) df/dx = ", d, "  The algorithm doesn't have enough numerical stability \n")

for b in [4, 6, 8, 10, 12, 14, 16]:
    print("Value of the derivative for delta = 10^-{} = ".format(b), (f(1 + 10 ** -b) - f(1)) / 10 ** -b)

# b) I would say that there is no precise correlation between delta and the result. The closest value is reached with 10^-8.
