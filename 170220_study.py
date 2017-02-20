

def reverse_number(n):
	result = 0
	while n != 0:
		result *= 10
		result += n % 10
		n //= 10
	return result

print(reverse_number(12345))
print(reverse_number(593721367))

