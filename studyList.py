# List study

# list examples
list1 = []
list2 = [1, 2, 3]
list3 = ['kang', 'kim', 'park']
list4 = ['kim', 100, 0.15, 'lee']
list5 = [1, ['kim', 'jung', 'lee'], 2, 3]

strList = ['kim', 'lee', 'park', 'kang']
print(strList[0] + strList[2])

print(strList[-1])
testList = [1, 4, 6, 12, 20]
print(testList[-1])
testList2 = [5, 6, 7, ['kang', 'lee']]
print(testList2[-1])

print(testList2[-1][1])


aList = [1, 2, 3, 4]
bList = [5, 6, 7, 8]

# 리스트 더하기
print(aList + bList)

# 리스트 반복
print(aList * 2)
print(bList * 3)

# 리스트에서 원소 수정 하기
elist = [3, 5, 6]
elist[1] = 100
print(elist)

# 리스트에서 연속적 원소들을 수정 하기
elist = [4, 5, 6, 7]
elist[1:2] = ['a', 'b']
print(elist)

elist = [4, 5, 6, 7]
elist[1] = ['a', 'b']
print(elist)

# 리스트에서 원소를 삭제 하기
elist = [4, 5, 6, 7, 8, 9]
elist[1:3] = []
print(elist)

# 리스트에서 원소를 삭제
elist = [4, 5, 6, 7]
del elist[1]
print(elist)

# 리스트의 정렬
numList = [4, 2, 12, 8, 5, 1, 3]
numList.sort()
print(numList)

textList = ['r', 'Kim', 'jung', 'B', 'c', 'b', 'Zed', 'a']
textList.sort()
print(textList)

# 리스트 뒤집기
elist = [1, 2, 3, 4]
elist.reverse()
print(elist)

# 원소 탐색 하고 인덱스 얻기
elist = [11, 22, 33, 44]
print(elist.index(22))
slist = ['abc', 'kim', 'lee', 'park']
print(slist.index('abc'))
print(slist.index('zzzz'))      # 없을 경우