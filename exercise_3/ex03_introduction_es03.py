import math

i = 1.0
while True:
    last_i = i
    i = i * 2
    if math.isinf(i):
        print("The overflow limit is: ", last_i)
        break


i = 1.0
while True:
    last_i = i
    i = i / 2
    if i == 0:
        print("The underflow limit is: ", last_i)
        break
