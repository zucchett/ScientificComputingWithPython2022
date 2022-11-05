# 6. The Derivative
def fx(x):
    return x*(x-1)


def derivative(x,delta):
    return (fx(x+delta) - fx(x))/delta

print(derivative(1,10**-2)) # Part a 

derivatives = [derivative(1,10**-x) for x in range(2,15,2)] # Part b : A list with derivatives for delta from 10^-2 to 10^-14

print(derivatives)

# For loop to determine percentage change in the values for the decrease in delta by factor 10^-2

for val in derivatives:
    print(abs(val-1)*100/val)

# Answer:
# Analytically the derivative of the function at x = 1 is equal to 1
# The Accuracy increases as we move from 10^-2 to 10^-8 as we move delta towards zero but from 10^-10 to 10^-14 the answer moves away from the analytical answer (i.e `1`).