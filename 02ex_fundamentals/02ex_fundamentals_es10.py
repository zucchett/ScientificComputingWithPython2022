class polygon:
    def __init__(self,t):
        self.t = t
        
    def getLength(self,n):
        if n<len(self.t):
            return self.t[n]
        
    def setLength(self,n,L):
        if n<len(self.t):
            self.t[n] = L
                
    def perimeter(self):
        return(sum(self.t))
        
    def getOrderedSides(self,increasing = True):
        x = self.t
        x.sort(reverse = increasing)
        return x
    
t = [1,2,3] 
p = polygon(t)
print('length of the last side:',p.getLength(-1))
p.setLength(2,6)
print('length after change:',p.getLength(-1))
print('perimeter:',p.perimeter())
print(p.getOrderedSides())        