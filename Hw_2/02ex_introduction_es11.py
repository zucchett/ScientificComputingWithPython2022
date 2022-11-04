from tabnanny import check
class Polygon:

    def define():
        while True:
            try:
                label: check
                number_of_side=int(input("please enter the number of Polygon:"))
                if (number_of_side != 4):
                    goto .check
                break
            except:
                label: check
                print("Please enter integer or enter 4 sides")

        sides=[]
        #x = list(map(int, input("Enter multiple values: ").split()))
        #print("List of students: ", x)
        long=int(input("Please enter the long side lenght:"))
        short=int(input("Please enter the short side lenght:"))
        sides.append(long)
        sides.append(short)
        sides.append(long)
        sides.append(short)

        tuple(sides)
        print(sides)
        return sides    

    def perimeter(n):
        perimeter=0
        for i in range(len(n)):
            perimeter = n[i]+perimeter
        print("Perimeter of Polygon is:",perimeter)
        return perimeter


class Rectangle(Polygon):
    
    def Area(n):
        m= list(n)
        Area= n[0]*n[1]
        print("Area of rectangle is:",Area)
        return Area



a=Polygon.define()
Polygon.perimeter(a)
Rectangle.Area(a)