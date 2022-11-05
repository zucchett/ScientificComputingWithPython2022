# Computing the distance

import math

values1 = input("Input x and y coordinates of the first point by separating comma (,) : ")
list1 = values1.split(",")
point1 = tuple(list1)
values2 = input("Input x and y coordinates of the second point by separating comma (,) : ")
list2 = values2.split(",")
point2 = tuple(list2)

euclidean_distance = math.sqrt(math.pow(int(list1[0])-int(list2[0]), 2) + math.pow(int(list1[1])-int(list2[1]), 2))
print("Euclidean distance: " + str(euclidean_distance))

