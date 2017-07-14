from analizador.model import Tipo


class NatExpr(object):
    def __init__(self, expr):
        self.value = int(expr)
        self.type = Tipo.Tipo("Nat")

    def evaluate(self, context):
        return self.value

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
