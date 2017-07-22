from Tipo import *

g_count = 0

class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.exprIzq = expr1
        self.exprDer = expr2
        self.type = None
        self.initialExpression = False
        self.value = self
        self.defined = False
        self.name = None

    def evaluate(self, context, value=None):
        global g_count
        count = g_count
        g_count = g_count+1

        if self.exprIzq.getValue() != None:
            self.exprIzq.getValue().evaluate(context)
        else:
            self.exprIzq.evaluate(context)
        if self.exprDer.getValue() != None and not isinstance(self.exprDer.getValue(), int):
            self.exprDer.getValue().evaluate(context)
        else:
            self.exprDer.evaluate(context)
        #self.exprIzq.evaluate(context)
        #self.exprDer.evaluate(context)
        valIzq = self.exprIzq.getValue()
        valDer = self.exprDer.getValue()
        print str(count)+". AppExpr - ExprLeft: "+str(self.exprIzq)
        print str(count)+". AppExpr - ExprLeft type: "+str(self.exprIzq.__class__.__name__)
        print str(count)+". AppExpr - ExprLeft Value: "+str(valIzq)
        print str(count)+". AppExpr - ExprLeft Value type: "+str(valIzq.__class__.__name__)
        print str(count)+". AppExpr - RightVal: "+str(valDer)
        #if valDer != None and valIzq != None:
        if not (valDer.__class__.__name__ == 'VarExpr' and valDer.getValue() == valDer):
            print str(count)+". AppExpr - VarName: "+str(self.exprIzq.getValue().getName())
            context[self.exprIzq.getValue().getName()] = valDer
            self.defined = True
            #self.name = self.exprIzq.getValue().getName()
            self.exprIzq.getValue().evaluate(context, count)
            self.value = self.exprIzq.getValue()

        

    def __str__(self):
        toPrint = ""
        if not self.defined:
            toPrint = str(self.exprIzq) + " " + str(self.exprDer)
        else:
            toPrint = toPrint + str(self.exprIzq)

        if self.initialExpression:
            toPrint = toPrint + ":" + str(self.type)

        return toPrint


    def setExprTypes(self, context):
        self.exprDer.setExprTypes(context)
        self.exprIzq.setExprTypes(context)
        if self.exprIzq.getType().getImg() == None:
            raise Exception("ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en " + str(self.exprDer.getType()))
        
        self.type = Tipo(self.exprIzq.getType().getImg().getDom(), self.exprIzq.getType().getImg().getImg())


    def getType(self):
        return self.type

    def getValue(self):
        return self.value


    def getName(self):
        return self.name
        #return self.value.getName()

    def isDefined(self):
        return self.defined

