# 10. Normalization of a N-dimensional vector

# Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers, and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).

#  !!!! An  explanation is provided in the notebook 01ex_introduction_solved.ipynb
from math import sqrt
def normalizer(v):
    u = list(v)
    w = sqrt(sum([i**2 for i in u ]))
    return tuple([i/w for i in u])

v = (5,6,3,9,6)
norm = normalizer(v)
sum_norm = sum([i**2 for i in norm ])
print('v normalized : {}'.format(norm))
print('The squared sum of the normalized v : {}'.format(round(sum_norm,1)))
