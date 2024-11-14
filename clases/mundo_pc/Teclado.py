from mundo_pc.DipositivoEntrada import DipositivosEntrada

class Teclado(DipositivosEntrada):
    contador_teclado = 0;
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'''ID: {self.id}  Marca: {self.marca} Tipo de entrada: {self.tipo_entrada}'''

if __name__ == '__main__':
    teclado1 = Teclado('HP','USB')
    print(teclado1)

    teclado2 = Teclado('DELL', 'pullita')
    print(teclado2)