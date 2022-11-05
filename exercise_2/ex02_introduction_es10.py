from Polygon import Polygon

# The Polygon class has been defined in a separate module, so it can be used in exercise number 10 and 11
triangle = Polygon((3, 4, 5))
print("The perimeter of the triangle is: ", triangle.perimeter())
print("The sides length of the triangle are ", triangle.getOrderedSides(True))

irregularShape = Polygon((4, 2, 1, 3, 6))
print("The perimeter of the shape is: ", irregularShape.perimeter())
print("The sides length of the shape are ", irregularShape.getOrderedSides(False))
