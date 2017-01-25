# 딕셔너리 스터디


# 키값 쌍 추가
dic = {'name':'Kang', 'email':'kang1010@google.com', 'phone':'01012345678'}
print(dic)
dic['gender'] = 'male'
print(dic)

nums = {1:'kang', 2:'lee', 3:'park'}
print(nums)
nums[4] = 'jang'
print(nums)

# 키값 쌍 제거
dic = {'name':'Kang', 'email':'kang1010@google.com', 'phone':'01012345678'}
print(dic)
del dic['name']
print(dic)

nums = {1:'kang', 2:'lee', 3:'park'}
print(nums)
del nums[2]
print(nums)

# 값 얻기
dic = {'name':'Kang', 'email':'kang1010@google.com', 'phone':'01012345678'}
print(dic['name'])
print(dic['phone'])

nums = {1:'kang', 2:'lee', 3:'park'}
print(nums[1])
print(nums[3])

# 키들의 리스트 만들기
dickeys = dic.keys()
print(dickeys)
dickeys = list(dic.keys())
print(dickeys)

# 값들의 리스트 만들기
dicvalues = dic.values()
print(dicvalues)
dicvalues = list(dic.values())
print(dicvalues)

# 키와 값의 쌍을 튜플로 얻기
print(dic.items())
print(nums.items())

# 키로 값 얻기
print(dic.get('name'))
print(dic.get('phone'))
print(dic.get('address', 'not found'))
print(nums.get(1))
print(nums.get(3))

# 키 존재 여부 검색
print('name' in dic)
print('address' in dic)
print(1 in nums)
print(100 in nums)

if dic: print("dictionary has elements")

emptyDic = {}
if emptyDic: print("is not Empty dictionary.")
else: print("is empty dictionary.")
