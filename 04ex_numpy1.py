import numpy as np
m_1= np.arange(12).reshape((3,4))
print(m_1)
column_mean = np.mean(m_1,axis=0)
row_mean = np.mean(m_1,axis=1)
print("Mean of the columns:",column_mean)
print("Mean of the rows:",row_mean)