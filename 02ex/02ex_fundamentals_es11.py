# Class inheritance

class polygon:
	
	x = []
	def __init__(self, components):
		if components == tuple(components):
			if len(components) >= 3:
				self.x = list(components)
				#print("Access the single sides of the polygons using indices 1-n.")
			else:
				print("Not enough sides to make a polygon.")
				self.x = None
		else:
			print("Input argument is not a tuple.")
			self.x = None
	
	def get(self):
		return self.x
		
	
	def getX(self, n):
		if n <= len(self.x) and n != 0:
			return self.x[n-1]
		else:
			print("Invalid index value.")
	
	def setX(self, n, xi):
		if n <= len(self.x) and n != 0:
			self.x[n-1] = xi
			print("Setting side n." + str(n) + " value to " + str(xi) + ".")
		else:
			print("Invalid index value.")
	
	def perimeter(self):
		peri = 0
		for n in range(len(self.x)):
			peri += (self.x[n-1])
		return peri
	
	def getOrderedSides(self, increasing = True):
		if increasing:
			self.x.sort()
		else:
			self.x.sort()
			self.x.reverse()
		return self.x

class rectangle(polygon):
	
	def __init__(self, components):
	
		if components == tuple(components):
			if len(components) == 4 and len(set(components)) == 2 and components.count(components[0]) == 2:
				self.x = list(components)
				#print("Access the single sides of the polygons using indices 1-n.")
			else:
				print("Input argument does not represent a rectangle.")
				self.x = None
		else:
			print("Input argument is not a tuple.")
			self.x = None
	
	def area(self):
		area = list(set(self.x))[0]*list(set(self.x))[1]
		return area
		
chocobar = rectangle((4,4,2,2))
if chocobar.get() != None:
	print("The inserted rectangle has sides: " + str(chocobar.get()) + ".")
	print("Side no.3 is equal to " + str(chocobar.getX(3)) + ".")
	print("The perimeter of the rectangle is equal to " + str(chocobar.perimeter()) + ".")
	print("Reordering the rectangle sides in increasing order: " + 	str(chocobar.getOrderedSides()))
	print("Reordering the rectangle sides in decreasing order: " + str(chocobar.getOrderedSides(False)))
	print("The rectangle's area is", str(chocobar.area()), ".")
