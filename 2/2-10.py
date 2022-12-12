class polygon:
    sides = None
    def __init__(self, sides:tuple):
        if len(sides) < 3:
            print('Sides should contain at least 3 items.')
        self.sides = sides

    def get_sides(self) -> tuple:
        return self.sides

    def set_sides(self, sides:tuple):
            if len(sides) < 3:
                print('Sides should contain at least 3 items.')
            self.sides = sides     

    def perimeter(self):
        sum = 0
        for item in self.sides:
            sum += item
        return sum    

    def get_ordered_sides(self, increasing):
        return sorted(self.sides, reverse=not increasing)
        

triangle = polygon((3, 4, 5))
print(triangle.get_sides())
triangle.set_sides((8, 6, 10))
print(triangle.get_sides())
print(triangle.perimeter())
print(triangle.get_ordered_sides(False))

