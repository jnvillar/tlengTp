from analizador.model import Tipo


class NatExpr(object):
    def __init__(self, value):
        self.value = int(value)
        self.type = Tipo.Tipo("Nat")
        self.initialExpression = False
        self.defined = True

    def evaluate(self, context):
        pass

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def setExprTypes(self, context):
    	pass

    def isDefined(self):
        return self.defined

    def __str__(self):
        toPrint = ""
        for it in range(self.value):
            toPrint = toPrint + "succ("
        toPrint = toPrint + "0"
        for x in range(self.value):
            toPrint = toPrint + ")"

        if(self.initialExpression):
            toPrint = toPrint+":"+str(self.type)
        return toPrint