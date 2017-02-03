# function study

v = 10
def incrementValue(v):
	v += 20

incrementValue(v)
print(v)

print()

def sumValue(x, y):
	if x <= 0 or y <= 0: return None;
	return x + y

print(sumValue(10, 20))
print(sumValue(0, 50))

print()

def sum(*nums):
	result = 0
	for n in nums:
		result += n
	return result


def minus(*nums):
	result = 0
	for n in nums:
		result -= n
	return result


def divide(*nums):
	result = 0
	for n in nums:
		result /= n
	return result

def multyply(*nums):
	result = 0
	for n in nums:
		result *= n
	return result

print(sum(12, 34))
print(minus(12, 34))
print(divide(12, 34))
print(multyply(12, 34))

def sum(x, y):
	return x + y

print(sum(12, 34))
print(sum(100, 300))

print()

def createHelloWorld():
	return "HelloWorld"
print(createHelloWorld())

print()

def printHelloWorld(prefix, postfix):
	print(prefix + "Hello World" + postfix)
printHelloWorld("<<<", ">>>")

print()

def printLoveYou():
	print("I Love You")
printLoveYou()

print()

def sumOfAllNumbers(a, b, c, d, e, f, g):
	return a+b+c+d+e+f+g
print(sumOfAllNumbers(1, 2, 3, 4, 5, 6, 7))

print()

def sumOfAllNumbers(*nums):
	sum = 0
	for n in nums: sum += n
	return sum
print(sumOfAllNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

print()

def sum(value, *nums):
	sum = value
	for n in nums: sum += n
	return sum
print(sum(10000, 10, 20, 30, 40, 50))

