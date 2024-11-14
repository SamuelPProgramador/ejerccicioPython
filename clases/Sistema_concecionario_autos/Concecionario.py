
class Concecionario:
    def __init__(self, nombre):
        self._nombre = nombre
        self._autos = []
    @property
    def nombre(self):
        return self._nombre

    def agregarAuto(self, auto):
        self._autos.append(auto)

    def mostrarAutos(self, auto):
        print(f'Marca {auto.marca}'
              f'Modelo {auto.modelo}'
              f'Matricula {auto.matricula}'
              f'Color {auto.color}')

    def mostrarTodosLosAutos(self):
        print(f'Mostrar todos los Autos {self.nombre}')
        for auto in self._autos:
            self.mostrarAutos(auto)

    def mostrarAutosMarca(self, marca):
        for auto in self._autos:
            if auto.marca.lower() == marca.lower():
                self.mostrarAutos(auto)

    def mostrarAutoPorMatricula(self, matricula):
        for auto in self._autos:
            if auto.matricula.lowe() == matricula.lower():
                self.mostrarAutos(matricula)