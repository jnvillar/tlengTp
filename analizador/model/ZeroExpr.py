from analizador.model.oldModels import Tipo


class ZeroExpr(object):
    def __init__(self):
        self.value = 0
        self.type = Tipo("Nat")
        self.initialExpression = False

    def evaluate(self, context):
        pass

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def setExprTypes(self, context):
    	pass

    def __str__(self):
    	toPrint = ""+str(self.value)

    	if(self.initialExpression):
            toPrint = toPrint+":"+str(self.type)
        return toPrint