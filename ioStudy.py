# input / output study

def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


inputs = input("input > ")
print(inputs)

print()
print(type(inputs))		# only String

value = None
if inputs.isnumeric():	# 101:true, -101:false, 10.30:false
	value = int(inputs)
elif isfloat(inputs):
	value = float(inputs)
else:
	value = inputs

print()
print(value)
print("type of value is %s." % type(value))



