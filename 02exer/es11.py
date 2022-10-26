 
from es10  import polygon 
class rectangle(polygon):
    x = ()
    def __init__(self,N,components):
        if N == 4:
            
            print("The figure has 4 sides")
            i=0
            while i<N:
                if components.count(components[i])==2 and components.count(components[i+2])==2 :
                    self.x = components
                    print("The figure is  a rectangle")
                    
                    break
                elif components.count(components[i])==4:
                    raise ValueError('ERROR: It is a square or a rhombus not a rectangle')
                    break
                else:
                    raise ValueError('ERROR: It is not a rectangle')
                    #print("Error: figure is not a rectangle")
                    break
            i +=1        
        else:
            #print("Error: number of components is not 4")
            raise ValueError('ERROR: Number of sides is not 4')
    def area(self):
        if self.x[0]!=self.x[1]:
            return self.x[0]*self.x[1]
        else:
            return self.x[0]*self.x[2]
#l = (4,4,3,4)
l=()
N = int(input("Set the dimension of the figure: "))

for i in range(N):    
    element= float(input(""))
    l = l + (element,)

r = rectangle(N,l)
print(r.area())