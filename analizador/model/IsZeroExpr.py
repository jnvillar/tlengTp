import Tipo

class IsZeroExpr(object):
	def __init__(object):
		if(object.getType() != "Nat"):
			raise Exception("No es un Nat")

		self.value = object.getValue()
		self.type = Tipo("Bool")

def __str__(self):
	res = "IsZero("
		for it in range(self.value):
			res = res + "succ("

		res = res + "0"

		for x in range(self.value):
			res = res + ")"

		res = res + ")"

def evaluate(self,context):
	return self.value==0

def getType(self):
	return self.type

def getValue(self):
	return self.value==0