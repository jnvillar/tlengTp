import sys


class Tipo(object):
    def __init__(self, dom, img=None):
        self.dom = dom
        self.img = img

    def __str__(self):
        if (self.img == None or self.img == 'None'):
            return str(self.dom)
        else:
            return str(self.dom) + '->' + str(self.img)

    def evaluate(self):
        return self.value

    def getDom(self):
        return self.dom

    def getImg(self):
        return self.img

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return str(self) != str(other)
    

