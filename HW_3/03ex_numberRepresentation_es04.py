count = 20
var = 0.034
frac = 0.1 + 1e-1  # since we need precision for floating point numbers
for i in range(count):
    frac = frac * 1e-3  # everytime the loop runs the fraction must get smaller
    var = var + frac  # everytime the loop runs the variable must get smaller
    print(i, var)  # from 4th there is no change in the number
