import numpy as np

vector = (5,10,5,20)

extra =vector/np.linalg.norm(vector)
print(extra) # Normalized versions of the vector

checking = np.sqrt(sum([ex**2 for ex in extra]))
print(checking) # Making sure that the squared sum of all entries is equal to 1
