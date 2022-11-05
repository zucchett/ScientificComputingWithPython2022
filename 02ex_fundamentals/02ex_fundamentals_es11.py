class rectangle(polygon):
    def __init__(self, components):
        if len(components) == 4:
            self.x = components
            print("The rectangle is of sides: ", components)
        else:
            raise Exception("This is not rectangle")

    def area(self):
        return (max(self.x) * min(self.x))

    
a = rectangle((4,2,4,2))

print("The area of rectangle is: ", a.area())
