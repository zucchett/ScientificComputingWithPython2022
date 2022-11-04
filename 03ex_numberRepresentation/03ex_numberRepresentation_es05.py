import math

def computeQuadraticEquation_V1(a, b, c):
    print("Ans 1:", (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    print("Ans 2:", (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)

def computeQuadraticEquation_V2(a, b, c):
    print("Ans 1:", ((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a) * (-b - math.sqrt(b ** 2 - 4 * a * c)) / (-b - math.sqrt(b ** 2 - 4 * a * c)))
    print("Ans 2:", ((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a) * (-b + math.sqrt(b ** 2 - 4 * a * c)) / (-b + math.sqrt(b ** 2 - 4 * a * c)))

def computeQuadraticEquation_V22(a, b, c):
    print("Ans 1:", (4 * a * c) / ((-2 * a * b) - (2 * a * (math.sqrt((b ** 2) - (4 * a * c))))))
    print("Ans 2:", (4 * a * c) / ((-2 * a * b) + (2 * a * (math.sqrt((b ** 2) - (4 * a * c))))))

def computeQuadraticEquation_V3(a, b, c): 
    if a == 0: 
        if b == 0: 
            print("")
            return 
        else: 
            print("Ans:", -c / b)
            return 
    print("Ans 1:", (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    print("Ans 2:", (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)

a = 0.001
b = 1000
c = 0.001

computeQuadraticEquation_V1(a, b, c)
computeQuadraticEquation_V22(a, b, c)
computeQuadraticEquation_V3(a, b, c)