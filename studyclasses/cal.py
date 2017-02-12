
class Calculator:
	x = 0
	y = 0

	# 클래스의 생성자
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# x 와 y 의 합을 얻는 함수
	def add(self):
		return self.x + self.y

	# x 에서 y 를 뺀 값을 얻는 함수
	def minus(self):
		return self.x + self.y

	# x 와 y를 나눈 값을 얻는 함수 (x 나 y가 둘 중 하나라도 0 일경우 0을 반환)
	def divide(self):
		if self.x == 0 or self.y == 0:
			return 0
		return self.x / self.y

	# x 와 y 를 곱한 값을 얻는 함수
	def multiply(self):
		return self.x * self.y

	def __add__(self, other):
		return self.add(self) + other.add()


class ScientificCalculator(Calculator):

	z = 0

	def __init__(self, x, y, z):
		Calculator.__init__(self, x, y)
		self.z = z

	def add(self):
		return Calculator.add(self) + self.z

	def mod(self):
		return self.x % self.y

	def squarex(self):
		return self.x ** 2

	def square(self):
		return self.x ** self.y


calc = Calculator(21, 3)
print("%d + %d = %d" % (calc.x, calc.y, calc.add()))
print("%d - %d = %d" % (calc.x, calc.y, calc.minus()))
print("%d / %d = %d" % (calc.x, calc.y, calc.divide()))
print("%d * %d = %d" % (calc.x, calc.y, calc.multiply()))

calc2 = Calculator(6, 9)
print("calc2 = %d" % (calc + calc2))

print()

sincalc = ScientificCalculator(14, 3, 12)
print("%d + %d + %d = %d" % (sincalc.x, sincalc.y, sincalc.z, sincalc.add()))
print("%d mod %d = %d" % (sincalc.x, sincalc.y, sincalc.mod()))
print("%d square %d = %d" % (sincalc.x, sincalc.y, sincalc.square()))
print("%d square 2 = %d" % (sincalc.x, sincalc.squarex()))

