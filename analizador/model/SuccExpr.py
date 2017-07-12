import Tipo

class SuccExpr(object):
	def __init__(object):
		if(object.getType != "Nat"):
			raise Exception("No es un Nat")

		self.value = object.value
		self.type = Tipo("Nat")

	def __str__(self):
		res = ""
		for it in range(self.value+1):
			res = res + "succ("

		res = res + "0"

		for x in range(self.value+1):
			res = res + ")"

	def evaluate(self,context):
		return self.value+1

	def getType(self):
		return self.type

	def getValue(self):
		return self.value