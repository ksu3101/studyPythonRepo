from studyclasses.Rectangle import Rectangle
from studyclasses.RoundedRectangle import RoundedRectangle
from studyclasses.Shape import Shape

shape = Shape("default shape", "white", "black", 120, 100)

print("%s type = %s" % (shape.type, shape.type))
print("%s SolidColor = %s" % (shape.type, shape.solidColor))
print("%s StrokeColor = %s" % (shape.type, shape.strokeColor))
print("%s x = %d" % (shape.type, shape.x))
print("%s y = %d" % (shape.type, shape.y))

shape.setSize(200, 300)

print("%s width = %d" % (shape.type, shape.width))
print("%s height = %d" % (shape.type, shape.height))

print("- - - - - - - - - - - - - - - - - -")

rectangle = Rectangle("red", "green", 70, 50, "Dot", "cyan")

print("%s type = %s" % (rectangle.type, rectangle.type))
print("%s SolidColor = %s" % (rectangle.type, rectangle.solidColor))
print("%s StrokeColor = %s" % (rectangle.type, rectangle.strokeColor))
print("%s pathType = %s" % (rectangle.type, rectangle.pathType))
print("%s pathColor = %s" % (rectangle.type, rectangle.pathColor))
print("%s x = %d" % (rectangle.type, rectangle.x))
print("%s y = %d" % (rectangle.type, rectangle.y))

rectangle.setSize(100, 100)

print("%s width = %d" % (rectangle.type, rectangle.width))
print("%s height = %d" % (rectangle.type, rectangle.height))

print("- - - - - - - - - - - - - - - - - -")

roundedrect = RoundedRectangle("blue", "white", 25, 25, "Normal", "black", 5)

print("%s type = %s" % (roundedrect.type, roundedrect.type))
print("%s SolidColor = %s" % (roundedrect.type, roundedrect.solidColor))
print("%s StrokeColor = %s" % (roundedrect.type, roundedrect.strokeColor))
print("%s pathType = %s" % (roundedrect.type, roundedrect.pathType))
print("%s pathColor = %s" % (roundedrect.type, roundedrect.pathColor))
print("%s x = %d" % (roundedrect.type, roundedrect.x))
print("%s y = %d" % (roundedrect.type, roundedrect.y))

roundedrect.setSize(75, 75)

print("%s width = %d" % (roundedrect.type, roundedrect.width))
print("%s height = %d" % (roundedrect.type, roundedrect.height))

print("- - - - - - - - - - - - - - - - - -")
