class Polygon: # The Polygon class module
    def __init__(self, sides_lengths_arg):
        if len(sides_lengths_arg) >= 3:
            self.sides_lengths = sides_lengths_arg
        else:
            print("A polygon can not have les than two sides! Please pass a tuple with at least 3 numbers as sides of "
                  "polygon")

    def get_the_side_length(self, side):
        return self.sides_lengths[side]

    def set_the_side_length(self, side, length):
        self.sides_lengths[side] = length

    def perimeter(self):
        return sum(self.sides_lengths)

    def getOrderedSides(self, increasing=True):
        return sorted(self.sides_lengths, reverse=not increasing)




class Rectangle(Polygon):

    # Since a rectangle has 4 equal sides, we just need the size of one side
    def __init__(self, sides_lengths_arg):
        if len(sides_lengths_arg) == 4:
            self.sides_lengths = sides_lengths_arg
        else:
            print("please enter a tuple with 4 size")
        super().__init__(self.sides_lengths)

    def area(self):
        return self.sides_lengths[0] ** 2


sideSize = (3,3,3,3)
rectangle = Rectangle(sideSize)
area = rectangle.area()
print("The area of rectangle with side size of ", sideSize[0], " is ", area)
