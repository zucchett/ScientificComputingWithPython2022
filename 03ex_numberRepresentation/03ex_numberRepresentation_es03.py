from math import inf

n_overflow = 1
n_underflow = 1

while True:
    n_overflow = float(n_overflow*2)
    if float(n_overflow*2) == inf:
        print("Overflow reached at: ", n_overflow)
        break



while True: 
    n_underflow = float(n_underflow/2)
    if float(n_underflow/2)==0.0:
        print("Underflow reached at: ", n_underflow)
        break


