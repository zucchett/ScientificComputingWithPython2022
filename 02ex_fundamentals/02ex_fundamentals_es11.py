class polygon :
    def __init__(self,sides_tuple) :
        self.sides_tuple = sides_tuple
    def demonstrat(self):
        print(f' the length of size are : {self.sides_tuple}')
    def perimeter(self):
        print(f'the perimeter of this polygon is : {sum(self.sides_tuple)}')
    def getOrderedSides(self):
        print(f'the sorted tuple of sides is : {tuple(sorted(self.sides_tuple))}')

class rectangle(polygon):
    def __init__(self, sides_tuple):
        self.sides_tuple = sides_tuple
    def area(self):
        sorted_sides = sorted(self.sides_tuple)
        print(f'the area of rectangle is {sorted_sides[0] * sorted_sides[2]}')

example = rectangle((3,1,3,1))
print(example.area())