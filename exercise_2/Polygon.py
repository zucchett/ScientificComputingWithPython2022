class Polygon:
    sides_lengths = tuple()

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
