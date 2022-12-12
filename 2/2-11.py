import math

class polygon:
    sides = None
    def __init__(self, sides:tuple):
        if len(sides) < 3:
            raise Exception('Sides should contain at least 3 items.')
        self.sides = sides

    def get_sides(self):
        return self.sides

    def set_sides(self, sides:tuple):
            if len(sides) < 3:
                raise Exception('Sides should contain at least 3 items.')
            self.sides = sides     

    def perimeter(self):
        sum = 0
        for item in self.sides:
            sum += item
        return sum    

    def get_ordered_sides(self, increasing):
        return sorted(self.sides, reverse=not increasing)

class rectangle(polygon):
    def init(self, sides: tuple):
        super().init(sides)

    def area(self):
        return self.sides[0] + self.sides[1] + self.sides[2] + self.sides[3]


r = rectangle((1, 1, 2, 2))
print(r.area())