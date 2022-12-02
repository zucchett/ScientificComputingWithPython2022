import numpy as np
start = np.linspace(0, 0.9,10)
end = np.linspace(5, 5.9,10)

M = np.linspace(start,end,6)
print(M)

print("\nSet all entries with a decimal part  <0.4  to zero:")
for i in range(0,4):
    M[:,i] = [0]

print(M)