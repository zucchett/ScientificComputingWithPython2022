import math
class polygon:    
    x = tuple()
    
    def __init__(self, components):
        self.x = components
        print(components) 
   
    def perimeter(self):
        s2=0
        for i in range(len(self.x)):
            s2 += self.x[i] 
        return (s2)
    
    def getorderedSides(self,increasing = True):
        list_1 = []
        for i in range(len(self.x)):
            list_1.append(self.x[i])
        list_1.sort()
        return (list_1)

class rectangle(polygon):
    def __init__(self, components):
        if len(components) == 4:
            self.x = components
        else:
            print("Error: This is not rectangle!!!")
    def area(self):
        return (max(self.x) * min(self.x))




a = rectangle((7,5,7,5))

print("The area is : " , a.area())  