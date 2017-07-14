from Tipo import *


class PredExpr(object):
    def __init__(self, expr):
        self.expr = expr
        self.type = Tipo("Nat")

    def evaluate(self, context):

        if self.expr.getType() == "Nat":
            value = max(0, self.expr.evaluate(context) - 1)

            for it in range(value):
                res = res + "succ("

            res = res + "0"
            for it in range(value):
                res = res + ")"

            return
        else:
            return 'pred('+self.expr.evaluate(context)+')'

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
