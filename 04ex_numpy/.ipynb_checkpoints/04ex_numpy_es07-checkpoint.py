import numpy as np
mask = np.full((1,99), True)
numbers = np.arange(1,99)
x = 2
while x * 2 < 99:
    if x *2 <= 99:
        mask[0, (x * 2)-1] = False
    if x*3 <=  99:
        mask[0, (x *3)-1] = False
    if x * 5 <=99:
        mask[0, (x*5)-1] = False
    x = x+1
print(numbers)
print(mask)
print(np.shape(numbers))
print(np.shape(mask))
