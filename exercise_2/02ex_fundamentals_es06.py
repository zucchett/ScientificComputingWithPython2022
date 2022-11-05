x = 4
def square_x(x):
    square = x*x
    return square

def cube_x(x):
    cube = x*x*x
    return cube

def power6th_x(square,cube):
    first_z = square_x() ** 6
    second_z = cube_x() ** 6
    return first_z , second_z