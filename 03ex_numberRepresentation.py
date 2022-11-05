import numpy as np
from math import sqrt

###########
# PART 1  #
###########
print("PART 1\n")
def convertNumber(number,  output: type):
    # Convert the inputted number to string to process
    number = str(number)
    input_base = None

    # If we have the hexadecimal indicator
    if 'x' in number:
        input_base = 16
    # If we have the binary indicator
    elif 'b' in number:
        input_base = 2
    # It is in decimal format
    else:
        input_base = 10

    return output(int(number,input_base))

print("Decimal to Hex", convertNumber(11, hex))
print("Hex to Binary", convertNumber(hex(11), bin))
print("Binary to Decimal", convertNumber(bin(11), int))

###########
# PART 2  #
###########
print("\nPART 2\n")
def convertBinaryToFloating(number):
    # Split into meaningful parts
    sign = int(number[0])
    exponent_part = number[1:9]
    fraction = number[9:]

    # Exponent calculation
    integer = int(exponent_part,2)
    exponent = integer - ( pow(2, len(exponent_part)-1) -1 )

    # Mantissa calculation
    significand = 1
    for index, bit in enumerate(fraction):
        # If there is 1, calculate its digit value
        if bit == '1':
            significand += pow(2, -1*(index+1))

    # Apply the formula
    result = pow(-1,sign) * pow(2,exponent) * significand
    print("{} converted to floating point is {}".format(number,result))

convertBinaryToFloating("01000000110110000000000000000000")

###########
# PART 3  #
###########
print("\nPART 3\n")
def under_over_flow():
    underflow_value = 1.0
    overflow_value = 1.0
    limit = pow(2,20)

    underflow_trial_count = 0

    # Constantly divide the number until there is no meaningful change
    while(underflow_value > 0.0):
        underflow_value /= 2
        underflow_trial_count += 1

    overflow_temp_value = 0
    overflow_trial_count = 0
    # Constantly double the number until there is overflow or the limit is reached
    while(overflow_value >= overflow_temp_value and overflow_trial_count < limit):
        overflow_temp_value = 2 * overflow_value

        # Checking the sign of the doubled number to detect a change
        if np.sign(overflow_value) != np.sign(overflow_temp_value):
            break
        overflow_trial_count += 1
        overflow_value *= 2.0  
    
    print("Underflow limit is",underflow_trial_count)
    print("Overflow limit is",overflow_trial_count)

under_over_flow()

###########
# PART 4  #
###########
print("\nPART 4\n")
def machine_precision():
    floating_number = 1.0
    trial_count = 0
    limit = 10000

    # Constantly add a new number with greater significant fiugre until there is no change or the limit is reached 
    while(trial_count < limit):
        temp = pow(10,-1*(trial_count+1))
        temp_sum = floating_number + temp
        if temp_sum == floating_number:
            break
        floating_number = temp_sum
        trial_count += 1

    print("Machine precision limit is : {} and the result number is: {}".format(trial_count,floating_number))

machine_precision()

############
# PART 5/A #
############
print("\nPART 5\n")

# A simple discriminant method
def discriminant(a,b,c):
    return sqrt(pow(b,2) - 4*a*c)

# The standard quadratic formula
def quadratic(a,b,c):
    print("Standard quadratic formula")
    sol_1 = (-1*b + discriminant(a,b,c) ) / (2*a)
    sol_2 = (-1*b - discriminant(a,b,c) ) / (2*a)

    print("Solution x1={},\nSolution x2={}".format(sol_1, sol_2))

quadratic(a=0.001, b=1000, c=0.001)

############
# PART 5/B #
############

# The updated quadratic formula
def quadratic_updated(a,b,c):
    print("\nUpdated quadratic formula")
    sol_1 = (-1*b + discriminant(a,b,c) ) * (-1*b - discriminant(a,b,c)) / ( (2*a) * (-1*b - discriminant(a,b,c)))
    sol_2 = (-1*b - discriminant(a,b,c) ) * (-1*b + discriminant(a,b,c)) / ( (2*a) * (-1*b + discriminant(a,b,c)))
    
    print("Solution x1={},\nSolution x2={}".format(sol_1, sol_2))

quadratic_updated(a=0.001, b=1000, c=0.001)

# ANSWER, PART B:
# I have observed that the precision of my solution increased as 
# my second solution has more significant figures after the decimal point

###########
# PART 6  #
###########
print("\nPART 6\n")

def f(x):
    return x*(x-1)

def derivative(function, value):
    constant = pow(10,-2)
    numerator = function(value + constant) - function(value)
    denominator = constant
    result = numerator / denominator
    print("Result of the standard formula is", result)

def analytical():
    result = ( (2.01 * 1.01) - 2*1 ) / 0.01
    print("Result of the analytical solution is", result)

derivative(f,2)
analytical()