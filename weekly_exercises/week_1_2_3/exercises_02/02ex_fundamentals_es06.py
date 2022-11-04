#Zuccolo Giada, matr. 2055702
# EXE 6
def th6(n):
    def cube(n):
        return n * n * n

    def square(n):
        return n * n

    print(square(n))
    print(cube(n))
    return cube(square(n))

print(th6(2))