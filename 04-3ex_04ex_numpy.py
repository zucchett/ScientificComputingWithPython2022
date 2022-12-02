import numpy.random as npr
random = 3 * npr.random_sample((10, 6)) - 0
print("10 by 6 matrix of float random numbers: ")
print(random)
arr = np.array(random)
mask = (random < 0.3)
print("Mask: \n", mask)
random[random < 0.3] = 0
print("\n All entries smaller than 3 set to zero : ")
print(random)