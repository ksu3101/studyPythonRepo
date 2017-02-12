# Rectangle clas
from studyclasses.Shape import Shape


class Rectangle(Shape):
	path = None
	pathColor = None

	def __init__(self, solidcolor, strokecolor, x, y, pathtype, pathcolor):
		Shape.__init__(self, "Rectangle", solidcolor, strokecolor, x, y)
		self.pathType = pathtype
		self.pathColor = pathcolor
