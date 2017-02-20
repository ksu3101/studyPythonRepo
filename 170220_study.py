
def tonumber(obj, default_value):
	try:
		int(obj)
	except ValueError:
		return default_value
	return int(obj)

def reverse_number(n):
	result = 0
	while n != 0:
		result *= 10
		result += n % 10
		n //= 10
	return result

print(reverse_number(12345))
print(reverse_number(593721367))

print(tonumber("123", 0))
print(tonumber("kang", 0))