import sys
from Tipo import *


class IfExpr(object):
    def __init__(self, cond, trueExpr, falseExpr):
        self.value = self
        self.type = None
        self.cond = cond
        self.trueExpr = trueExpr
        self.falseExpr = falseExpr
        self.initialExpression = False
        self.defined = False

    def __str__(self):
        if not self.defined:
            toPrint = 'if ' + str(self.cond) + ' then ' + str(self.trueExpr) + ' else ' + str(self.falseExpr)
        else:
            if self.cond.getValue():
                toPrint = str(self.trueExpr)
            else:
                toPrint = str(self.falseExpr)

        if self.initialExpression:
            toPrint = toPrint + ":" + str(self.type)
        return toPrint

    def evaluate(self, context, value=None):
        if self.value != self:
            self.value.evaluate(context)
        else:
            self.evaluateExpr(context)

    def evaluateExpr(self, context):
        self.cond.evaluate(context,0)
        self.trueExpr.evaluate(context,0)
        self.falseExpr.evaluate(context,0)
        if self.cond.isDefined() and self.trueExpr.isDefined() and self.falseExpr.isDefined():
            self.defined = True
            self.value = self.trueExpr.getValue() if self.cond.getValue() else self.falseExpr.getValue()

    def setExprTypes(self, context):
        self.cond.setExprTypes(context)
        self.trueExpr.setExprTypes(context)
        self.falseExpr.setExprTypes(context)
        self.type = self.trueExpr.getType()
        trueExprType = self.trueExpr.getType()
        falseExprType = self.falseExpr.getType()
        if trueExprType != falseExprType:
            raise Exception("Las expresiones del if no son del mismo tipo")
        if self.cond.getType() != Tipo('Bool'):
            raise Exception("Las condicion en el if debe ser de tipo Bool")

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def isDefined(self):
        return self.defined
