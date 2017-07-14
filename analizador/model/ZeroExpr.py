from analizador.model.oldModels import Tipo


class ZeroExpr(object):
    def __init__(self):
        self.value = 0
        self.type = Tipo("Nat")

    def evaluate(self, context):
        return self.value

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
