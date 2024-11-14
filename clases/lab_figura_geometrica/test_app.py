from lab_figura_geometrica.Cuadrado import Cuadrado
from lab_figura_geometrica.Rectangulo import Rectangulo

print('Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado = 5, color='Verde')
print(cuadrado1)

print('Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho = 5, alto = 10, color = 'verde')
print(rectangulo1.calcular_area())

