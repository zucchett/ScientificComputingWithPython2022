import math

class polygon:
	#create a class that accepts as an input the sides of a polygon and performs various operations 
	x=[]	

	def __init__(self, sides):
		if len(sides)<3:
			print("Invalid input")
		else:
			self.x=sides	

	def __del__(self):
        	print("Goodbye")

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

