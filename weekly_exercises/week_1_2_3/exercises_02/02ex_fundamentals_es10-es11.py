#Zuccolo Giada, matr. 2055702
# EXE 10
class Polygon:
    def __init__(self, components):
        self.components = components

    def setComponent(self, c):
        self.components = list(self.components)
        (self.components).append(c)
        self.components = tuple(self.components)

    def getComponent(self, c):
        return (self.components)[c]

    def getPolyComponents(self):
        return self.components

    def perimeter(self):
        return sum(list(self.components))

    def getOrderedPolyComponents(self, increasing):
        self.components = list(self.components)
        if increasing:
            self.components.sort()
            return tuple(self.components)
        else:
            self.components.sort(reverse=True)
            return tuple(self.components)


print("Creating a Polygon...")
l = int(input("#components: "))
while (l < 3):
    print("ERROR: to create a polygon at least 3 components are needed!")
    l = int(input("#components: "))
components_of_p = []
for x in range(l):
    components_of_p.append(float(input("Length of " + str(x + 1) + "^ component: ")))
components_of_p = tuple(components_of_p)

p = Polygon(components_of_p)

print("\nList of Poly Components")
for x in range(l):
    print(str(x+1)+"^ component: " + str(p.getComponent(x)))

print("\nHow many components do you want to add?")
new_l = int(input("#components: "))
if new_l!=0:
    for x in range(new_l):
        p.setComponent(float(input("Length of " + str(x + 1) + "^ new component: ")))

print("\nList of Poly Components")
print(p.getPolyComponents())

print("\nPerimeter = "+str(p.perimeter()))

print("\nList of components in ascending order = \t" + str(p.getOrderedPolyComponents(increasing = True)))
print("List of components in descending order = \t" + str(p.getOrderedPolyComponents(increasing = False)))




# EXE 11
class Rectangle(Polygon):
    def __init__(self, components):
        if len(components)==2: # components are equals group by 2 (base and height)
                self.components = components
        else:
            print("[ERROR]: component must be 2")

    def perimeter(self):
        return super().perimeter()*2

    def area(self):
        return self.components[0] * self.components[1]

print("\n\nCreating a Rectangle...")

r = Rectangle(((float(input("Length of base: "))),(float(input("Length of height: ")))))

print("\nPerimeter of rectangle = "+str(r.perimeter()))
print("Area of rectangle = " + str(r.area()))
