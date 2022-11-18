#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
import numpy as np

u = np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
v = np.array([0,198,303,736,871,1175,1475,1544,1913,2448])
miles = np.array([[np.abs(u[i]-v[j]) for i in range(10)] for j in range(10)])
print("The grid of distances in miles is: \n",miles)
print()
km = np.array(miles/1.6)
print("The grid of distances in km is: \n",km)
