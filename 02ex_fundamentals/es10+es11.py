class Polygon:
    s=()
    def __init__(self,sides):
        self.s=sides
        if len(self.s)<3:
            print("error, ther should be at least 3 sides")
            return 0
        
    def getSides(self):
        return self.s
    def getSideN(self,n):
        return self.s[n]
    def setX(self, n, si): # n is the component index, and si is the value
        if n < len(self.s):
            self.s[n] = xi
    def perimeter(self):
        peri=0
        for i in range(len(self.s)):
            peri+=self.s[i]
        return peri
    def getOrderedSides(self,order):
          if order==True:
                sorted_ = tuple(sorted(self.s))
          elif  order==False:
                sorted_ = tuple(sorted(self.s,reverse=True))
          else :print("enter true for ascending or flase for descending")
            
          return sorted_
    
class Rectangle(Polygon):
    def __init__(self,sides):
        if len(sides)==4 and sides[0]==sides[0]and sides[1]==sides[3] :
            self.s=sides
        else:print(
            "this not a rectangle, make sure to have 4 sides and each two opposite side are equals")
            
    def Area(self):
        area=self.getSideN(0)*self.getSideN(1)
        return area

poly=Polygon((4,3,2,7))
rec=Rectangle((4,5,4,5))

print(poly.getSides())
print("the length of 4th side of this polygon is ",poly.getSideN(3))
print("the perimeter of this polygon is : ",poly.perimeter())
print("sorted sides are :", poly.getOrderedSides(False))
print("the rectungle is :",rec.getSides())
print("area is ",rec.Area())