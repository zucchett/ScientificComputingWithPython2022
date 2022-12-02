import matplotlib.pyplot as plt
import numpy as np
mile=np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
print("in miles:",mile)
SH= np.abs(mile-mile[:, np.newaxis])
print("distances:","\n",SH)
S_H = SH*1.609344
print("distance array in km:","\n" ,S_H.round(2))