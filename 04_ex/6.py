import numpy as np
import matplotlib.pyplot as plt
Mile=np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
print("\n in Miles:\n",Mile)
Distance= np.abs(Mile-Mile[:, np.newaxis])
print("\n Distances:","\n",Distance)
d_km = Distance*1.609344
print("\n Distance array in km:","\n" ,d_km)