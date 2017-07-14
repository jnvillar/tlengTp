
class AppExpr(object):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
       # self.expr = expr
        self.tipo = None
'''
        # def __str__(self):
        #     return '\\'+str(self.var)+':'+ str(self.tipo) +'.'+str(self.expr)


        def evaluar(self, context):
            return toStr(self)

        def tipar(self, context):
            if self.expr1.tipar(context).dom != self.expr1.tipar(context).img
                raise Exception(
                    "La parte izquierda de la aplicacion no es una funcion con dominio en " + self.expr1.tipar(
                        context).img)
            else:
                self.tipo = self.expr1.tipar(context).img
                return self.tipo
'''