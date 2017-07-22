from Tipo import *

class IsZeroExpr(object):
    def __init__(self, expr):
        self.type = None
        self.defined = False
        self.expr = expr
        self.initialExpression = False


    def __str__(self):
        toPrint = ""
        if not self.defined:
            toPrint = "IsZero("
            toPrint = toPrint + str(self.expr)
            toPrint = ")"
        else:
            print self.value == 0

        if self.initialExpression:
            toPrint = toPrint + ":" + str(self.type)

        print toPrint


    def evaluate(self, context):
        self.expr.evaluate(context)
        if self.expr.isDefined():
            self.value = self.expr.getValue() == 0
            self.defined = True


    def isDefined(self):
        return self.defined


    def setExprTypes(self, context):
        self.expr.setExprTypes(context)
        if self.expr.getType() == Tipo('Nat'):git
            self.type = Tipo('Bool')

    def getType(self):
        return self.type


    def getValue(self):
        return self.value == 0
