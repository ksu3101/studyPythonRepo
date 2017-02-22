import random

class Lotto:
	numbers = [i for i in range(1, 46)]

	def generate_number(self):
		random.shuffle(self.numbers)

	def __str__(self):
		return self.numbers[0:6].__str__()


lotto = Lotto()
lotto.generate_number()
print(lotto)
