import numpy as np

distances = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
d1 = np.absolute(distances[:,np.newaxis] - distances)
print(d1)
print(d1*1.60934)