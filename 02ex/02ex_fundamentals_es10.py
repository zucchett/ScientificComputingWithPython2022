# Class definition

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
			print("Input is not a tuple.")
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
		
pentagon = polygon((3,5,7,6,4))
if pentagon.get() != None:
	print("The inserted polygon has sides: " + str(pentagon.get()) + ".")
	print("Side no.3 is equal to " + str(pentagon.getX(3)) + ".")
	pentagon.setX(3,2)
	print("Side no.3 value is now equal to " + str(pentagon.getX(3)) + ".")
	print("The modified polygon has sides: " + str(pentagon.get()) + ".")
	print("The perimeter of the polygon is equal to " + str(pentagon.perimeter()) + ".")
	print("Reordering the polygon sides in increasing order: " + 	str(pentagon.getOrderedSides()))
	print("Reordering the polygon sides in decreasing order: " + str(pentagon.getOrderedSides(False)))
