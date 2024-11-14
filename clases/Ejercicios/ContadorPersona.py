class Persona:
    contador_personas = 0
    def __init__(self, nombre, apellido):
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
    def mostrarPersona(self):
        print(f'''Personas id: {self.id}
        Nombre: {self.nombre}
        Apellido {self.apellido}''')
    @staticmethod
    def get_contador_personas_metodos():
        print("Metodo Estatico")
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_cla(cls):
        print("Metodo de clase")
        return cls.contador_personas
if __name__ == "__main__":
    persona1 = Persona('Samuel', 'Arias')
    persona1.mostrarPersona()

    persona2 = Persona('Luz', 'Penalo')
    persona2.mostrarPersona()

    print(Persona.get_contador_personas_metodos())
    print(persona2.get_contador_personas_cla())