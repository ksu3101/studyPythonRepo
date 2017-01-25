# set study

s = set([1, 2, 3, 4])
print(s)

s = set("HelloWorld")
print(s)

s1 = set([1, 2, 4, 5, 6])
s2 = set([2, 3, 4, 9, 7])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

s = set([1, 2, 3])
# 값 추가 하기
s.add(4)
s.add(5)
print(s)

# 값 여러개 추가 하기
s.update([7, 8, 9])
print(s)

# 특정 값 제거 하기
s.remove(3)
print(s)


s = set([0, ])
s.add('kim')

print(s)