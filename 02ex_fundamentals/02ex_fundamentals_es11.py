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

class rectangle(polygon):
    def __init__(self,t):
        if len(t) == 2:
            self.t = t
            
    def area(self):
        return self.t[0]*self.t[1]
    
    def perimeter(self):
        return(2*sum(self.t))
    
l = [2,3]
r = rectangle(l)
print('length of the last side:',r.getLength(-1))
print('perimeter:',r.perimeter())
print(r.getOrderedSides()) 
print('Area of the rectangle:',r.area())
r.setLength(1,6)
print('length of the last side after change',r.getLength(-1))