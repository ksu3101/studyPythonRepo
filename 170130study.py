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

print()

# reverse string
text = "abcdefg"
print(text[::-1])

listText = list(text)
reversedText = ""
i = len(text) - 1
while i > -1:
	reversedText += listText[i]
	i -= 1
print(reversedText)

print()

text = "MRL"
listText = list(text)
caesar = ""
i = 0

while i < len(text):
	caesar += listText[i] + 3
	i += 1
print(caesar)

