# 3. Underflow and overflow

import math

underflow = 1
for i in range(1200):
    x = underflow / 2
    if x == 0:
        print("Underflow: ", underflow)
        break
    else:
        underflow = x

overflow = 1.0
for i in range(10000):
    x = overflow * 2
    if x == math.inf:
        print("Overflow: ", overflow)
        break
    else:
        overflow = x