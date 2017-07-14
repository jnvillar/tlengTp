class VarExpr(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def evaluate(self, context):
        return context[self.name]

    def tipar(self, context):
        if self.name not in context:
            raise Exception('ERROR: El término no es cerrado (' + self.name + ' está libre)')
