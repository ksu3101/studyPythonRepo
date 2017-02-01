# play ground py

import sys

a = 10
b = 10
c = "Hell Korea"
d = "KangSungWoo"
e = b

print(a is b)	# true
print(a is c)	# false
print(b is a)	# true
print(c is d)	# false
print(e is b)	# true

print(sys.getrefcount(10))	# 35