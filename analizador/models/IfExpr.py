import sys

class IfExpr(object):
    def __init__(self, cond, trueValue, falseValue):
        self.cond = cond
        self.trueValue = trueValue
        self.falseValue = falseValue

    def __str__(self):
        return 'if '+str(self.hijo1)+' then '+str(self.hijo2)+' else '+str(self.hijo3)


    def validType(self):
    	if(differentType(trueValue, falseValue)):
        	raise Exception("Las dos opciones del if deben tener el mismo tipo")
        
    def evaluate(self, context):
    	cond = self.cond.evaluate(context)
        trueValue = self.trueValue.evaluate(context)
        falseValue = self.falseValue.evaluate(context)
    	
        if(cond):
        	return trueValue
        else:
        	return falseValue


    def differentType(trueValue, falseValue):
    	if(trueValue.getType().getDom() != 'Var' && falseValue.getType().getDom() != 'Var'):
    		if(str(trueValue.getType()) != str(falseValue.getType())):
    			return True

