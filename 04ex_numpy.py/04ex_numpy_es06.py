import numpy as np
position_mile=np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
print(position_mile)
x=(position_mile[:,np.newaxis])
print(x)
distance=np.abs(position_mile-x)
print(distance)
distance_km=distance*1.609344
print(distance_km.round(3))