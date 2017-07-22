from Tipo import *


class ParanthesisExpr(object):
    def __init__(self, expr):
        self.expr = expr
        self.value = None
        self.type = None
        self.initialExpression = False
        self.defined = False

    def __str__(self):
        if not self.defined:
            toPrint = "(" + str(self.expr) + ")"
        else:
            toPrint = str(self.expr)

        if (self.initialExpression):
            toPrint = toPrint + ":" + str(self.type)

        return toPrint

    def evaluate(self, context, value=None):
        self.expr.evaluate(context, value)
        if (self.expr.isDefined()):
            self.value = self.expr.getValue()
            self.defined = True

    def getType(self):
        return self.type

    def getValue(self):
        if not self.defined:
            return self
        return self.value

    def setExprTypes(self, context):
        self.expr.setExprTypes(context)
        self.type = self.expr.getType()

    def isDefined(self):
        return self.defined

    def getName(self):
        return self.expr.getName()
