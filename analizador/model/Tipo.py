import sys


class Tipo(object):
    def __init__(self, dom, img=None):
        self.dom = dom
        self.img = img

    def __str__(self):
        if self.img == None or self.img == 'None':
            return str(self.dom)
        elif self.img.__class__.__name__ == 'Tipo' and self.img.img != None and self.dom.__class__.__name__ == 'Tipo' and self.dom.img != None:
            return '(' + str(self.dom) + ')' + '->(' + str(self.img) + ')'
        elif self.img.__class__.__name__ == 'Tipo' and self.img.img != None:
            return str(self.dom) + '->(' + str(self.img) + ')'
        else:
            return str(self.dom) + '->' + str(self.img)

    def getDom(self):
        return self.dom

    def getImg(self):
        return self.img

    def __eq__(self, other):
        return str(self) == str(other)

    def __ne__(self, other):
        return str(self) != str(other)
