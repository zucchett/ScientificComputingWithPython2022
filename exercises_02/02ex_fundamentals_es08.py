#Zuccolo Giada, matr. 2055702
# EXE 8

def fibonacci_recursive(r):
    def fibonacci_sequence(n):
        if n <= 1:
            return n
        else:
            return (fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2))

    for i in range(r):
        print(fibonacci_sequence(i))


r = 20
fibonacci_recursive(r)