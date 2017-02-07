# Rectangle clas
from studyclasses.Shape import Shape


class Rectangle(Shape):
	def __init__(self, solidcolor, strokecolor, x, y):
		super(self.__class__, self).__init__("Rectangle", solidcolor, strokecolor, x, y)
