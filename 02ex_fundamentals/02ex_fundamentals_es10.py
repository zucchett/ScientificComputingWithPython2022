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



triangle = polygon((4, 5, 6, 3))                     # Instantiating the class by creating the object
print(triangle.getOrderedSides())                    # Ordered the length of the sides in increasing order
print(triangle.change_length(1,10))                  # Number 1o selected and inserted to the second side part
print(triangle.change_length(0,8))                   # Number 8 selected and inserted to the first side part 
print(triangle.shape)                                # Tuple were checked 
print(triangle.getOrderedSides(increasing=True))     # Ordered the length of the sides in increasing order
print(triangle.getOrderedSides(increasing=False))    # Ordered the length of the sides in decreasing order