#11. Class inheritance
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


class rectangle(Polygon):
    isRec=False
    area=0
    a=[]

    def __init__(self, components):
        if len(components)==4:
            self.a= components
            self.a = sorted(self.a, reverse= False)
            print("rectangle list: ", self.a)
            if(self.a[0]==self.a[1] and self.a[2]==self.a[3]):
                self.isRec= True
            else:
                self.isRec= False
                print("Error: format of components is not like as rectangle")
        else:
            self.isRec= False
            print("Error: number of components is not 4")
    
    
    def area(self):
        if self.isRec == True:
            area= self.a[0] * self.a[2]
            return area
        else:
            return "null"

a=(3,7,7,3)
rec = rectangle(a)
ar = rec.area()
print("Area of rectangle is: ", ar)


