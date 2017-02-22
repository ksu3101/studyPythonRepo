import random

class upAndDown():
	num = random.randrange(1, 100)

	def checkNumber(self, n):
		if n > self.num:
			print("UP")
		elif n < self.num:
			print("Down")
		else:
			print("Correct")
			return True
		return False

uad = upAndDown()

userinput = input("in number (1~100) > ")