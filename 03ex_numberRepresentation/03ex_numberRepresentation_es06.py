import math as m


def sol1(a,b,c):
    x1 = (-b-m.sqrt(pow(b,2)-4*a*c))/(2*a)
    x2 = (-b+m.sqrt(pow(b,2)-4*a*c))/(2*a)
    return [x1,x2]

def sol2(a,b,c):
    x1 = (4*a*c)/(-2*a*b+2*a*m.sqrt(pow(b,2)-4*a*c))
    x2 = (4*a*c)/(-2*a*b-2*a*m.sqrt(pow(b,2)-4*a*c))
    return [x1,x2]


print('Check the two methods with random numbers')
print(sol1(2,-1,-3))
print(sol2(2,-1,-3))

print('Check the two methods with given numbers')
print(sol1(0.001,1000,0.001))
print(sol2(0.001,1000,0.001))

#the problem is the term -b + sqrt(b^2-4ac) that appears on the numerator of x2  in sol1 and on the denominaror of x1 in sol2