import math

class polygon:
        #create a class that accepts as an input the sides of a polygon and performs various operations
        x=[]

        def __init__(self, sides):
                if len(sides)<3:
                        print("Invalid input")
                else:
                        self.x=sides


        def getSides(self,n):
                return self.x[n]

        def setSides(self,n,xi):
                if n < len(self.x):
                        self.x[n] = xi
                else:
                        print("Index out of range")

        def perimeter(self):
                sum=0
                for i in range(len(self.x)):
                        sum+=self.x[i]
                return sum

        def getOrderedSides(increasing):
                list=[]
                if increasing==1:
                        for i in range(len(self.x)):
                                min=min(self.x)
                                list[i]=min
                                self.x.remove(min)
                if increasing==0:
                        for i in range(len(self.x)):
                                max=max(self.x)
                                list[i]=max
                                self.x.remove(max)
                return list


class rectangle(polygon):

	def __init__(self, sides):
		flag=0
		if len(sides)==4:
			for i in range(4):
				if sides.count(sides[i])!=2:
					flag=1
			if flag==0:
				self.x=sides
				print("Item created correctly")
			else:
				print("Invalid input")
		else:
			print("Invalid number of sides")

	def area(self):
		a=self.x[0]
		if self.x[1]==a:
			b=self.x[2]
		else:
			b=self.x[1]
		return a*b

rect_1=rectangle([1,1,3,4]) 
rect_2=rectangle([1,2,3])
rect_3=rectangle([2,4,4,2])
a=rect_3.area()
print(a)
