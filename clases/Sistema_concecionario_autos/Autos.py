class Auto:
    def __init__(self, marca, modelo, matricula, color):
        self._marca = marca
        self._modelo = modelo
        self._matricula = matricula
        self._color = color

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return  self._modelo

    @property
    def matricula(self):
        return self._matricula

    @property
    def color(self):
        return self._color