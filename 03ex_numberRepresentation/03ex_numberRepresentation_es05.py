import math
a = float(input('please insert the value of "a" : '))
b = float(input('please insert the value of "b" : '))
c = float(input('please insert the value of "c" : '))

def solution_A():
    x1_A= (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2_A= (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return x1_A,x2_A
print(f'x1 and x2 for part A:  {solution_A()}')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def solution_B():
    x1_B = ((-b + math.sqrt(b**2 - 4*a*c))*(-b - math.sqrt(b**2 - 4*a*c)))/((2*a)*(-b - math.sqrt(b**2 - 4*a*c))) 
    x2_B = ((-b - math.sqrt(b**2 - 4*a*c))*(-b + math.sqrt(b**2 - 4*a*c)))/((2*a)*(-b + math.sqrt(b**2 - 4*a*c)))
    return x1_B,x2_B
print(f'x1 and x2 for part B:  {solution_B()}')
# the answer does not change because we multiplying the the same matematical operation on numerator and the denominator,so, the answer is unchanged.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------   
def solution_c():
    delta = b**2 - 4*a*c
    x1_C = (-b + math.sqrt(delta))/(2*a)
    x2_C = (-b - math.sqrt(delta))/(2*a)
    return x1_C,x2_C
print(f'x1 and x2 for part C:  {solution_c()}')
