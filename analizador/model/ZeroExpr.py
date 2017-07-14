from analizador.model import Tipo


class Zero(object):
    def __init__():
        self.value = 0
        self.type = Tipo("Nat")

    def __str__(self):
        return "0"

    def evaluate(self, context):
        return self.value

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
