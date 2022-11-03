# a)

def f(x):
    return x*(x-1)

def derive(func, val):
    delta = 1e-2
    top = func(val + delta) - func(val)
    bottom = delta
    slope = top / bottom
    return float("%f" % slope)
print(f"The result of part a is: {derive(f,1)} ")

# b)
# when we have smaller delta , we have more accurate result.

def derive2(function, value):
    delta = 1e-2
    for i in range(0,6):
        delta = delta * 1e-2
        top = function(value + delta) - function(value)
        bottom = delta
        slope = top / bottom
        print(f"Result of the function with h {delta}  derivative imp. : ", float("%f" % slope))
        
derive2(f,1)

        