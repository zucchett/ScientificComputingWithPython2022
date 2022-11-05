lengths = (2, 5, 3, 12)

class polygon:
    def __init__ (self, lengths):
        self.l = lengths
        if len(self.l) < 3:
            raise ValueError("The number of dimensions is less than 3")
    def primeter(self):
        return(sum(self.l))

    def getOrderedsides(self, increasing):
        if (increasing):
            return(sorted(self.l))
        else:
            return(sorted(self.l, reverse = True))

poly = polygon(lengths)
print(poly.primeter())
print(poly.getOrderedsides(increasing = True))
print(poly.getOrderedsides(increasing = False))
