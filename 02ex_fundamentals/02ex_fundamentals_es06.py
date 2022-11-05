n = int(input("Enter a number: "))


def square():
    return n**2
def cube():
    return n**3
def power_6():
    return square() * cube()
    
print("Square of", n, "is", square())
print("Cube of", n, "is", cube())
print("6th power of", n, "is", power_6())