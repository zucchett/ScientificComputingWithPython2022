lengths = (2, 5, 3, 12)

class polygon:
    def __init__(self, lengths):
        self.l = lengths

    def primeter(self):
        return(sum(self.l))

    def getOrderedsides(self):
        return(sorted(self.l))
        

poly = polygon(lengths)
print(poly.primeter())
print(poly.getOrderedsides())
