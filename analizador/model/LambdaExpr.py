class LambdaExpr(object):
    def __init__(self, var, tipoVar, expr):
        self.var = var
        self.tipoVar = tipoVar
        self.expr = expr
        self.tipo = None
        self.value = None

    def __str__(self):
        return '\\' + str(self.var) + ':' + str(self.tipo) + '.' + str(self.expr)

    def evaluate(self, context, value):
        if (context[var.getName()]):
            self.expr.evaluar(context)

    def setExprTypes(self, context):
        if self.var.name in context:
            raise Exception("Hay variables repetidas en distintas lambdas")
        else:
            context[self.var.name] = tipo
            self.tipo = Tipo(tipoVar, expr.setExprTypes(context))
            return self.tipo

    def getType(self):
        return self.tipo

