# ex_11
 
# class inheritance

import math

class Polygon:

  
    sides = [] 

    
    def __init__(self, tuple_sides):
        if len(tuple_sides) < 3:
            print("It is not a polygon! We need at least 3 sides!")
        else:
            for i in range(len(tuple_sides)):
                self.sides.append(tuple_sides[i])
            print("Polygon created!")

   
    def __del__(self):
        print("Goodbye, exercise done!")

    # Definition of the methods

    
    def getSideN(self, n): 
        return self.sides[n-1]
    
        # set the length of each side
    def setSideN(self, n_length, n): 
        if n <= len(self.sides):
            self.sides[n-1] = n_length
  
    def perimeter(self):
        sum = 0
        for s in self.sides:
            sum += s
        return sum

    # sides of the Polygon ordered 
    def getOrderedSides(self, increasing = True):
        if increasing == True:
            p_copy = [i for i in self.sides]
            p_copy.sort()
            tuple_poly = tuple(p_copy)
            return tuple_poly
        else:
            p_copy = [i for i in self.sides]
            p_copy.sort(reverse=True)
            return tuple(p_copy)


class Rectangle(Polygon): # class 'Rectangle' inherits from class 'Polygon'

    
    def __init__(self, two_sides):
        if len(two_sides) == 2:
            for i in range(len(two_sides)):
                self.sides.append(two_sides[i]) # a tuple is expected as input
        else:
            print("Error: number of sides is not 2, so it is not a rectangle!")

    
    def area(self):
        return self.sides[0]*self.sides[1]

    def perimeter(self):
        sum = 0
        for s in self.sides:
            sum += s
        return sum*2
    
r = Rectangle((6,7))



print("The area of the rectangle is " + str(r.area()))

r.setSideN(4,1)

print("After changing the dimension of the 1-nd side now the sides (with decreasing order) are: " + str(r.getOrderedSides(increasing='False')))

print("The ordered sides are " + str(r.getOrderedSides()))

print("Perimeter is: " + str(r.perimeter()))




