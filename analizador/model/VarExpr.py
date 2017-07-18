from Tipo import *

class VarExpr(object):
    def __init__(self, name):
        self.name = name
        self.expr = None
        self.value = None
        self.type = None
        self.defined = False


    def __str__(self):
        if self.defined:
            toPrint = str(self.value)
        else:
            toPrint = str(self.name)
        
        return toPrint

    def evaluate(self, context):
    	if self.name in context and context[self.name] != None:
            print("evaluated")
    		#self.expr = context[self.name]
    		#self.value = self.expr.getValue()
            self.value = context[self.name]
            self.defined = True
        else:
            print("not evaluated")

    def setExprTypes(self, context):
        if self.name not in context:
            raise Exception('ERROR: El termino no es cerrado (' + self.name + ' esta libre)')

        if (context[self.name] != None):
        	self.type = context[self.name]
        
        

    def getType(self):
    	return self.type

    def getName(self):
        return self.name

    def isDefined(self):
        return self.defined