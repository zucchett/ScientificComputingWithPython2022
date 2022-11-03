import sympy
from sympy import *
def limit(z):
    x = 1
    zi = symbols('zi')
    expretion = (((x + zi)*(x + zi + 1 )) - (x*(x-1)))
    limit_expretion = sympy.limit(expretion,zi,0)
    return limit_expretion
print(limit(0.01))
#------------------------------------------------------------------------------------------------------
zigma_list = [10**-4,10**-6,10**-8,10**-10,10**-12,10**-14]
for i in zigma_list :
    print(f'the derivative of function with zigma = {i} is equal to :  {limit(i)}')
#according to the result that is calculated by python with different zigma we have the same answer 
#--------------------------------------------------------------------------------------------------------