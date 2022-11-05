import sympy

#A
def f(x):
    fx=x*(x-1)
    return fx

def derivativ(y,delta):
    return (f(y+delta)-f(y))/delta

defn_result=derivativ(1,10**-2)
print("Derivative definition result:",defn_result)

x=sympy.symbols('x')
analytically_result=sympy.diff(x*(x-1))
print("analytically derivative is:",analytically_result)

f=x*(x-1)
f = sympy.lambdify(x, f)
f_prime = sympy.lambdify(x, analytically_result )
print("analytically  result:",f_prime(1))

 # Because analytically one of is stable other one is unstable.

#B
sigma=[10**(-4) ,10**(-6),10**(-8) ,10**(-10) ,10**(-12) ,10**(-14)]

for i in range(len(sigma)):
    defn_result=derivativ(1,sigma[i])
    print("Derivative with sigma=", sigma[i],"result:",defn_result)

# The accuracy increasing while the sigma is decreasing untill the some point.

