from mundo_pc.DipositivoEntrada import DipositivosEntrada

class Raton(DipositivosEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones +=1
        self.id = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada

    def __str__(self):
        return (f'''ID: {self.id} Marca: {self.marca} Tipo Entrada: {self.tipo_entrada}''')

if __name__ == "__main__":
    raton1 = Raton('HP','USB')
    print(raton1)
    raton2 = Raton("dell", 'USB')
    print(raton2)