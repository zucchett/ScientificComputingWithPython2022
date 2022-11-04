# 6. The Derivative

def fx(x):
    return x*(x-1)


def derivative(x,delta):
    return (fx(x+delta) - fx(x))/delta

value = [derivative(1,10**-x) for x in range(2,15,2)] # A list with derivatives for delta from 10^-2 to 10^-14

print(value)

# The Accuracy increases as we move from 10^-2 to 10^-8 as we move delta towards zero but from 10^-10 to 10^-14 the answer moves away from the analytical answer (i.e `1`).