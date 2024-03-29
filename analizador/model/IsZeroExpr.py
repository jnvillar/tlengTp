from Tipo import *


class IsZeroExpr(object):
    def __init__(self, expr):
        self.value = None
        self.type = None
        self.defined = False
        self.expr = expr
        self.initialExpression = False

    def __str__(self):
        toPrint = ""
        if not self.defined:
            toPrint = toPrint + "iszero("
            toPrint = toPrint + str(self.expr)
            toPrint = toPrint + ")"
        else:
            toPrint = toPrint + str(self.value)

        if self.initialExpression:
            toPrint = toPrint + ":" + str(self.type)

        return toPrint

    def evaluate(self, context, value = None):
        self.expr.evaluate(context)
        if self.expr.isDefined():
            self.value = self.expr.getValue() == 0
            self.defined = True

    def isDefined(self):
        return self.defined

    def setExprTypes(self, context):
        self.expr.setExprTypes(context)
        if self.expr.getType() == Tipo('Nat'):
            self.type = Tipo('Bool')
        else:
            raise Exception("iszero toma como parametro un Nat. Fue pasado un elemento de tipo: "+str(self.expr.getType()))

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
