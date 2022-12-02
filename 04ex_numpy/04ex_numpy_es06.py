import numpy as np
import pandas as pd
x1 =  np.array([[0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448]])
labels = ['Chicago', 'Springfield', 'Saint-Louis', 'Tulsa', 'Oklahoma City', 'Amarillo', 'Santa Fe', 'Albuquerque', 'Flagstaff', 'Los Angeles']
x2 = x1.T

ans = abs(x1-x2)
ans = pd.DataFrame(ans, index =labels, columns = labels)
print("These are distances:\n", ans)
# Each Mile is 1.6 kilometre so I multiplied matrix by 1.6 to convert the unit
print("\nThis is distances in Km:\n", ans*1.6)
