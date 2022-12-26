# 10. Class definition

# Define a class polygon. The constructor has to take a tuple as input that contains the length of each side.
class polygon():
  sides = ()

# The (unordered) input list does not have to have a fixed length, but should contain at least 3 items.
  def __init__(self,components):
    if len(components) >= 3:
      self.sides = components
    else : print('You entered a non polygon')

  def __del__(self):
      print('GoodBye')
  def get(self):
    return self.sides
# Create appropriate methods to get and set the length of each side
  def getX(self, n): # n is the component index
      return self.sides[n]
  
  # This method allows to set individial elements of the 'x' attribute 
  def setX(self, n, xi): # n is the component index, and xi is the value
      if n < len(self.sides):
          tmp=list(self.sides)
          tmp[n]= xi
          self.sides = tuple(tmp)

# Create a method perimeter() that returns the perimeter of the polygon
  def perimeter(self):
    sum = 0
    for side in self.sides:
      sum +=side
    return sum

# Create a method getOrderedSides(increasing = True) that returns a tuple containing the length of the sides arranged
#  in increasing or decreasing order, depending on the argument of the method
  def getOrderedSides(self,increasing = True):
    tmp = list(self.sides)
    tmp.sort(reverse=not(increasing))
    return tmp

# Test the class by creating an instance and calling the perimeter() and getOrderedSides(increasing = True) methods.

##Uncomment to check for non polygons
# two_side = polygon((5,2))

five_side = polygon((5,6,7,12,2))

print('Perimeter of the polygon you entered is:',five_side.perimeter())
print('Sorted sides of the polygon:', five_side.getOrderedSides(increasing = True))
# trekendeshi = polygon((4,5,6))
# print(trekendeshi.getX(2))
# trekendeshi.setX(2,8)
# print(trekendeshi.getX(2))
