

class polygon:
    def __init__(self , tuple) -> None:
        self.tuple = tuple
        self.lenle = len(tuple)
    
    def perimeter(self):
        p = self.tuple[1] * self.len
        print(p)

    def getOrderedSides(self , increasing = True):
        print(sorted(self.tuple))


class rectangle(polygon):
    def __init__(self, tuple):
        self.tuple = tuple
        self.len = len(tuple)

    def area(self):
        p = self.tuple[1] * self.len
        print(p)
    
      
    
    # def area(self):
       

   
x = rectangle(tuple=(2,1,2,1))
x.area()
