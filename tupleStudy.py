# Tuple Study

t1 = (1,)   # 단 한개의 원소만 가졌을 경우에도 ,를 붙인다
print(t1)

t = (1, 2, 3, 4, 5)
print(t)

#t[2] = 100
#print(t)

#del t[2]        # 원소 삭제 시도시 오류

tmp = (95, 96)
t += tmp        # append() 함수가 없음
print(t)

tstr = ("kang", "lee", "park", "kim", "lee", "jung")
print(tstr.index("park"))       # 2 출력 (2번째 인덱스에 위치)
print(tstr.count("lee"))        # `lee`라는 문자열이 2개 존재
print(tstr[2:])                 # `park` 부터 마지막 원소 까지 출력

print("%d" % len(tstr))