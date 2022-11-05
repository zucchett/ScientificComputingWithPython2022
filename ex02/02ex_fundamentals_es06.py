x = int(input("please insert a number:"))


def square_of_a_number(x):
    s = x * x
    return s
print("square is : ",square_of_a_number(x))

# ------------------------------------------------------------------
def cube_of_a_number(x):
    c = x * x * x
    return c
print("cube is : ",cube_of_a_number(x))


# -------------------------------------------------------------------
def sixth_power_of_a_number():
    z_1 = square_of_a_number(x) ** 6
    z_2 = cube_of_a_number(x) ** 6
    return z_1,z_2


# -------------------------------------------------------------------
print("sixth power of raised numbers are:",sixth_power_of_a_number())