#10. Class definition
import math
class Polygon:
    a=[]
    b=[]
    Dic={}
    prim=0
    def __init__(self, components):
        self.a = list(components)

    def __del__(self):
        print("Goodbye")

    def getDimension(self):
        return len(self.a)

    def getA(self, n):
        return self.a[n]

    def setA(self, n,ai):
        if n< len(self.a):
            self.a[n] = ai
        #print("Hi", len(self.a))

    def createPolygan(self):
        for i in range(len(self.a)):
            self.b.append(i)
            self.dec[i] = self.a[i]
            print(self.dec)
    
    def primeter(self):
        for i in range(len(self.a)):
            self.prim += self.a[i]
        return self.prim

    def getOrderedSides(self, increasing):
        self.b= tuple(sorted(self.a, reverse = not increasing))
        return self.b

a=(3,4,5)
pln = Polygon(a)
print("Dimension:", pln.getDimension())
pln.setA(1,6)   # set the first component to six
c=pln.getA(1)   # get the first component
print("changed side a[1] =", c)  # print the changed side
print("primeter: ", pln.primeter())
print("get order sides increasing",pln.getOrderedSides(True))
print("get order sides decreasing",pln.getOrderedSides(False))