#6. Nested functions

num = int(input("Enter your number: "))

def square(x):
    return x*x

def cube(x):
    return x**3

def six_power(x):
    return square(cube(x))

print(f"The 6th power of {num} is {six_power(num)}")