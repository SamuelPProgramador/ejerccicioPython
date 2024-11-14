class Monitor:
    contador_monitores = 0
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return f''' ID: {self.id} Marca: {self.marca} Tamanio: {self.tamanio}'''

if __name__ =='__main__':
    monitor1 = Monitor("Dell","17pg")
    print(monitor1)

    monitor2 = Monitor('HP', '22pg')
    print(monitor2)