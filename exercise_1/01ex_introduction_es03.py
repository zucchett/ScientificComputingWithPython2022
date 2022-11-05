import math

try:
    firstPoint = input("Enter first point coordinate as x,y : ")
    secondPoint = input("Enter second point coordinate as x,y : ")
    firstPointTuple = [float(x) for x in firstPoint.split(",")]
    secondPointTuple = [float(x) for x in secondPoint.split(",")]
    distance = str(math.sqrt(math.pow(secondPointTuple[0] - firstPointTuple[0], 2) +
                             math.pow(secondPointTuple[1] - firstPointTuple[1], 2)))
    print("The distance between first and second point is: " + distance)
except Exception as e:
    print("Please enter the x and y coordinates as float in this format: 'x,y'. E.G: '4.5,5'")
    print(e)
