# 6. The derivative

import math

def f(x):
    return x*(x-1)

def der_f(x):
    return (2*x-1)

delta = 1

d_f_analitic = der_f(1)

print("The derivative computed analytically is " + str(d_f_analitic))
print("\n")

accuracy = []

for i in range(0, 7):

    delta = delta*(0.01)

    d_f = (f(1+delta)-f(1))/delta

    print("Case delta = " + str(delta))
    print("The approximation of the derivative is " + str(d_f))
    print("The derivative computed in " + str(1 + delta) + " is " + str(d_f_analitic))
    accuracy.append(format(100-(abs(d_f_analitic - d_f)*100), '.8f') + " %")
    print("The accuracy is " + str(format(100-(abs(d_f_analitic - d_f)*100), '.8f')) + " %")
    print('\n')
  
print("The accuracy of the derivative computed with smaller and smaller values of delta is: ")
print(accuracy)

# at the beginning the accuracy is of 99% and in the next three measurements it increases becoming closer and closer to the true value
# however in the last three computations (with the smallest delta) we can see a tiny decrease of the accuracy that might be due to the finite-precision represententation of numbers

# exercise completed ?