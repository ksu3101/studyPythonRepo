from studyclasses.Shape import Shape


class Circle(Shape):
	radius = 0

	def __init__(self, solidcolor, strokecolor, x, y, radius):
		Shape.__init__(self, solidcolor, strokecolor, x, y)
		self.radius = radius

