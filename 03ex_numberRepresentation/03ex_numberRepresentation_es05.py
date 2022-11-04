import math 

def quadratic_eq(a, b, c):
    x1 = (-b + ((b**2 - 4*a*c)**(1/2))) / (2*a)
    x2 = (-b - ((b**2 - 4*a*c)**(1/2))) / (2*a)
    print("x1: ",x1)
    print("x2: ",x2)

# case (a)

a = 0.001
b = 1000
c = 0.001
print("Given a:",a ,"b:",b ,"c:",c)

quadratic_eq(a, b, c)
print("\n")

# case (b)

def quadratic_eq2(a, b, c):
    x1_1 = ((-b + (b**2 - 4*a*c)**(1/2)) * (-b + ((b**2 - 4*a*c)**(1/2)))) / ((2*a) * (-b + ((b*b - 4*a*c)**(1/2))))
    x1_2 = ((-b + (b**2 - 4*a*c)**(1/2)) * (-b - ((b**2  - 4*a*c)**(1/2)))) / ((2*a) * (-b - ((b*b - 4*a*c)**(1/2))))
    x2_1 = ((-b - (b**2 - 4*a*c)**(1/2)) * (-b + ((b**2  - 4*a*c)**(1/2)))) / ((2*a) * (-b + ((b*b - 4*a*c)**(1/2))))
    x2_2 = ((-b - (b**2 - 4*a*c)**(1/2)) * (-b - ((b**2  - 4*a*c)**(1/2)))) / ((2*a) * (-b - ((b*b - 4*a*c)**(1/2))))
    print("x1_1: ", x1_1)
    print("x1_2: ", x1_2)
    print("x2_1: ", x2_1)
    print("x2_2: ", x2_2)

print("Given a:",a ,"b:",b ,"c:",c)
quadratic_eq2(a, b, c)
print("\n")
# The results x2_1 and x2_2 are slightly different due to performing calculations with floating point number and 
# the accuracy might vary a little


# case (c)

def quadraticSolution(a,b,c):
    a_per_c = (a*c)
    delta = (b**2) - (4*a_per_c)
    
    x1 = (- b - ( math.sqrt(delta))) / (2*a)
    y1 = 2*c / (- b + (math.sqrt(delta)))
    x2 =  (- b + ( math.sqrt(delta))) / (2*a)
    y2 = 2*c / (- b - ( math.sqrt(delta)))
    return x1, y1, x2, y2

x1, y1, x2, y2 = quadraticSolution(a,b,c)
print('Results using the final function: ', '\n', 'x1 = ', x1, '\n', 'y1 = ', y2, '\n', 'x2 = ', x2, '\n', 'y2 = ', y2)
