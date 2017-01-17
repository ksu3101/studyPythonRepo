montyPython = "Monty python's Flying Circus"

# 문자열의 길이 `len()`
print("monty's count = %d" % len(montyPython))

# 문자열에서 특정 문자나 단어의 갯수 세기 `count()`
print(montyPython.count('o'))
print(montyPython.count('on'))

# 문자열에서 특정 문자의 인덱스 얻기 `find()` : 없을 경우 -1
# 가장 처음을 찾게 되는 문자의 인덱스를 얻는다.
print(montyPython.find('p'))
print(montyPython.find('z'))
print(montyPython.find('Circus'))

# find() 와 동일 하게 특정 문자의 인덱스를 얻는 `index()`
# 다른 점은 찾는 문자가 없을 경우 오류가 발생 된다.
print(montyPython.index('p'))
#print(montyPython.index('z'))  # 오류 발생

# 어떤 문자열의 문자들 사이 마다 주어지는 문자열을 삽입 하는 `join()`
joinText = ","
print(joinText.join(montyPython))   # M,o,n,t,y, ,p,y,t,h,o,n,',s, ,F,l,y,i,n,g, ,C,i,r,c,u,s

# 소문자를 대문자로 바꾸는 `upper()`
print(montyPython.upper())

# 대문자를 소문자로 바꾸는 `lower()`
upperString = "MONTY PYTHON'S FLYING CIRCUS"
print(montyPython.lower())

# 왼쪽 공백을 모두 지우는 `lstrip()`
spacestring = "     abc  d      "
print(spacestring.lstrip())

# 오른쪽 공백을 모두 지우는 `rstring()`
print(spacestring.rstrip())

# 왼쪽과 오른쪽 공백을 지우는 `strip()`
print(spacestring.strip())

# 문자열에서 어떤 문자열을 대상 문자열로 치환 하는 `replace()`
# 입력한 패러미터에서 첫번째는 치환할 대상 문자열
# 입력한 두번째 패러미터는 치환될 문자열
print(montyPython.replace("on", "9999"))    # M9999ty pyth9999's Flying Circus

# 문자열을 단어 단위로 나누는 `split()`
# 공백을 기준으로 문자열을 나눈다. [] 는 배열이라는 자료 형 으로서 나중에 알아 볼 것 이다.
print(montyPython.split())      # ['Monty', "python's", 'Flying', 'Circus']


