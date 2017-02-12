# Rectangle clas
from studyclasses.Shape import Shape


class Rectangle(Shape):
	pathColor = None

	def __init__(self, solidcolor, strokecolor, x, y, pathtype, pathcolor):
		Shape.__init__(self, "Rectangle", solidcolor, strokecolor, x, y)
		self.pathType = pathtype
		self.pathColor = pathcolor

	def drawShape(self):
		Shape.drawShape(self)
		print("%s : %d, %d, size is (%d, %d)" % (type, self.x, self.y, self.width, self.height))

