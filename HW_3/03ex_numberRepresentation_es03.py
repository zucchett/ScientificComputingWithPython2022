import sys

print(sys.float_info)
print(sys.float_info.max)
print(sys.float_info.min)
under_flow = 1
over_flow = 1

maximum = 1050  # since max is given as 1024 , lets give 1050
for i in range(maximum):  # since max is given as 1024
    under_flow = under_flow / 2
    over_flow = over_flow * 2
    print(i, "underflow is:", '%1e' % under_flow, "overflow is:", '%1e' % over_flow)

# i got underflow as = 1.112537e-308 and overflow as = 8.988466e+307
