import sys
from Tipo import *

class BooleanExpr(object):
    def __init__(self, value):
        self.realValue = value
        self.value = self
        self.type = Tipo("Bool")
        self.initialExpression = False
        self.defined = True

    def __str__(self):
        toPrint = str(self.realValue).lower()

        if(self.initialExpression):
            toPrint = toPrint+":"+str(self.type)
        return toPrint


    def getValue(self):
    	return self.realValue

    def getType(self):
    	return self.type
        
    def evaluate(self, context,value = None):
        pass

    def isDefined(self):
        return self.defined

    def setExprTypes(self, context):
    	pass

