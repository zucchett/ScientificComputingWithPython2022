def square(num):
    return num*num

def cube(num):
    return num*num*num
    
print(square(2))
print(cube(2))

def sixth_pow(num):
    return cube(square(num))

print(sixth_pow(2))