from Tipo import *
import sys


class LambdaExpr(object):
    def __init__(self, var, tipoVar, expr):
        self.var = var
        self.tipoVar = tipoVar
        self.expr = expr
        self.type = None
        self.value = self
        self.defined = False
        self.initialExpression = False

    def __str__(self):
        if not self.defined:
            toPrint = '\\' + str(self.var) + ':' + str(self.tipoVar) + '.' + str(self.expr)
        else:
            toPrint = str(self.expr)

        if (self.initialExpression):
            toPrint = toPrint + ":" + str(self.type)

        return toPrint

    def getName(self):
        if not self.defined:
            return str(self.var)
        return self.expr.getName()

    def evaluate(self, context, value=None):
        if self.value != self:
            if(not isinstance(self.value,int) or isinstance(self.value,bool)):
                self.value.evaluate(context)
        else:
            self.evaluateExpr(context)

    def evaluateExpr(self, context):
        if self.var.getName() in context:
            self.defined = True
            self.expr.evaluate(context)
            self.value = self.expr.getValue()
        else:
            self.expr.evaluate(context)

    def setExprTypes(self, context):
        if self.var.getName() in context:
            sys.stderr.write("Hay variables repetidas en distintas lambdas")
            exit(1)
        else:
            context[self.var.getName()] = self.tipoVar
            self.expr.setExprTypes(context)
            self.type = Tipo(self.tipoVar, self.expr.getType())

    def getType(self):
        return self.type

    def isDefined(self):
        return self.defined

    def getValue(self):
        return self.value
