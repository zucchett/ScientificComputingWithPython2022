"""
10. Normalization of a N-dimensional vector
Write a program that takes an N-dimensional vector, e.g. a variable-length tuple of numbers,
and normalizes it to one (in such a way that the squared sum of all the entries is equal to 1).
"""

def normalizes(var):
    squ = [i / sum(var) for i in var]
    print(squ)
    return squ


demo_tuple = (2, 4.5, 5, 7)
normalizes(demo_tuple)
