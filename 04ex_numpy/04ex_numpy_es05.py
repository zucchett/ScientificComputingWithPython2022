#5. Matrices

import numpy as np

a=np.fromfunction(lambda i,j:(i+1)*(j+1),(10,10),dtype='int')
print('The 10 by 10 multiplication table:\n',a)

print('The trace of the 10 by 10 multiplication table:\n',a.trace())

print('The anti-diagonal matrix of the 10 by 10 multiplication table:\n',np.fliplr(a).diagonal())

print('The diagonal offset by 1 upwards of the 10 by 10 multiplication table:\n',np.diag(a,-1))
