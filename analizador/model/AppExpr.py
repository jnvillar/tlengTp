from Tipo import *


class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.exprDer = expr1
        self.exprIzq = expr2
        self.type = None
        self.initialExpression = False
        self.value = None
        self.defined = False

    def evaluate(self, context, value=None):
        self.exprDer.evaluate(context)
        valDer = self.exprDer.getValue()
        self.exprIzq.evaluate(context, valDer)
        self.value = self.exprDer.getValue()
        if(self.exprIzq.img != None):
            self.defined = True

    def __str__(self):
        toPrint = ""
        if not self.defined:
            toPrint = str(self.exprDer) + str(self.exprIzq)
        else:
            toPrint = toPrint + str(self.exprIzq)

        if self.initialExpression:
            toPrint = toPrint + ":" + str(self.type)
            toPrint = toPrint + str(self.exprDer.getType().img)

        return toPrint


    def setExprTypes(self, context):
        self.exprDer.setExprTypes(context)
        self.exprIzq.setExprTypes(context)

        if self.exprIzq.getType().img == None:
            raise Exception("ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en " + str(self.exprDer.getType()))
        
        if self.exprDer.getType() == Tipo('Nat'):
            self.type = Tipo('Nat')
        elif self.exprDer.getType() == Tipo('Bool'):
            self.type = Tipo('Bool')
        else:
            self.type = Tipo('Undefined')
