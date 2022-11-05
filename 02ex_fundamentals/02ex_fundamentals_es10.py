class polygon:
    def _init_(self, list):
        self.list = list
        self.lene = len(list)
        if self.lene < 3:
            print("enter more than 3")
            return

    def perimeter(self):
        perimeter = sum(self.list)
        # print("first solv: ",self.list[0] * self.lene)
        print("sum: ", perimeter)

    def getOrderedSides(self, increasing=True):
        print(sorted(self.list))


x = polygon((3, 6, 7, 1))
x.perimeter()
x.getOrderedSides()