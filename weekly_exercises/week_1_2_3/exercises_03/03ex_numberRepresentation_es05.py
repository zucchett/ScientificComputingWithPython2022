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


print(">>>>>>>>>>>>>> PART 0)\n")
parameters = inputValues()
standardSolution(parameters)

print("\n>>>>>>>>>>>>>> PART a)\n")
parameters = [0.001, 1000, 0.001]
print("a =", parameters[0], "\nb =", parameters[1], "\nc =", parameters[2])
standardSolution(parameters)

print("\n>>>>>>>>>>>>>> PART b)\n")
parameters = [0.001, 1000, 0.001]
print("a =", parameters[0], "\nb =", parameters[1], "\nc =", parameters[2])
bSolution(parameters)

# solutions are different because of the the precision of the float value are not so accuracy