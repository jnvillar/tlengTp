from Tipo import *


class ParanthesisExpr(object):
    def __init__(self, expr):
        self.expr = expr
        self.value = None
        self.type = None
        self.initialExpression = False
        self.defined = False

    def __str__(self):
        toPrint = ""
        if not self.defined:
            toPrint = "(" + str(self.expr) + ")"
        else:
            toPrint = str(self.expr)

        if (self.initialExpression):
            toPrint = toPrint + ":" + str(self.type)

        return toPrint

    def evaluate(self, context):
        self.expr.evaluate(context)
        if (self.expr.isDefined()):
            self.value = self.expr.getValue()
            self.defined = True

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def setExprTypes(self, context):
        self.expr.setExprTypes(context)
        self.type = self.expr.getType()

    def isDefined(self):
        return self.defined
