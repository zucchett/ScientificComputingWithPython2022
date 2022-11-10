#5. Quadratic slution

from cmath import sqrt

#a
a = 0.001
b = 1000
c = 0.001

def roots(a,b,c): #first method to solve the equation
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    x_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    
    return [x_1,x_2]
 
#b
def roots_2(a,b,c):
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    m_1 = -b - sqrt(b**2 - 4*a*c)
    m_2 = -b + sqrt(b**2 - 4*a*c)

    x_1 = (2*c)/m_1
    x_2 = (2*c)/m_2

    return [x_1,x_2]
#in these two solutions there are errors due to the limited precision of the floating point numbers

#c
#to eliminate the error we should avoid the substraction of really close numbers
def roots_3(a,b,c):
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    if( b >= 0):
        x_1 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    else:
        x_1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = c/(a*x_1)
    
    return [x_1,x_2]

print("By using the classic formula these are the results: ",roots(a,b,c))
print("By using the second method these are the results: ",roots_2(a,b,c))
print("By using the third method these are the results: ",roots_3(a,b,c))

