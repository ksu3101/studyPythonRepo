# 테스트

print("Hello World")

# 자료형

# integer
intvalue = 10
minusIntValue = -200
print(minusIntValue)

# long / big number
longValue = 98765432109876543210987654321
print(longValue)

# float
print(intvalue)
floatValue = 0.12345678901
print(floatValue)
minusFloatValue = -45.223
print(minusFloatValue)

# Octal number
octalValue = 0o1234
print(octalValue)

# Hexa number
hexaValue = 0x1234
print(hexaValue)

# 사칙 연산
a = 10
b = 25
c = 0.55

print(a + b)
print(b - a)
print(a * c)
print(b / a)

# 제곱 연산 (x 의 y 제곱) `**`
print(a ** b)
print(b ** a)

# 나머지 연산 `%`
print(b % a)

# 나누고 나머지를 버림 `//`
# 음수에 이 연산자를 사용 할 경우 조심 해야 한다.
print(b / a)
print(b // a)


# 문자열 자료형

textValue = 'hello world'
print(textValue)

longTextValue = '안녕하세요.\n반갑습니다.'
print(longTextValue)


text1 = "안녕"
text2 = "하세요?"
print(text1 + text2)

dashChar = '-'
print(dashChar * 20)
print(textValue)
print(dashChar * 20)

montyPython = "Monty python's Flying Circus"
print(montyPython[7])
print(montyPython[15])

print(montyPython[-0])
print(montyPython[-8])

print(montyPython[0:14])
print(montyPython[15:21])

print(montyPython[:14])
print(montyPython[:])
print(montyPython[:30])

# formating

print("Hello, %s World!!" % "Python")   # 문자열 대입
print("Hello, %d World!!" % 1000)       # 숫자 대입
print("Hello, %d World!!" % b)          # 숫자 변수 대입

# 여러개 대입
print("Hello, %s World!! %d" % ("Python", a))
print("%d + %d = %d" % (a, b, a+b))

# 퍼센트 문자 사용
print("경험치 %d%%가 증가 하였습니다. 앞으로 %d%%가 더 필요합니다." % (5, 12))

# 공백 및 소수점
print("===== %20d =====" % 98)
print("%.4f" % 0.123456789)

