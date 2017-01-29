# while 반복문 스터디

# 기본
index = 1
while index <= 10:
	if index < 10:
		print("index 값은 %d 입니다." % index)
	else:
		print("index 값이 %d 입니다. 마지막 숫자 입니다." % index)
	index += 1

print(" - - - - - - - - - - - - - - -")

# continue, break
index = 0
while index <= 10:
	if index == 2:
		index += 1
		continue  # index 가 2일땐 index를 증가 시키고 다음 반복으로 진행
	elif index == 9:
		print("index 가 9일땐 강제 종료 합니다. ")
		break
	else:
		print("index 값은 %d 입니다." % index)
	index += 1

print(" - - - - - - - - - - - - - - -")

# 무한 반복
index = 1
while True:
	if index == 10:
		print("index 값은 10 입니다. 반복을 종료 합니다.")
		break
	print("index 값은 %d 입니다." % index)
	index += 1

print(" - - - - - - - - - - - - - - -")

# while 중첩
x = 1
y = 1
while x <= 9:
	if y == 10: y = 0
	while y <= 9:
		print("%d * %d = %d" % (x, y, x * y))
		y += 1
	x += 1
