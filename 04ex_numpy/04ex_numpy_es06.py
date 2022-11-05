# 6. Broadcasting

# Use broadcasting to create a grid of distances.

# Route 66 crosses the following cities in the US: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff, Los Angeles.

# The corresponding positions in miles are: 0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448

# Build a 2D grid of distances among each city along Route 66
# Convert the distances in km

# -------------------------------------- Code Begin-------------------------------------
import numpy as np

milesstones  = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])

distanceMiles = np.abs(milesstones  - milesstones[:, np.newaxis])
distanceKm = distanceMiles * 1.60934 

print('2D grid of distances among each city along Route 66 : \n',distanceMiles )
print('\n ------------------------------------------- \n')
print('2D grid of distances in Km : \n ',distanceKm  )


# -------------------------------------- Code End---------------------------------------
