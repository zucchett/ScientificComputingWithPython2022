class polygon :
    def __init__(self,sides_tuple) :
        self.sides_tuple = sides_tuple
    def demonstrat(self):
        print(f' the length of size are : {self.sides_tuple}')
    def perimeter(self):
        print(f'the perimeter of this polygon is : {sum(self.sides_tuple)}')
    def getOrderedSides(self):
        print(f'the sorted tuple of sides is : {tuple(sorted(self.sides_tuple))}')
a = polygon((4,3,2,1))
a.demonstrat()
a.perimeter()
a.getOrderedSides()