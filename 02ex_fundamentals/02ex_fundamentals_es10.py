import math
class polygon:

    x=()
    def __init__ (self,slength):
        if len(slength)<3:
            print("Side count must be 3 or more")
        else:
            self.x=slength
        
    def perimeter(self):
        a = sum(self.x)
        print ("The primeter is:",a)
    def getOrderedSides(self, b):
        s_tuple = sorted(self.x)
        if b == True:
            print(s_tuple)
            return s_tuple
        else:
            c=[]
            c = s_tuple
            c.reverse()
            print(c)
            r_tuples =()
            r_tuples = c
            return r_tuples
            

p1 = polygon((19,2,4,8))
p1.perimeter()
p1.getOrderedSides(True)
