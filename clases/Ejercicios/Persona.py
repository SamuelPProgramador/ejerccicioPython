class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrarPersona(self):
        print(f''' Persona
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

if __name__ == '__main__':
    persona1 = Persona('Samuel', 'Arias')
    persona1.mostrarPersona()

    persona2 = Persona('Luz', 'Penalo')
    persona2.mostrarPersona()


