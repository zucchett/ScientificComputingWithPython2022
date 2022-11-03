import numpy as np
fibo = np.array([0,1])
while(len(fibo) < 20):
    last_pair = fibo[-2:]
    fibo = np.append(fibo, sum(last_pair))
    print(fibo)


