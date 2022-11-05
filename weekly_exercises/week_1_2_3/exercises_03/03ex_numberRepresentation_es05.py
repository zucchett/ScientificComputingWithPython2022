#Zuccolo Giada, matr. 2055702
# EXE 5
import math
from fractions import Fraction

def inputValues():
    print("Parameters")
    while True:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        if check_values(a,b,c):
            break
    return a,b,c

def check_values(a,b,c):
    if (pow(b, 2) - 4 * a * c)<0:
        print("Wrong values| Try again!")
        return False
    else:
        return True

def standardSolution(parameters):
    a, b, c = parameters[0], parameters[1], parameters[2]
    solutions = [((-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)),
                 ((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a))]
    print("\nSolutions\nx1 = ", Fraction(solutions[0]), "\nx2 = ",
      Fraction(solutions[1]))

def bSolution(parameters):
    a, b, c = parameters[0], parameters[1], parameters[2]
    solutions = [
        (4 * a * c) / (2 * a * (-b - math.sqrt(pow(b, 2) - 4 * a * c))),
        (4 * a * c) / (2 * a * (-b + math.sqrt(pow(b, 2) - 4 * a * c)))
    ]
    print("\nSolutions\nx1 = ", Fraction(solutions[0]), "\nx2 = ",
          Fraction(solutions[1]))

def cSolution(parameters):
    a, b, c = parameters[0], parameters[1], parameters[2]
    solutions = []
    if b >= 0:
        solutions = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a), c / (a * ((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)))
    else:
        solutions = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a), c / (a * ((-b - math.sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)))

    print("\nSolutions\nx1 = ", (solutions[0]), "\nx2 = ", (solutions[1]))


print(">>>>>>>>>>>>>> PART 0)\n")
parameters_input = inputValues()
standardSolution(parameters_input)

print("\n>>>>>>>>>>>>>> PART a)\n")
parameters_prof = [0.001, 1000, 0.001]
print("a =", parameters_prof[0], "\nb =", parameters_prof[1], "\nc =", parameters_prof[2])
standardSolution(parameters_prof)

print("\n>>>>>>>>>>>>>> PART b)\n")
print("a =", parameters_prof[0], "\nb =", parameters_prof[1], "\nc =", parameters_prof[2])
bSolution(parameters_prof)

# solutions are different because of the the precision of the float value are not so accurate

print("\n>>>>>>>>>>>>>> PART c)\n---- Input parameters")
print("a =", parameters_input[0], "\nb =", parameters_input[1], "\nc =", parameters_input[2])
cSolution(parameters_prof)

print("\n---- Prof parameters")
print("a =", parameters_prof[0], "\nb =", parameters_prof[1], "\nc =", parameters_prof[2])
cSolution(parameters_prof)