#ex_10

import math

vector = []
sum = 0

vector = [int(item) for item in input("Enters the vectors components separated only by commas : ").split(",")]
print()

for i in range(len(vector)):
    sum = sum + vector[i]**2

norm = math.sqrt(sum)

vector_normalized = [vector[i]/norm for i in range(len(vector)) ]

print("The norm of your vector is: \n", norm)
print()
print("The normalized vector is: ", vector_normalized)
print()

sum2=0
for i in range(len(vector_normalized)):
    sum2 = sum2 + vector_normalized[i]**2

norm2 = math.sqrt(sum2)

print("The norm of this new vector is: ", norm2)
print()



