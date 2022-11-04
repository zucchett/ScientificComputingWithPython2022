import sys
print("precision from info: ", sys.float_info.epsilon)
a = 2
EPS = 1
last_eps = EPS
while a > 1:
    last_eps = EPS
    EPS = EPS / 2
    a = EPS + 1

print("Calculated precision: ", last_eps)