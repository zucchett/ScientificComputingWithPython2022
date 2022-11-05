def square(x: float) -> float:
    return x * x

def cube(x: float) -> float:
    return x * x * x

def main():
    x = float(input("Please enter any number:2"))
    print("User entered number {}".format(x))

    x1 = square(x)
    print("Square of {} is {}".format(x, x1))
    
    x2 = cube(x)
    print("Cube of {} is {}".format(x, x2))
   
    # x to the 6th    
    x3 = cube(square(x))
    print("{} to the 6th is {}".format(x, x3))
   
    return x3

print("Program running :) !") 
main()


