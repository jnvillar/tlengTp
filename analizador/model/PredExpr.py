from Tipo import *


class PredExpr(object):
    def __init__(self, expr):
        self.expr = expr
        self.value = None
        self.type = None
        self.initialExpression = False
        self.defined = False

    def isDefined(self):
        return self.defined

    def evaluate(self, context):

        self.expr.evaluate(context)

        if self.expr.isDefined():
            self.defined = True
            self.value = max(0, self.expr.getValue() - 1)

    def __str__(self):
        if self.type == Tipo("Undefined"):
            toPrint = "pred(" + str(self.expr) + ")"
        else:
            toPrint = ""
            for it in range(self.value):
                toPrint = toPrint + "succ("

            toPrint = toPrint + "0"
            for it in range(self.value):
                toPrint = toPrint + ")"

        if (self.initialExpression):
            toPrint = toPrint + ":" + str(self.type)
        return toPrint

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def setExprTypes(self, context):
        self.expr.setExprTypes(context)
        self.type = Tipo('Nat')
