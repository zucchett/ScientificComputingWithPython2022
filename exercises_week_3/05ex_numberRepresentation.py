#5. Quadratic slution

from cmath import sqrt

def squares(a,b,c):
    squares = [0,0]
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    if(b**2 - 4*a*c < 0):
        return "Impossible"
    elif(b**2 - 4*a*c == 0):
        x_1 = (-b + sqrt(b**2 - 4*a*c))/2*a
        squares.append(x_1)
    else:
        x_1 = (-b + sqrt(b**2 - 4*a*c))/2*a
        x_2 = (-b - sqrt(b**2 - 4*a*c))/2*a 
        squares[0] = x_1
        squares[1] = x_2
    return squares
 
 
#a
a = 0.001
b = 1000
c = 0.001

print(squares(a,b,c))

#b
def squares_2(a,b,c):
    squares = [0,0]
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    m_1 = -b - sqrt(b**2 - 4*a*c)
    m_2 = -b + sqrt(b**2 - 4*a*c)
    
    if(b**2 - 4*a*c < 0):
        return "Impossible"
    elif(b**2 - 4*a*c == 0):
        x_1 = (-b + sqrt(b**2 - 4*a*c))*m_2/(2*a*m_2)
        squares.append(x_1)
    else:
        x_1 = (-b + sqrt(b**2 - 4*a*c))*m_2/(2*a*m_2)
        x_2 = (-b - sqrt(b**2 - 4*a*c))*m_1/(2*a*m_1) 
        squares[0] = x_1
        squares[1] = x_2
    return squares

print("This is the second function")
print(squares_2(a,b,c))

#c
def squares_2(a,b,c):
    squares = [0,0]
    
    a = int(a)
    b = int(b)
    c = int(c)
    
    m_1 = -b - sqrt(b**2 - 4*a*c)
    m_2 = -b + sqrt(b**2 - 4*a*c)
    
    if(b**2 - 4*a*c < 0):
        return "Impossible"
    elif(b**2 - 4*a*c == 0):
        x_1 = (-b + sqrt(b**2 - 4*a*c))*m_2/(2*a*m_2)
        squares.append(x_1)
    else:
        x_1 = (-b + sqrt(b**2 - 4*a*c))*m_2/(2*a*m_2)
        x_2 = (-b - sqrt(b**2 - 4*a*c))*m_1/(2*a*m_1) 
        squares[0] = x_1
        squares[1] = x_2
    return squares

print("This is the third function")
print(squares_2(a,b,c))