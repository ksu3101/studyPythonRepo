# study

# * 으로 계단 그려보기
i = 0
while i < 5:
	i += 1
	print('*' * i)

print()

i = 5
while i > 0:
	print('*' * i)
	i -= 1

print()

i = 0
while i < 5:
	i += 1
	print((' ' * (i - 1)) + ('*' * (6 - i)))

print()

i = 0
while i < 5:
	i += 1
	print((' ' * (6 - i)) + ('*' * (i * 2 - 1)))

print()

value = 12345678
result = 0
while value != 0:
	result = (result * 10) + (value % 10)
	value //= 10
print(result)
