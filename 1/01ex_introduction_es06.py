# Casting

x = input("Enter the first variable: ")
y = input("Enter the second variable: ")

try: 
    res = float(x) + float(y)
    print("Result as float: " + str(res))
    print("Result as integer: " + str(int(res)))

except:
    print("You didn't enter a number...")
    print("Do you mean " + str(x) + str(y) + "?")
