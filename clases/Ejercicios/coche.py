class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    # def __init__(self, marca, modelo, color):
    #     self.marca = marca #publico
    #     self._modelo = modelo #Protegido
    #     self.__color = color #Privado

    def conducir(self):
        print(f'''Conduciendo el Coche 
        Marca: {self._marca}
        Modelo:{self._modelo}
        Color: {self._color}''')


    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return  self._color

    @color.setter
    def color(self, color):
        self._color = color

if __name__ == '__main__':
    coche1 = Coche('Mercedez', 'AMG', 'Negro')
    coche1.conducir()
    print()
    print(f'''Marca del coche {coche1.marca}
         El modelo {coche1.modelo}
         El color {coche1.color}''')
