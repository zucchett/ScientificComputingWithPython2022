# 11. Class inheritance
from _02ex_fundamentals10 import polygon as p
# from _02ex_introduction10 import polygon as p 

# Define a class rectangle that inherits from polygon. Modify the constructor,
class rectangle(p):
  def __init__(self,components):
  #Geometrical properties of rectangle
  #it needs a,c and b,d to be same length
    if len(components) == 4 and components[0]==components[2] and components[1]==components[3]:
      self.sides = components
    else: print('You did not complete Geometrical properties of rectangle, you entered:', components)
  
  # Create a method area() that returns the area of the rectangle.
  def area(self):
    return self.sides[0]*self.sides[1]

# Test the rectangle class by creating an instance and passing an appropriate input to the constructor.
rectang = rectangle((4,5,4,5))
print('\n######################################\n')
print('Area for recangle {} is: {}'.format(rectang.get(),rectang.area()))
# print(rectang.area())

print('\nTesting a non Recangular polygon\n')

nonrectang = rectangle((4,5,1,6,2))
