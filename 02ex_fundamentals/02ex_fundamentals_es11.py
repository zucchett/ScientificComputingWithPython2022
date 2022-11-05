class polygon:
    def __init__(self, shape):
        self.shape = shape

    def change_length(self,index,leng):
        self.shape = list(self.shape)
        self.shape[index] = leng
        self.shape = tuple(self.shape)
        return self.shape
    
    def perimeter(self):
        return sum(self.shape)
    
    def getOrderedSides(self, increasing=True):
        self.sorted = tuple(sorted(self.shape, reverse=not increasing))
        return self.sorted

class rectangle(polygon):
    def __init__(self, shape):
        super().__init__(shape)
    
    def area(self):
        area = self.getOrderedSides()  # The values are being ordered according to their sizes
        return area[0] * area[2]       # To grab each side 0-2 indexes are being selected (1-3/1-2/0-3 could be chosen as well)
        

rectangle = rectangle((3,4,3,4))                    # Instantiating the rectangle class by creating the object
print(rectangle.perimeter())                        # Perimeter of the rectangle has been calculated
print(rectangle.getOrderedSides(increasing=False))  # Ordered the rectangle 
print(rectangle.area())                             # Area of the rectangle has been calculated