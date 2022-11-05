class polygon:
    x = ()

    def __init__(self, components):
        if len(components) < 3:
            raise Exception()

        self.x = components
        print("The polygon is: ", components)

    def perimeter(self):
        return sum(self.x)

    def getOrderedSides(self, increasing = True):
        alist = []
        for i in range(len(self.x)):
            alist.append(self.x[i])
        if increasing:
            alist.sort()
            return alist
        else:
            alist.sort(reverse = True)
            return alist


a = polygon((12,4,8))
print("The perimeter of polygon is: ", a.perimeter())
print("The ordered sides of polygon are: ", a.getOrderedSides(increasing=True))
