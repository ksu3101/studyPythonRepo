
class MyException(Exception):
	errorMsg = ""

	def __init__(self, errorMsg):
		self.errorMsg = errorMsg

	def __str__(self):
		return self.errorMsg


num = 23

try:
	num / 5

except ZeroDivisionError as error:
	print(error)

else:
	print("정상적인 케이스 입니다.")

finally:
	print("모든 실행 구문을 완료 했습니다.")



try:
	raise MyException("오류가 발생했습니다.")

except MyException as error:
	print(error)