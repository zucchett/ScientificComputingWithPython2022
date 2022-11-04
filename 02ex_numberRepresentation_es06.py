#squared:
def squared(x):
    return x**2
#cubed:
def cubed(x):
    return x*x*x
#sixth
def sixth_pow(x):
    return squared(x)*cubed(x)

print('sixth power:', sixth_pow(2))
