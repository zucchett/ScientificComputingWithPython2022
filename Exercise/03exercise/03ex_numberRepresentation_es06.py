#6. The derivative
#Part a:
def f(x):
    return (x * (x-1))
#lim[f(x+d)]-f(x)]/d = ([f(1+0.01) - f(1)]/0.01)
driv=(f(1 + 0.01) - f(1)) /0.01
print("derivative is:" , driv)
print("step derivative is: 1.01, derivative in analytically : 2x -1 -> for x=1 : derivative = 1")

#part b:
dList =[10e-4, 10e-6, 10e-8, 10e-10, 10e-12]
for i in dList:
    driv =(f(1 + i) - f(1))/i
    print("derivation is: ", driv)
    
print("In each step the derivation are closed to absolute derivation which is equal to 1")
