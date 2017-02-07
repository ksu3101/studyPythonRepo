# RoundedRectangle class
from studyclasses.Rectangle import Rectangle


class RoundedRectangle(Rectangle):
	radius = 0

	def __init__(self, solidcolor, strokecolor, x, y, pathtype, pathcolor, radius):
		super(self.__class__, self).__init__("RoundedRectangle", solidcolor, strokecolor, x, y, pathtype, pathcolor)
		self.radius = radius
