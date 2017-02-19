
def func(number):
	return number >= 100

result = filter(func, [10, 47, 201, 99, 105, 192])
for n in result:
	print(n)

print(list(filter(lambda n : n >= 100, [10, 47, 201, 99, 105, 192])))

print()

print(hex(100))
print(hex(2))
print(hex(346780))

a = 100
b = "Kim"
c = a

print(id(a))
print(id(b))
print(id(c))
print(id(c) == id(a))

print()

print(int("123"))
print(int(51.3))

print("------")


class SomeClass():
	def __init__(self):
		pass

print(isinstance("하이욤", str))
print(isinstance(123, int))

s = SomeClass()
print(isinstance(s, SomeClass))
a = 100
print(isinstance(a, SomeClass))

print("------")

def sum(a, b):
	return a + b

a = 100
b = 250
result = sum(a, b)
print(result)
print((lambda a, b: a + b)(a, b))

sum = lambda a, b: a + b
print(sum(100, 250))

print("------")

calclist = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b]
print(calclist[0](10, 20))
print(calclist[1](50, 10))
print(calclist[2](12, 66))

print("------")

print(len([1, 2, 3, 4, 5]))
print(len("MontyPython"))

print("------")

print(list("안녕하세요."))
l = [1, 2, 3]
print(list(l) == l)

print("------")

def square(n):
	return n * n

nums = [10, 52, 3, 14, 71, 8, 9]
result = []
for n in nums:
	result.append(square(n))

print(result)

print("------")

print(list(map(square, nums)))

print("------")

print(list(map(lambda n: n*n, nums)))

print("------")

a = [1, 2, 3, 4, 5]
b = 'kangsungwoo'
print(max(a))
print(max(b))
print(min(a))
print(min(b))


print(pow(10, 4))
print(pow(2, 15))

a = [12, 42, 8, 14, 25]
b = 'kangsungwoo'
print(sorted(a))
print(sorted(b))

print(str(1234))


print(type(1234))
print(type('kang'))

s = SomeClass()
print(type(s))