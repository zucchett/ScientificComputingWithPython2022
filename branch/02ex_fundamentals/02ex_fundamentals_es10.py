#ex_10

# class definition

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

# End of the class definition

p = Polygon((5,4,2))

print("The dimension of the 2-nd side is ", str(p.getSideN(2)))

print("Perimeter is: " + str(p.perimeter()))

p.setSideN(6,3)

print("After changing the dimension of the 3-rd side now the sides (with decreasing order) are: " + str(p.getOrderedSides(increasing='False')))

p.setSideN(9,1)

print("After changing the dimension of the 1-st side now the sides (with increasing order) are: " + str(p.getOrderedSides()))


