import numpy as np

a = np.linspace(1,10,10, dtype = int)
b = a[:,np.newaxis] * a
print(b, '\n')

m, n = b.shape
diag1 = np.zeros(m, dtype = int)
diag2 = np.zeros(m, dtype = int)

anti_diag1 = np.zeros(m, dtype = int)
anti_diag2 = np.zeros(m, dtype = int)


print(np.where(b == 4)[0].tolist())
print(np.where(b == 4)[1].tolist())

# with numpy functions
diag1 = np.diag(b)
anti_diag1 = np.fliplr(b).diagonal()

# with for loop
for i in range(m):
    diag2[i] = b[i][i]
    anti_diag2[i] = b[i][n-1-i]
print(np.diag(b))
print(anti_diag2)

print("trace is :", np.sum(diag1))
d_offset = diag + a
print(d_offset)

