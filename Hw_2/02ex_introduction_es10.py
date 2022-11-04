from tabnanny import check
class Polygon:
    def define():
        while True:
            try:
                label: check
                number_of_side=int(input("please enter the number of Polygon:"))
                if (number_of_side < 3):
                    goto .check
                break
            except:
                print("Please enter integer or enter at least 3 sides")

        sides=[]
        #x = list(map(int, input("Enter multiple values: ").split()))
        #print("List of students: ", x)
        for i in range (number_of_side):
            sides.append(int(input("Please enter the side lenght:")))
        tuple(sides)
        #print(sides)
        return sides    

    def perimeter(n):
        perimeter=0
        for i in range(len(n)):
            perimeter = n[i]+perimeter
        print("Perimeter of Polygon is:",perimeter)
        return perimeter

    def getOrderedSides(increasing,n):
        if increasing:
            list.sort(n)
            print("The sides of polygon are:",n)





a=Polygon.define()
Polygon.perimeter(a)
Polygon.getOrderedSides(True,a)