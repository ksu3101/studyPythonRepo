# if 문 스터디

value = 90
if value == 100:
	print("값이 100 이다")
elif value == 90:
	print("값이 90 이다")
else:
	print("값이 100이 아니다")

intValueTrue = 10
intValueFalse = 0

if intValueTrue:
	print("주어진 값은 %d입니다." % intValueTrue)
if intValueFalse:
	print("주어진 값은 %d입니다." % intValueFalse)
if intValueFalse == 0:
	pass
elif intValueFalse == False:
	print("주어진 값은 거짓으로 판명된 %d입니다." % intValueFalse)

print("- - - - - - - - - - - - - - - - - ")

# 비교 연산자
value = 120
if value == 120:
	print("값은 120 이다")
if value != 100:
	print("값은 100이 아니다")
if value > 100:
	print("값은 100보다 크다")
if value < 900:
	print("값은 900보다 작다")
if value >= 120:
	print("값은 120보다 같거나 크다")
if value <= 900:
	print("값은 900보다 같거나 작다")

print("- - - - - - - - - - - - - - - - - ")

# 예제 풀이
# 만약 5000원 이상을 가지고 있다면 택시를 탄다. 하지만 5000을 갖지 못하고 2000을 갖고 있다면 지하철을 탄다. 그리고 그보다 더 적다면 그냥 걸어서 간다.
money = 5000
if money >= 5000:
	print("택시를 타고 가자!!")
elif money == 2000:
	print("지하철을 타고 가자!!")
elif money < 2000:
	print("걸어 가자..")

print("- - - - - - - - - - - - - - - - - ")

# and or not
value = 100
strValue = ""
if value == 100 and value != 900:
	print("값은 정확히 100 이면서 900은 절대로 아니다.")
if value != 50 or value >= 100:
	print("값은 50이 아니거나 100보단 크거나 같다.")
if not value:
	print("값인 False(0)이 아니다.")
if not strValue:
	print("문자열이 현재 비어 있다.")
if not value == 900:
	print("값이 900 이 아니다.")

print("- - - - - - - - - - - - - - - - - ")

# in, not in
print("1 은 [1, 2, 3] 리스트 안에 존재 하는가? %s " % (1 in [1, 2, 3]))
print("`A` 는 (`K`, `C`, `D`) 튜플 안에 존재 하는가? %s " % ('A' in ('K', 'C', 'D')))
print("500 은 [100, 200, 300] 리스트 안에 존재하지 않는가?  %s " % (500 not in [100, 200, 300]))
print("`Kang` 은 [`Kim`, `Kang`, `Jang`] 리스트 안에 존재하지 않는가? %s " % ("Kang" not in ["Kim", "Kang", "Jang"]))
print("'D'는 'PythonDjango 문자열에 존재 하는 문자인가? %s " % ('D' in "PythonDjango"))

print("- - - - - - - - - - - - - - - - - ")

# one line
value = 10
if value == 10: print("값은 10 이다.")
else: print ("값은 10이 아니다")
