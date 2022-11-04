#squared:
def squared(x):
    return x**2
#cubed:
def cubed(x):
    return x*x*x
#sixth
def sixth_pow(x):
    return squared(x)*cubed(x)

print('second power of x=2: ', squared(2))
print('third power of x=2: ', cubed(2))
print('sixth power of x=2: ', sixth_pow(2))
