import numpy as np
import matplotlib.pyplot as plt
mile=np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
print("in miles:",mile)
dis= np.abs(mile-mile[:, np.newaxis])
print("distances:","\n",dis)
d_km = dis*1.609344
print("distance array in km:","\n" ,d_km)