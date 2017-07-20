import sys
from Tipo import *


class IfExpr(object):
    def __init__(self, cond, trueExpr, falseExpr):
        self.value = None
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

    def evaluate(self, context, value = None):
        self.cond.evaluate(context)
        self.trueExpr.evaluate(context)
        self.falseExpr.evaluate(context)
        if self.cond.isDefined() and self.trueExpr.isDefined() and self.falseExpr.isDefined():
            self.defined = True

    def setExprTypes(self, context):
        self.cond.setExprTypes(context)
        self.trueExpr.setExprTypes(context)
        self.falseExpr.setExprTypes(context)
        self.type = self.trueExpr.getType()



        ##print "IF Tipo True: "+str(self.trueExpr.getType())
        ##print "IF Tipo False: "+str(self.falseExpr.getType())
        trueExprType = self.trueExpr.getType()
        falseExprType = self.falseExpr.getType()
        print "trueExprType: "+str(trueExprType) + "clase: "+ trueExprType.__class__.__name__
        print "falseExprType: "+str(falseExprType) + "clase: "+ falseExprType.__class__.__name__
        if (trueExprType != falseExprType):
            raise Exception("Las expresiones del if no son del mismo tipo")

        if (self.cond.getType() == Tipo('Bool')):
            self.value = self.trueExpr.getValue() if self.cond.getValue() else self.falseExpr.getValue()
            

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def isDefined(self):
        return self.defined

    def differentType(trueExpr, falseExpr):
        if (trueExpr.getType().getDom() != 'Var') & (falseExpr.getType().getDom() != 'Var'):
            if (str(trueExpr.getType()) != str(falseExpr.getType())):
                return True

    def validType(self):
        if self.differentType(self.trueExpr, self.falseExpr):
            raise Exception("Las dos opciones del if deben tener el mismo tipo")
