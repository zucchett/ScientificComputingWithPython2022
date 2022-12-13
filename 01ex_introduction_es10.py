import numpy 
from sklearn.preprocessing import normalize

x = np.random.rand(1000)*10
norm1 = x / numpy.linalg.norm(x)
norm2 = normalize(x[:,np.newaxis], axis=0).ravel()
print (np.all(norm1 == norm2))
