import sys
from Tipo import *

class BooleanExpr(object):
    def __init__(self, value):
        self.value = value
        self.type = Tipo("Bool")

    def __str__(self):
        return str(self.value).lower() 

        
    def evaluate(self):
        return self.value



