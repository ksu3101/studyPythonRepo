# for 반복문

scoreList = [32, 11, 94, 26, 86, 54, 62, 80, 73]
for score in scoreList:
	print("점수는 %d 입니다." % score)

# 튜플 원소를 갖는 리스트
tupleList = [(5, 10), (80, 42), (22, 19)]
for (x, y) in tupleList:
	print("%d + %d = %d" % (x, y, x+y))

# 반복과 제어
for score in scoreList:
	if score <= 60:
		print("점수 %d 는 불합격 입니다." % score)
	else:
		print("점수 %d 는 합격 입니다." % score)

print("- - - - - - - - - - - - - -")

# continue, break
scoreList = [32, 11, 94, 26, 86, 54, 62, 101, 80, 73]
for score in scoreList:
	if score <= 60:
		continue
	elif score > 100:
		print("오류!! 잘못된 점수인 %d 를 발견했습니다. 실행을 종료 합니다." % score)
		break
	else:
		print("점수 %d 는 합격 입니다." % score)

print("- - - - - - - - - - - - - -")

intList = range(5)
for value in intList:
	print("%d" % value)

print("- - - - - - - - - - - - - -")

intList = range(3, 8)
for value in intList:
	print("%d" % value)

print("- - - - - - - - - - - - - -")

sum = 0;
for value in range(1, 101):
	sum += value
print("1 부터 100까지의 합은 %d 입니다." % sum)

print("%d" % len(scoreList))

print("- - - - - - - - - - - - - -")

# 구구단

for x in range(2, 10):
	for y in range(1, 10):
		print("%d * %d = %d" % (x, y, x*y))

print("- - - - - - - - - - - - - -")

# 리스트 내포
value = []
for i in range(5):
	value.append(i * 2)
print(value)

# list comprehension (리스트 내포)
value = [i * 2 for i in range(5)]
print(value)

# list comprehension 두번째 예제 (0 부터 14까지 숫자들 중 짝수만)
value = [i for i in range(15) if i % 2 == 0]
print(value)

# 리스트 내 튜플의 list comprehension 세번째 예제 (n, n*n), ...
value = [(x, x*x) for x in range(5)]
print(value)