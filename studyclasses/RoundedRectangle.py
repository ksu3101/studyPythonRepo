# RoundedRectangle class
from studyclasses.Rectangle import Rectangle


class RoundedRectangle(Rectangle):
	radius = 0

	def __init__(self, solidcolor, strokecolor, x, y, pathtype, pathcolor, radius):
		Rectangle.__init__(self, solidcolor, strokecolor, x, y, pathtype, pathcolor)
		self.type = "RoundedRectangle"
		self.radius = radius
