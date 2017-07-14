class VarExpr(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def evaluate(self, context):
        return context[self.name]

    def tipar(self, context):
        if self.name not in context:
            raise Exception('ERROR: El termino no es cerrado (' + self.name + ' esta libre)')
