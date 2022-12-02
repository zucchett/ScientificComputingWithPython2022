import numpy as np
m= np.arange(12).reshape((3,4))
print("Total is:" , m.mean())
column_definition = np.mean(m,axis=0)
row_definition    = np.mean(m,axis=1)
print(" the columns is:",column_definition)
print("the rows is:",row_definition)