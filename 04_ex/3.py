import numpy as np
start = np.linspace(0, 0.9,10)
end = np.linspace(5, 5.9,10)

A = np.linspace(start,end,6)
print(A)

print("\n ")
for i in range(0,4):
    A[:,i] = [0]

print(A)