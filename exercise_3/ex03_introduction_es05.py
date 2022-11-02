import math


def quadratic_equation(a, b, c):
    x_plus = (-b + (math.sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    x_minus = (-b - (math.sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    return {"plus": x_plus, "minus": x_minus}


# part a:
a = 0.001
b = 1000
c = 0.001
print(quadratic_equation(a, b, c))


def quadratic_equation_multiply(a, b, c):
    plus_numerator = (-b + (math.sqrt(b ** 2 - (4 * a * c))))
    minus_numerator = (-b - (math.sqrt(b ** 2 - (4 * a * c))))
    denominator = 2 * a
    plus_numerator_multiply_plus_numerator = (plus_numerator * plus_numerator) / (denominator * plus_numerator)
    plus_numerator_multiply_minus_numerator = (minus_numerator * plus_numerator) / (denominator * minus_numerator)
    minus_numerator_multiply_plus_numerator = (plus_numerator * minus_numerator) / (denominator * plus_numerator)
    minus_numerator_multiply_minus_numerator = (minus_numerator * minus_numerator) / (denominator * minus_numerator)
    return {"p-p": plus_numerator_multiply_plus_numerator, "p-m": plus_numerator_multiply_minus_numerator,
            "m-p": minus_numerator_multiply_plus_numerator, "m-m": minus_numerator_multiply_minus_numerator}


print(quadratic_equation_multiply(a, b, c))

# The only change happened in multiplying the formula with minus in numerator by the equation with plus in it.
# The difference is only 1.0e-10 and that is because float numbers has limited number of meaningful places.
