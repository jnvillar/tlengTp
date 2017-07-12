class LambdaExpr(object):
    def __init__(self, var, tipoVar, expr):
        self.var = var
        self.tipoVar = tipoVar
        self.expr = expr
        self.tipo = None


    def __str__(self):
        return '\\'+str(self.var)+':'+ str(self.tipo) +'.'+str(self.expr)


	def evaluar(self, context):
		return toStr(self)

	def tipar(self, context):
		if self.var.name in context:
			raise Exception("Hay variables repetidas en distintas lambdas")
		else:
			context[self.var.name] = tipo
			self.tipo = Tipo(tipoVar, expr.tipar(context))
			return self.tipo