class polygon:    
    x = tuple()
    
    def __init__(self, components):
        self.x = components
        print(components)
        
    def perimeter(self):
        
        return (sum(self.x))
    
    def getorderedSides(self,increasing = True or False):
        list_1 = []
        for i in range(len(self.x)):
                list_1.append(self.x[i])
        if increasing == True:
            list_1.sort()
            return (list_1)
        if increasing == False:
            list_1.sort(reverse = True)
            return (list_1)

a = polygon((3,9,1,4))

print("The perimeter is :", a.perimeter()) 
print("The orderedsides are:" , a.getorderedSides(increasing= True))