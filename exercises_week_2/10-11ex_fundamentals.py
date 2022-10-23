#10. Class definition

class Polygon:
    
        def __init__(self, sides): #Initialization of the object of the class Polygon
            if len(sides)<3:
                 print("Not enough sides for a polygon!")
            else:
             self.sides = sides
        
        def setSide(self,xi): #set the length of one side
            newSide = (xi)
            self.sides = self.sides + newSide
            
        def getSide(self,n): #get the length of one side
            return self.sides[n]
        
        def getList(self):
            return self.sides
            
        def perimeter(self): #calculates the perimeter of the poligon
            sum = 0
            for i in range(len(self.sides)):
                sum += self.sides[i] 
            return sum
        
        def getOrderedSides(self,increasing = True or False):
            list = []
            for i in range(len(self.sides)):
                list.append(self.sides[i])
            if increasing == True:
                list.sort()
                return (list)
            else:
                list.sort(reverse= True)
                return (list)
                    
            
            
#Create an istance of the class Polygon
sides = (2,3,4)
x = Polygon(sides)
p1 = x.perimeter() #calculates the perimeter

a = x.getSide(len(sides)-1) #gets the side at the last position, should be 6
p2 = x.perimeter() #calculates the perimeter of the new poligon

y=x.getOrderedSides(increasing = True) #sort the list of the sides in ascendant order
z=x.getOrderedSides(increasing = False) #sort the list in descndent order


print(f"The perimeter is {p1}")
print(f"The last side of the polion is {a}")
print(f"Now the perimeter is {p2}")
print(f"Sides in ascendant order: {y}")
print(f"Sides in descendant order: {z}")

#11. Class inheritance
class Rectangle(Polygon):
    
    def __init__(self, sides): #Initialization of the object of the class Polygon
            self.sides = sides
    
    def area(self):
        if len(self.sides)>2:
            return
        else:
            a = self.sides[0]
            b = self.sides[1]
            return a*b
    
sides = (5,6)    
rectangle = Rectangle(sides)
a = rectangle.area()
if a == None:
    print("Not a rectangle")
else:
    print(f"The area of the rectangle is {a}")
        
        