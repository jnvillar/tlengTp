import Tipo


class NatExpr(object):
    def __init__(object):
        self.value = object
        self.type = Tipo("Nat")

        def __str__(self):
            res = ""
            for it in range(self.value):
                res = res + "succ("

            res = res + "0"

            for x in range(self.value):
                res = res + ")"

    def evaluate(self, context):
        return self.value

    def getType(self):
        return self.type

    def getValue(self):
        return self.value
