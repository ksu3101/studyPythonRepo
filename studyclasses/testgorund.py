
class Number:
	x = 0

	def __init__(self, x):
		self.x = x

	def __add__(self, other):
		if isinstance(other, Number):
			return self.x + other.x
		return self.x + other

n = Number(10)
print("%d" % (n + 100))
print("%d" % (n + Number(200)))
