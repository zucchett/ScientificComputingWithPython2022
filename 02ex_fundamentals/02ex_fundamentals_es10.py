#10. Class definition

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
    
p1=polygon((5,4,3))
print(p1.perimeter())
print(p1.getOrderedSides(increasing = True)) 
    
