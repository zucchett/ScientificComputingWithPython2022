import math

def quadratic_eq(a, b, c):
    x_p = ((math.sqrt(b ** 2 - (4 * a * c)))-b ) / (2 * a)
    x_m = (- (math.sqrt(b ** 2 - (4 * a * c)))-b ) / (2 * a)
    return {"plus": x_p, "minus": x_m}
# part a:
a = 0.002
b = 1100
c = 0.011
print(quadratic_eq(a, b, c))
def quadratic_eq_multiply(a, b, c):
    plus_num = (-b + (math.sqrt(b ** 2 - (4 * a * c))))
    minus_num = (-b - (math.sqrt(b ** 2 - (4 * a * c))))
    denominator = 2 * a
    plus_num_multiply_plus_num = (plus_num * plus_num) / (denominator * plus_num)
    plus_num_multiply_minus_num = (minus_num * plus_num) / (denominator * minus_num)
    minus_num_multiply_plus_num = (plus_num * minus_num) / (denominator * plus_num)
    minus_num_multiply_minus_num = (minus_num * minus_num) / (denominator * minus_num)
    return {"p-p": plus_num_multiply_plus_num, "p-m": plus_num_multiply_minus_num,
            "m-p": minus_num_multiply_plus_num, "m-m": minus_num_multiply_minus_num}

print("results",quadratic_eq_multiply(a, b, c))
# when you multiplying the formula with minus in numerator by (equation with plus), changes will happen.
# The difference occurs because limited float numbers with meaningful places.