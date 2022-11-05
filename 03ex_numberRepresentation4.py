a2 = 1.0
b2 = 1.0
k2 = 0
while True:
    addition = 10**(-k2)
    print(k2, b2+addition)
    if a2 == b2+addition:
        print(f"Result: Addition has no effect on the number when it is 1e-{k2} or smaller")
        break
    k2 += 1
    