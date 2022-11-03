#5. Quadratic solution


#a
from math import sqrt 
def f1(a,b,c):
    x1= (-b+sqrt(b**2-4*a*c))/(2*a)
    x2= (-b-sqrt(b**2-4*a*c))/(2*a)
    return x1 ,x2
a=0.001
b=1000
c=0.001
x1,x2=f1(a,b,c)
print("x1=",x1,"x2=",x2)
print("ax1**2+b*x1+c=",a*(x1**2)+b*x1+c)
print("ax2**2+b*x2+c=",a*(x2**2)+b*x2+c)
#ax**2+b*x+c is supposed to give us 0 which is not the case
#Actually, in python, the more similar two float numbers are, the more precision you can lose from subtracting them.
#In this case √(b² – 4ac) is very nearly equal to b (Cancellation error)

#b
def f2(a,b,c):
    #by multiplying the numerator and the denominator with -b+sqrt(b**2-4*a*c) the expression becomes:
    x1= (2*c)/(-b-sqrt(b**2-4*a*c))
    x2= (2*c)/(-b+sqrt(b**2-4*a*c))
    return x1 ,x2
x1,x2=f2(a,b,c)
print("x1=",x1,"x2=",x2)
print("ax1**2+b*x1+c=",a*(x1**2)+b*x1+c)
print("ax2**2+b*x2+c=",a*(x2**2)+b*x2+c)

#Here the first solution is right but the second solution is wrong.
#The reason is the same as before as we are subtracted two nearly equal numbers. 


#This result shows more precision in the result

#c
def f3(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta > 0:
        x1= (-b+sqrt(b**2-4*a*c))/(2*a)
        x2= (-b-sqrt(b*b-4*a*c))/(2*a)
    elif delta <0:
        x1= complex(-b/(2*a),((sqrt(-delta))/(2*a)))
        x2= complex(-b/(2*a) , ((sqrt(-delta))/(2*a)))
    else:
        return(-b/(2*a))
    return x1 ,x2
#print(f3(1,4,5))
#print(f3(1,-4,3))
