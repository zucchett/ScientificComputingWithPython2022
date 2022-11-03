def sixth_power(n):
    def square(n):
        return n*n
    def cube(n):
        return n*n*n
    return square(cube(n))