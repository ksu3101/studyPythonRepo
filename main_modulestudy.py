import calc
from calc import sum
from calc import divide
from studyclasses.Shape import Shape

print(sum(10, 30))
print(divide(12, 6))
print(calc.multiply(4, 8))

shape = Shape("Rectangle", "red", "blue", 10, 10)
shape.setSize(25, 50)
print(shape)
