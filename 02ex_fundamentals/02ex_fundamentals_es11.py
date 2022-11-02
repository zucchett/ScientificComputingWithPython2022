
# 11. Class inheritance

# Define a class rectangle that inherits from polygon. Modify the constructor, if necessary, to make sure that the input data is consistent with the geometrical properties of a rectangle.

# Create a method area() that returns the area of the rectangle.
# Test the rectangle class by creating an instance and passing an appropriate input to the constructor.

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

class rectangle(polygon):
    def __init__(self, sides):
        if (len(sides) == 4) and (sides[0] == sides[2]) and (sides[1] == sides[3]):
            self.sides = sides # a list is expected as input
        else:
            print("Error: This sides can't make a rectangle")
    def area(self):
        return self.sides[0] * self.sides[1]
    


# Create an instance of class 'rectangle'
a = rectangle([2, 6, 2, 6])

print("Get the value of the 3rd side:", a.getSide(3)) 
print("Perimeter:", a.perimeter())
print("Area:", a.area())
print("The length of the sides arranged:", a.getOrderedSides(increasing = True))

# -------------------------------------- Code End -------------------------------------
