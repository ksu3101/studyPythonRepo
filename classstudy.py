import studyclasses.Shape
from studyclasses.Rectangle import Rectangle

shape = studyclasses.Shape.Shape("default shape", "white", "black", 120, 100)

print("%s type = %s" % (shape.type, shape.type))
print("%s SolidColor = %s" % (shape.type, shape.solidColor))
print("%s StrokeColor = %s" % (shape.type, shape.strokeColor))
print("%s x = %d" % (shape.type, shape.x))
print("%s y = %d" % (shape.type, shape.y))

shape.setSize(200, 300)

print("%s width = %d" % (shape.type, shape.width))
print("%s height = %d" % (shape.type, shape.height))

print("- - - - - - - - - - - - - - - - - -")

rectangle = Rectangle("red", "green", 70, 50)

print("%s type = %s" % (rectangle.type, rectangle.type))
print("%s SolidColor = %s" % (rectangle.type, rectangle.solidColor))
print("%s StrokeColor = %s" % (rectangle.type, rectangle.strokeColor))
print("%s x = %d" % (rectangle.type, rectangle.x))
print("%s y = %d" % (rectangle.type, rectangle.y))

rectangle.setSize(100, 100)

print("%s width = %d" % (rectangle.type, rectangle.width))
print("%s height = %d" % (rectangle.type, rectangle.height))

print("- - - - - - - - - - - - - - - - - -")

