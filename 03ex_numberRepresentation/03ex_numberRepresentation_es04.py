#Machine precision

x = x_temp = 1
j = 1
while True :
    x_temp += j
    if x_temp == x :
        break
    else :
        x_temp = x
        j /= 2
print("precision for floating point numbers:",j)