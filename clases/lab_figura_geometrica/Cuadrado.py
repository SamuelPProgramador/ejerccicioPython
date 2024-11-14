from lab_figura_geometrica.Color import Color
from lab_figura_geometrica.FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return  f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'