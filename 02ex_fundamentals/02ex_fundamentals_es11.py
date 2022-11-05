lengths = (5,9,9,5)

class polygon:
	def __init__ (self, lengths):
		self.l = lengths
		if len(self.l) < 3:
			raise ValueError("The number of dimensions is less than 3")
	def primeter(self):
		return(sum(self.l))

	def getOrderedsides(self):
		return(sorted(self.l))
        
class rectangle(polygon):
	def __init__(self):
		polygon.__init__(self, lengths)
		if len(self.l) != 4 or len(set(self.l)) != 2:
			raise ValueError("The dimensions doesn't belong to a rectangle!")
	def area(self):
		dimensions = list(set(self.l))
		return(dimensions[0] * dimensions[1])
		
try:
	r = rectangle()
#	poly = polygon(lengths)
	print(r.area())
except ValueError as e:
	print(e)
