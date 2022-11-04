''' Created by Pedram on 10/23/2022 AD. '''

import math

def printNormalizedVector(normalizeVector):
    total2 = 0.0
    temp = str(normalizeVector) + " --> "
    for index in range(len(normalizeVector)):
        if (index != len(normalizeVector)-1):
            temp += "{}\u00b2 + ".format(normalizeVector[index])
        else:
            temp += "{}\u00b2 =\n".format(normalizeVector[index])

    for index in range(len(normalizeVector)):
        if (index != len(normalizeVector)-1):
            temp += str(normalizeVector[index] ** 2) + " + "
        else:
            temp += str(normalizeVector[index] ** 2) + " = "

    for index in range(len(normalizeVector)):
        total2 += float(normalizeVector[index] ** 2)
        
    temp += str(total2)
    print(temp)
        


def normalize(vector):
    total =0.0
    for x in vector:
        total += x**2
    temp = math.sqrt(total)
    normalizeVector = [v/temp for v in vector]
    printNormalizedVector(normalizeVector)

dimension = int(input('Input Dimension =?\n'))
vector = [float(input()) for x in range(0, dimension)]
normalize(vector)