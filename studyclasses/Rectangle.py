# Rectangle clas
from studyclasses.Shape import Shape


class Rectangle(Shape):
	path = None
	pathColor = None

	def __init__(self, solidcolor, strokecolor, x, y, pathtype, pathcolor):
		super(self.__class__, self).__init__("Rectangle", solidcolor, strokecolor, x, y)
		self.pathType = pathtype
		self.pathColor = pathcolor
