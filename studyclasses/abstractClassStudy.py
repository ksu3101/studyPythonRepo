from enum import Enum
from abc import ABCMeta, abstractmethod


# Shape type enum
class ShapeType(Enum):
	Rectangle = 1
	Oval = 2


# Shape 추상 부모 클래스
class Shape(metaclass=ABCMeta):
	type = ShapeType.Rectangle
	x = 0
	y = 0
	width = 0
	height = 0

	def __init__(self, type, x, y):
		self.type = type
		self.x = x
		self.y = y

	# 추상 메소드
	@abstractmethod
	def drawShape(self):
		pass

	def setSize(self, width, height):
		self.width = width
		self.height = height

# Rectangle 클래스
class Rectangle(Shape):
	def __init__(self, x, y):
		super().__init__(ShapeType.Rectangle, x, y)

	def drawShape(self):
		print("%s : x = %d, y = %d, width = %d, height = %d" % (self.type, self.x, self.y, self.width, self.height))

	def __str__(self):
		return "%s : x = %d, y = %d, width = %d, height = %d" % (self.type, self.x, self.y, self.width, self.height)

# Circle 클래스
class Circle(Shape):
	radius = 0

	def __init__(self, x, y, radius):
		super().__init__(ShapeType.Oval, x, y)
		self.radius = radius

	def drawShape(self):
		print("%s : x = %d, y = %d, width = %d, height = %d, radius = %d" % (self.type, self.x, self.y, self.width, self.height, self.radius))

	def __str__(self):
		return "%s : x = %d, y = %d, width = %d, height = %d, radius = %d" % (self.type, self.x, self.y, self.width, self.height, self.radius)

rect = Rectangle(50, 30)
rect.setSize(100, 100)
#rect.drawShape()
print(rect)

circle = Circle(20, 20, 5)
circle.setSize(60, 60)
#circle.drawShape()
print(circle)
