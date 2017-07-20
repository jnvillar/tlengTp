from Tipo import *

class LambdaExpr(object):
    def __init__(self, var, tipoVar, expr):
        self.var = var
        self.tipoVar = tipoVar
        self.expr = expr
        self.type = None
        self.value = None
        self.defined = False
        self.initialExpression = False

    def __str__(self):
        if not self.defined:
            toPrint = '\\' + str(self.var) + ':' + str(self.tipoVar) + '.' + str(self.expr)
        else:
            toPrint = str(self.expr)

        if(self.initialExpression):
            toPrint = toPrint+":"+str(self.type)

        return toPrint

    def evaluate(self, context, value = None):
        context[self.var.getName()] = value
        if value != None:
            self.defined = True
        self.expr.evaluate(context)        


    def setExprTypes(self, context):
        if self.var.getName() in context:
            raise Exception("Hay variables repetidas en distintas lambdas")
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

