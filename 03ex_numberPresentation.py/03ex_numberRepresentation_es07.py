# 7. Integral of a semicircle

import math


def calculateRiemann(N):
    result = 0
    y = 2 / N
    for i in range(N + 1):
        x = (y * i) - 1
        result = result + math.sqrt(1 - x ** 2) * y
    return result


print(calculateRiemann(100))
