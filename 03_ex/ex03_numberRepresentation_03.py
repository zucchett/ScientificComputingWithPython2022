import math #it is madatory
i = 1.0 #pre requisitive
while True:
    last_i = i
    i = i * 2
    if math.isinf(i):
        print("limit of overflow is: ", last_i)
        break


i = 1.0 #pre requisitive
while True:
    last_i = i
    i = i / 2
    if i == 0:
        print("The limit of underflow: ", last_i)
        break