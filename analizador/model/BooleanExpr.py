import sys
from Tipo import *

class BooleanExpr(object):
    def __init__(self, value):
        self.value = value
        self.type = Tipo("Bool")
        self.initialExpression = False

    def __str__(self):
        toPrint = str(self.value).lower()

        if(self.initialExpression):
            toPrint = toPrint+":"+str(self.type)
        return toPrint


    def getValue(self):
    	return self.value

    def getType(self):
    	return self.type
        
    def evaluate(self, context,value = None):
        pass


    def setExprTypes(self, context):
    	pass

