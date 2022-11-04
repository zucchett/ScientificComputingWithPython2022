def f(x):
    return x * (x-1)

def derivative(f, x, delta = 10**(-2)):
    dx = delta
    return (f(x + delta) - f(x)) / dx

# a)
x = 1
result = derivative(func, x)
print("Derivative of f (func): ",result)
deriv = 2*x - 1
print("Derivative of f (math) = ",deriv)
# the above values are almost same that is the result of the program slightly changes from true value, and it's numerically stable

# b)

deltaList = [10**(-4), 10**(-6), 10**(-8), 10**(-10), 10**(-12), 10**(-14)]

for i in deltaList:
    print("\n Derivative on ",str(i)," = ",derivative(func, x, i))
#as the input delta decreases there is a gradual decrease in the output and the system is well stable
