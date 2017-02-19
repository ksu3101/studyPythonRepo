
print(abs(-1))
print(abs(100))
print(abs(-25))

print()

print(all([1, 2, 3, 4, 5]))
print(all([1, 2, 3, 0]))
print(all(['lee', 'kim', '', 'kang']))
print(all((1, 2, 3, 4, 5)))

print()

print(any([1, 2, 3, 4, 5]))
print(any([1, 2, 3, 0]))
print(any(['lee', 'kim', '', 'kang']))
print(any((1, 2, 3, 4, 5)))
print(any([0, '', None]))

print()

print(chr(40))	# `(`
print(chr(35))	# `#`
print(chr(52))	# `4`
print(chr(74))	# `J`

print()

print(dir("String"))
print(dir([1, 2, 3]))
print(dir(Exception))

print()

print(divmod(10, 3))
print(divmod(22, 4))
print(divmod(42, 18))

print()

names = enumerate(('Kim', 'Lee', 'Park', 'Jang'))
for i, name in names:
	print("%d : %s" % (i, name))

print()

print(eval('1 + 2'))
print(eval('"kim" + "park"'))
print(eval('chr(74)'))