import sys
print("info precision : ", sys.float_info.epsilon)
eps = 1
a = 2
last_eps = eps
while a > 1:
    last_eps = eps
    eps = eps / 2
    a = eps + 1

print("precision: ", last_eps)