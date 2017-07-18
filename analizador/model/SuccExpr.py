from Tipo import *


class SuccExpr(object):
    def __init__(self, expr):
        self.expr = expr
        self.value = None
        self.type = None
        self.initialExpression = False

    def __str__(self):
        toPrint = ""
        if self.type == Tipo("Undefined"):
            toPrint = "succ(" + str(expr) + ")"
        else:
            for it in range(self.value):
                toPrint = toPrint + "succ("
            toPrint = toPrint + "0"
            for x in range(self.value):
                toPrint = toPrint + ")"

        if (self.initialExpression):
            toPrint = toPrint + ":" + str(self.type)

        return toPrint

    def evaluate(self, context):

        self.expr.evaluate(context)
        if (self.expr.getType() == Tipo('Nat')):
            self.value = self.expr.getValue() + 1

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def setExprTypes(self, context):
        self.expr.setExprTypes(context)
        if self.expr.getType() == Tipo('Nat'):
            self.type = Tipo('Nat')
        else:
            self.type = Tipo('Undefined')
