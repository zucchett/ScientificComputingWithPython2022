class Polygon: # The Polygon class module
    def __init__(self, sides_lengths_arg):
        if len(sides_lengths_arg) >= 3:
            self.sides_lengths = sides_lengths_arg
        else:
            print(" Please add a tuple with at least 3 sides")

    def get_the_side_length(self, side):
        return self.sides_lengths[side]

    def set_the_side_length(self, side, length):
        self.sides_lengths[side] = length

    def perimeter(self):
        return sum(self.sides_lengths)

    def getOrderedSides(self, increasing=True):
        return sorted(self.sides_lengths, reverse=not increasing)


triangle = Polygon((3, 4, 5))
print("The triangle perimeter : ", triangle.perimeter())
print("The triangle sides length : ", triangle.getOrderedSides(True))

irregularShape = Polygon((4, 2, 1, 3, 6))
print("The shape perimeter: ", irregularShape.perimeter())
print("The shape sides length: ", irregularShape.getOrderedSides(False))