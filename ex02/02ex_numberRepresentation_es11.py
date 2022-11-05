class rectangle(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 4)

    def Area(self):
        x = self.sides
        
        area =  x[0]*x[1]
        print('The area of the rectangle is :', area)

        
rec = rectangle()
rec.Area()
