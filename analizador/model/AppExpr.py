from Tipo import *


class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.exprDer = expr1
        self.exprIzq = expr2
        self.type = None
        self.initialExpression = False
        self.value = None

        def evaluate(self, context, value=None):
            self.exprDer.evaluate(context)
            valDer = self.exprDer.getValue()
            self.exprIzq.evaluate(context, valDer)
            self.value = self.exprDer.getValue()

        def __str__(self):
            toPrint = ""
            if self.type == Tipo("Undefined"):
                toPrint = str(self.exprDer) + str(self.exprIzq)
            else:
                toPrint = toPrint + str(expr1)

            if self.initialExpression:
                toPrint = toPrint + ":" + str(self.type)
                toPrint = toPrint + str(self.exprDer.getType().img)

            print toPrint

        def setExprTypes(self, context):
            self.exprDer.setExprTypes(context)
            self.exprIzq.setExprTypes(context)

            if self.exprDer.getType().dom != self.exprIzq.getType().img:
                raise "No coinciden los tipos papa"

            if self.exprDer.getType() == Tipo('Nat'):
                self.type = Tipo('Nat')
            elif self.exprDer.getType() == Tipo('Bool'):
                self.type = Tipo('Bool')
            else:
                self.type = Tipo('Undefined')
