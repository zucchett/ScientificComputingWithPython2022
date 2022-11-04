#Exercise 10
class polygon():
  sides = ()
  def __init__(self,components):
    if len(components) >= 3:
      self.sides = components
    else : 
      print("Please write at least 3 sides")
  def get(self):
    return self.sides

  def getX(self, n):
      return self.sides[n]

  def setX(self, n, i): 
      if n < len(self.sides):
          temp=list(self.sides)
          temp[n]= i
          self.sides = tuple(temp)

  def perimeter(self):
    sum = 0
    for side in self.sides:
      sum +=side
    return sum

  def getOrderedSides(self,increasing = True):
    temp = list(self.sides)
    temp.sort(reverse=not(increasing))
    return temp

test = polygon((5,1,7,12,6,4))

print("Perimeter --->",test.perimeter())
print("Sorted sides --->", test.getOrderedSides(increasing = True))

#Exercise 11

class rectangle(polygon):
  def __init__(self,components):
    if len(components) == 4 and components[0]==components[2] and components[1]==components[3]:
      self.sides = components
    else: 
      print("Please write a proper rectangle:")
  def area(self):
    return self.sides[0]*self.sides[1]
    
rectang = rectangle((7,9,7,9))
print("_____________________________________\n")
print("Area for recangle {} is: {}".format(rectang.get(),rectang.area()))
