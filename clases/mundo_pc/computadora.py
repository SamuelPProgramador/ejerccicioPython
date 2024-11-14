from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:
    contador_computadora = 0
    def __init__(self, nombre, monitor, teclado, raton ):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return  f'''Nombre: {self.nombre} ID: {self.id_computadora}
                Monitor: {self.monitor} 
                Teclado: {self.teclado}
                Raton: {self.raton}'''

if __name__ == "__main__":
    teclado1 = Teclado('Dell','USB')
    monitor1 = Monitor('Dell','27pg')
    raton1 = Raton('Dell','USB')

    computadora1 = Computadora('Dell', monitor1, teclado1, raton1)
    print(computadora1)