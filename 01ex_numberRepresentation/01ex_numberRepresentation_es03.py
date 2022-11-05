''' Created by Pedram on 10/19/2022 AD. '''

import math

# Calculate the Distance
def findDistance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)** 2 + (y1 - y2)** 2)

# Delete Extra '(', ')', 'White Space' 
def extractNumbers(text):
    text = str(text).replace(" ","")
    text = str(text).replace("(","")
    text = str(text).replace(")","")
    return text

# Input Two Points
firstPoint = input('Input First Point like (0, 3) =?\n')
secondPoint = input('Input First Point like (4, 0) =?\n')

# Check the Input Formation
x1 = extractNumbers(firstPoint.split(",")[0])
y1 = extractNumbers(firstPoint.split(",")[1])
x2 = extractNumbers(secondPoint.split(",")[0])
y2 = extractNumbers(secondPoint.split(",")[1])

print("distance= ", findDistance(int(x1), int(x2), int(y1), int(y2)))