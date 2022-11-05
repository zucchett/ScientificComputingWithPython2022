

class polygon:
    def __init__(self , tup) -> None:
        self.tup = tup
        self.len = len(tup)
    
    def perimeter(self):
        p = self.tup[1] * self.len
        print(p)

    def getOrderedSides(self , increasing = True):
        print(sorted(self.tup))


class rectangle(polygon):
    def __init__(self, tup):
        self.tup = tup
        self.len = len(tup)
        # super().__init__(tup)
    def area(self):
        p = self.tup[1] * self.len
        print(p)
    
      
    
    # def area(self):
       

   
d = rectangle(tup=(0,1,2,1))
d.area()
