from Tipo import *
import sys


class VarExpr(object):
    def __init__(self, name):
        self.name = name
        self.expr = None
        self.value = self
        self.type = None
        self.defined = False

    def __str__(self):
        if self.defined:
            toPrint = str(self.value)
        else:
            toPrint = str(self.name)

        return toPrint

    def evaluate(self, context, value=None):
        if self.name in context and context[self.name] != None:
            self.value = context[self.name]
            self.defined = True

    def setExprTypes(self, context):
        if self.name not in context:
            sys.stderr.write('ERROR: El termino no es cerrado (' + self.name + ' esta libre)')

        if (context[self.name] != None):
            self.type = context[self.name]

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def isDefined(self):
        return self.defined
