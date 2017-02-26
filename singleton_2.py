# 싱글톤 구현 방법들

class BaseClass:

	@classmethod
	def gettext(cls):
		return "static method string"

def singleton(clazz):
	instances = {}
	def getinstance(*args, **kargs):
		if clazz not in instances:
			instances[clazz] = clazz(*args, **kargs)
		return instances[clazz]
	return getinstance

@singleton
class MainClass(BaseClass):
	pass

instance = singleton(MainClass)
print(type(instance))
print(instance.gettext())	# cannot find static method in function

