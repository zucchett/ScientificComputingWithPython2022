#Zuccolo Giada, matr. 2055702
# EXE 4

starting_value = float(input("Insert a starting value: "))
step_value = float(input("Insert a step value: "))
factor = 0.5
sum = 0

n = 1
while True:
    sum = starting_value + step_value
    if sum == starting_value:
        print("Result:\t", "%2.8e"%step_value)
        break
    else:
        if step_value*factor == 0.0 :
            print("Result:\t", "%2.8e" % step_value)
            break
        else:
            step_value = step_value * factor
print("Note: the value depends on the inputs")
