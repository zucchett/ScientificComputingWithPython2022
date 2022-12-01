#6. Broadcasting

import numpy as np

distances=np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
m=len(distances)
a=np.tile(distances,(m,1)).T
grid_mile=abs(a-distances)
print('The 2D grid of distances among each city along Route 66 in mile:\n',grid_mile,'\n')

grid_km=grid_mile*1.609344
print('The 2D grid of distances among each city along Route 66 in km\n',grid_km)
