#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
def f(x):
    return (x)*(x-1)

def der(delta):
    x = 1
    return (f(x+delta)-f(x))/delta

print("The value of the derivative for delta = 10^(-2) is: ",der(1e-2))
print("The value of the derivative for delta = 10^(-4) is: ",der(1e-4))
print("The value of the derivative for delta = 10^(-6) is: ",der(1e-6))
print("The value of the derivative for delta = 10^(-8) is: ",der(1e-8))
print("The value of the derivative for delta = 10^(-10) is: ",der(1e-10))
print("The value of the derivative for delta = 10^(-12) is: ",der(1e-12))
print("The value of the derivative for delta = 10^(-14) is: ",der(1e-14))
print("ACCURACY")
print("The accuracy for delta = 10^(-2) is: ",1-der(1e-2))
print("The accuracy for delta = 10^(-4) is: ",1-der(1e-4))
print("The accuracy for delta = 10^(-6) is: ",1-der(1e-6))
print("The accuracy for delta = 10^(-8) is: ",1-der(1e-8))
print("The accuracy for delta = 10^(-10) is: ",1-der(1e-10))
print("The accuracy for delta = 10^(-12) is: ",1-der(1e-12))
print("The accuracy for delta = 10^(-14) is: ",1-der(1e-14))


# I see that accuracy becomes better up to delta = 10^(-8) and then starts decreasing
