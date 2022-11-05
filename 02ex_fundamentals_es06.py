from re import X


def square(n):
    x = n**2
    return x

def cube(n):
    x = n**3
    return x

def sixPower(n):
    a = square(n)
    b = cube(a)
    return b

n = int(input("please inpute the number: "))
print("the square is: ",square(n))
print("the cube is: ",cube(n))
print("the sixPower is: ",sixPower(n))