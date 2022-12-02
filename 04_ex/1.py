import numpy as np
A= np.arange(12).reshape((3,4))
print(A)
column_mean = np.mean(A,axis=0)
row_mean = np.mean(A,axis=1)
print("rows Mean is:",row_mean)
print("columns Mean is:",column_mean)
