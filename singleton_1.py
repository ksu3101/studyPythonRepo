# 싱글톤 구현 방법들

class BaseClass:
	pass

class SingletonInstance:
	__instance = None

	@classmethod
	def getinstance(cls):
		return cls.__instance

	@classmethod
	def instance(cls, *args, **kargs):
		cls.__instance = cls(*args, **kargs)
		cls.instance = cls.getinstance
		return cls.__instance

class MainClass(BaseClass, SingletonInstance):
	pass

mainclass = MainClass.instance()
print(mainclass)


