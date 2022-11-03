import math


def quadratic_equation(a, b, c):
    x1 = (-b + (math.sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    x2 = (-b - (math.sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    return {"x1": x1, "x2": x2}


# part a:
a = 0.001
b = 1000
c = 0.001
print(quadratic_equation(a, b, c))


print("----------Part B ------------")
# part b:
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


# The first quadratic equation yield the solution: -999999.999999 for the case with minus in its numerator,
# and when multiplied by the numerator with + in it, the solution was -999999.9999990001. This is because that this
# multiply resulted in adding around 1.0e-10 to the solution which was around '-999999.9999990001088008284'.
# Since float numbers has limited number of meaningful decimal places -in this case only 10 decimal places- it rounded
# the result to '-999999.9999990001'.
# The other cases didn't change.

print("----------Part C ------------")
# part c:
def roots_of_quadratic(a, b, c):
    print("calculating roots for a=%d, b=%d, c=%d" % (a,b,c))
    discriminant = b ** 2 - (4 * a * c)
    if discriminant > 0:
        x1 = (-b + (math.sqrt(discriminant))) / (2 * a)
        x2 = (-b - (math.sqrt(discriminant))) / (2 * a)
        print("The calculated roots are real and different:")
        print("x1 = %f and x2 = %f" % (x1, x2))
    elif discriminant == 0:
        x1 = x2 = -b / (2 * a)
        print("The calculated roots are real and equal:")
        print("x1 = %f and x2 = %f" % (x1, x2))
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-discriminant) / (2 * a)
        print("The calculated roots are complex:")
        print("x1 = ", real, " + ", imaginary, "i")
        print("x2 = ", real, " - ", imaginary, "i")
    print("-----------------End of function -------------------")


roots_of_quadratic(5, 3, 6)
roots_of_quadratic(3, 10, 5)
roots_of_quadratic(a, b, c)
