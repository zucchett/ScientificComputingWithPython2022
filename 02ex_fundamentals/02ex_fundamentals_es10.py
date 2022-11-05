
# 10. Class definition

# Define a class polygon. The constructor has to take a tuple as input that contains the length of each side. The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.

# Create appropriate methods to get and set the length of each side

# Create a method perimeter() that returns the perimeter of the polygon

# Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged in increasing or decreasing order, depending on the argument of the method

# Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.

# -------------------------------------- Code Begin-------------------------------------

class polygon:
    sides = []
    
    def __init__(self,sides):
        self.sides = sides
        
    def getSide(self, n): # n is the side index
        return self.sides[n]
    
    def setSide(self, n, x): # n is the side index, and x is the value
        if n < len(self.sides) and x != 0 : # you can't set a side with a Zero value
            self.sides[n] = x
    def perimeter(self):
        return sum(self.sides)
    def getOrderedSides(self, increasing = True):
        aux = self.sides
        aux.sort(reverse=increasing)
        return aux

# Create an instance of class 'polygon'
a = polygon([5, 6, 1, 6, 8])

print("Get the value of the 4th side:", a.getSide(4)) 

a.setSide(3, 7) # set the third side to 7

print("Perimeter:", a.perimeter())
print("The length of the sides arranged:", a.getOrderedSides(increasing = True))

# -------------------------------------- Code End -------------------------------------
