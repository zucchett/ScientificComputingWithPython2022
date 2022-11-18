#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np
m = np.arange(12).reshape((3,4))
print(m)
print("The mean of the total array is: ",np.mean(m))
print()
for i in range(3):
    print("The mean of the row", i+1, "is: ",np.mean(m[i]))
print()
for i in range(4):
    print("The mean of the column", i+1, "is: ",np.mean(m[:,i]))

