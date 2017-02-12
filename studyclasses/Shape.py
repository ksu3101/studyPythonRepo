# Shape class

class Shape:
	type = None
	solidColor = None
	strokeColor = None
	x = 0
	y = 0
	width = 0
	height = 0

	def __init__(self, type, solidcolor, strokecolor, x, y):
		self.type = type
		self.solidColor = solidcolor
		self.strokeColor = strokecolor
		self.x = x
		self.y = y

	def setSize(self, width, height):
		self.width = width
		self.height = height

	def drawShape(self):
		print("%s : %d, %d, size is (%d, %d)" % (type, self.x, self.y, self.width, self.height))
