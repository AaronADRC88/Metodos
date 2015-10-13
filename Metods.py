__author__ = 'aferreiradominguez'
class Punto(object):
    def __init__(self,x=0,y=0):

        if self.e_numero(x) and self.e_numero(y):
            self.x=x
            self.y=y

        else:
            raise TypeError("x e y deben ser valores numericos")

    def __str__(self):
        """mostrar ordenado"""
        return "("+ str(self.x)+", "+str(self.y)+")"

    def __add__(self, outroPunto):
        """devolve a suma """
        return Punto(self.x+outroPunto.x, self.y+outroPunto.y)
    def __sub__(self, other):
        """devolve a resta """
        return Punto(self.x-other.x, self.y-other.y)
    def e_numero(self,valor):
        return isinstance(valor,(int,float,  complex))


p = Punto(4,3)
p2= Punto(3,3)
print(str(p2.__add__(p)))
print(str(p+p2))
print(str(p-p2))
print(str(p.__sub__(p2)))
print (str(p))
