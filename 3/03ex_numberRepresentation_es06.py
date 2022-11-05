# 6. The derivative

# Write a program that implements the function $f(x)=x(x−1)$

# (a) Calculate the derivative of the function at the point $x = 1$ using the 
# derivative definition:
# $$
# \frac{{\rm d}f}{{\rm d}x} = \lim_{\delta\to0} \frac{f(x+\delta)-f(x)}{\delta}
# $$
# with $\delta = 10^{−2}$. 
# Calculate the true value of the same derivative 
# analytically and compare it with the answer your program gives. The two will not 
# agree perfectly. Why?

# (b) Repeat the calculation for $\delta = 10^{−4}, 10^{−6}, 10^{−8}, 10^{−10}, 
# 10^{−12}$ and $10^{−14}$. How does the accuracy scale with $\delta$?

def f(x:int):
    return x*(x-1)

def derivative(f, x:int, delta = 10**(-2)):
    xph = x + delta
    dx = xph - x
    return (f(x + delta) - f(x)) / dx

#a)
x = 1
res = derivative(f, x)
print("Result of derivative: "+str(res))
derivative_of_f = 2*x - 1
print("Result of derivative (analytically) = "+str(derivative_of_f))

# The two results are not agreeing perfectly, because the calculation is not 100% correct.
# In the formulation of the derivative, the delta is approaching to zero (even there is a initial value),
# but when we're calculating by hand, we're giving a discrete value for it. When delta gets smaller, the
# result will become correct because delta is more close to zero.

#b)
deltas = [10**(-4), 10**(-6), 10**(-8), 10**(-10), 10**(-12), 10**(-14)]

for i in deltas:
    print("Derivative with "+str(i) +" = "+str(derivative(f, x, i)))

# When delta gets smaller, the accuracy increases (the result becomes more correct).