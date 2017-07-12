import Tipo

class PredExpr(object):
	def __init__(object):

		if(object.getType() != "Nat"):
			raise Exception("No es un Nat")

		self.value = object.value
		self.type = Tipo("Nat")

	def __str__(self):

		res = "pred("
		for it in range(self.value):
			res = res + "succ("
		
		res = res + "0"

		for x in range(self.value):
			res = res + ")"

		res = res + ")"

	def evaluate(self,context):
		return max(0,self.value-1)

	def getType(self):
		return self.type

	def getValue(self):
		return self.value