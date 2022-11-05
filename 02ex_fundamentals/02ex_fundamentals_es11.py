#11. Class inheritance

class polygon:
    
    def __init__(self,T):
        if len(T)>=3:
                self.T=T
    def getS(self,side_number):
        return self.T[side_number]
    
    def setS(self,side_length):
        return self.T+(side_length,)
    
    def perimeter(self):
        return sum(self.T)
    
    def getOrderedSides(self,increasing = True):
        return tuple(sorted(self.T,reverse= not increasing))

    
class rectangle(polygon):
    
    def __init__(self,T):
        if len(T)==4 and T[0]==T[2] and T[1]==T[3] :
            self.T=T
        else:
            return("Error:A rectangle has 4 sides, the 1st (resp.2d) and the 3rd (resp.4th  side should have the same length,  ")
    def area(self):
        return self.T[0]*self.T[1]


r=rectangle((3,4,3,4))
print(r.area())
