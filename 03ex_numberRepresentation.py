# Part 1.

# Since hexadecimal numbers are represented with '0x' and binary numbers with '0b' we can
# determine the type of the input.
# If its not hex, bin or dec program should warn the user
def converter(number, output_type):
    # We need to check if given output_type is valid
    if output_type not in ["hex", "bin", "dec"]:
        print("Output type is not valid")
        return
    input_type = None
    if "0x" in number:
        input_type = "hex"
    elif "0b" in number:
        input_type = "bin"
    else:
        input_type = "dec"
    

    if input_type == "dec":
        if output_type == "bin":
            result = bin(int(number))
        elif output_type == "dec":
            result = number
        elif output_type == "hex":
            result = hex(int(number))
        else:
            print("Incorrect output type")
            return

    elif input_type == "bin":
        if output_type == "bin":
            result = number
        elif output_type == "dec":
            result = int(number, 2)
        elif output_type == "hex":
            result = hex(int(number,2))
        else:
            print("Incorrect output type")
            return
    
    elif input_type == "hex":
        if output_type == "bin":
            result = bin(int(number, 16))
        elif output_type == "dec":
            result = int(number, 16)
        elif output_type == "hex":
            result = number
        else:
            print("Incorrect output type")
            return
    else:
        print("Incorrect input type")
        return

    return result

result = converter("156", "hex")
print(result)

# Part 2.
def converter(number):
    sign_bit = number[0]
    exponent_bits = number[1:9]
    mantissa_bits = number[9:]
    bias = 127

    # Calculating exponent and sign
    exponent = int(exponent_bits, 2) - bias
    sign = pow(-1, int(sign_bit))

    fraction = 1
    # Getting the fraction from mantissa bits
    for index, bit in enumerate(mantissa_bits):
        fraction += int(bit) * pow(2, -(index+1))
    
    # Getting result from the IEEE754 formula
    result = sign * fraction * pow(2, exponent)

    print("number:", number)
    print("sign", sign)
    print("exponent", exponent)
    print("fraction", fraction)

    return result

result = converter("01000000110111000111101011100001")
print("Result of conversion is:", result)

# Part 3.
limit = 5000
underflow = 1
overflow = 1
factor = 2

for i in range(limit):
    if underflow / 2 == 0.0:
        print("Reached underflow limit at trial:", i, "with number:", underflow)
        break
    underflow = underflow / factor
    overflow = overflow * factor
    print("Trial:", i, "Underflow:", underflow, "Overflow:", overflow)

# Some comments in prints about the problem:
print("Theoretically it should reach underflow limit in 2**-1022 but apparently it can be extended using denormal numbers (which my example does) so the limit is 2**(-1074).")
print("Also Python does not have an overflow limit.")

# Part 4.
num = 1
factor = 2
limit = 10000
# Without getting to the specified limit it can be seen that addition becomes effectless
for i in range(limit):
    addition_res = num + factor**(-(i+1))
    if addition_res == num:
        print("Addition has no longer any effects with trial:", i, "and number:", num)
        break
    num = addition_res
    
# Part 5.a)
from math import sqrt
def quadratic(a, b, c):
    discriminant = sqrt(b**2 - 4*a*c)
    root_1 = (-b + discriminant) / (2*a)
    root_2 = (-b - discriminant) / (2*a)
    return root_1, root_2

root_1, root_2 = quadratic(0.001, 1000, 0.001)
print("First root:", root_1, "Second root:", root_2)

# Part 5.b)
def quadratic_2(a, b, c):
    discriminant = sqrt(b**2 - 4*a*c)
    root_1 = ((-b + discriminant) * (-b - discriminant)) / (2*a * (-b - discriminant))
    root_2 = ((-b - discriminant) * (-b + discriminant)) / (2*a * (-b + discriminant))
    return root_1, root_2

root_1, root_2 = quadratic_2(0.001, 1000, 0.001)
print("First root:", root_1, "Second root:", root_2)


# Part 6.a)
def f(x):
    return x * (x - 1)
def derivative(x, delta):
    return (f(x + delta) - f(x)) / delta

result = derivative(2, 10**-2)
print(result)

true_value = (2.01 * 1.01 - 2.0 * 1) / 0.01
print(true_value)

#
# By adding and multiplying by hand (for examole (1 + 1.01) * 1.01) we get a different result compared to python
# because as seen in lecture notebook python greets the numbers floating parts more detailly, therefore
# the end results becomes different between analytically calculated result and python's result.
#

# Part 6.b)
delta_values = [10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]

for delta in delta_values:
    print("For delta = ", delta)
    result = derivative(2, delta)
    print("Result of derivative function:", result)

    true_value = (((2 + delta) * (1 + delta)) - 2.0 * 1) / delta
    print("Analytically calculated value:", true_value)
# While the delta value gets smaller, accuracy also decreases.