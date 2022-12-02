import numpy as np
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
print("Answer use outer:\n", np.outer(u,v))
print("\nAnswer using for loop:\n", np.array([x*y for x in u for y in v]).reshape(4,4))
print("\nAnswer using Broadcasting:\n", np.tile(u,(4,1)).T * v)
