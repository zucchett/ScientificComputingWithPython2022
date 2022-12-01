"""
6. Broadcasting
Use broadcasting to create a grid of distances.
Route 66 crosses the following cities in the US: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City,
Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.
The corresponding positions in miles are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448
Build a 2D grid of distances among each city along Route 66
Convert the distances in km
"""
import numpy as np
import matplotlib.pyplot as plt

cities = ["Chicago", "Springfield", "Saint-Louis", "Tulsa", "Oklahoma City", "Amarillo", "Santa Fe", 
"Albuquerque","Flagstaff", "Los Angeles"]
dist = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
a = np.tile(dist, (10, 1)).T
a = abs(a - dist)  # built the matrix

print("\n#######################\n#########-DISTANCES IN MILES-##########\n########################\n")
fig, ax = plt.subplots()  # plot the grid
ax.set_axis_off()
table = plt.table(cellText=a, rowLabels=cities, colLabels=cities, loc='center')
table.scale(10, 10)
table.set_fontsize(32)
plt.show()

a = (a * (np.ones((10, 10)) * 1.60934)).round(decimals=0)  # conversion in km
print("\n#######################################\n"
      "\n##########-DISTANCES IN KM-############\n"
      "\n#######################################\n")
fig, ax = plt.subplots()  # plot the grid
ax.set_axis_off()
table = plt.table(cellText=a, rowLabels=cities, colLabels=cities, loc='center')
table.scale(10, 10)
table.set_fontsize(32)
plt.show()
