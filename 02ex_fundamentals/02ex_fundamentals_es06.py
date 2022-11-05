def square(n):
    return pow(n,2)

def cube(n):
    return pow(n,3)

def pow_6(n):
    return square(cube(n))

print(pow_6(2))
print(pow(2,6))