class VarExpr(object):
    def __init__(self, name):
        self.name = name
        self.expr = None
        self.value = None
        self.type = None


    def __str__(self):
        return str(self.name)

    def evaluate(self, context):
    	if self.name in context:
    		self.expr = context[self.name]
    		self.value = self.expr.getValue()

    def setExprTypes(self, context):
        if self.name not in context:
            raise Exception('ERROR: El termino no es cerrado (' + self.name + ' esta libre)')

        if (context[self.name] != None):
        	self.type = context[self.name].getType()
        else:
        	self.type = Tipo('Undefined')
        

    def getType(self):
    	return self.type
