class Persona:

    atribusto_clase = 0
    def __init__(self, atribusto_intancia):
        self.atribusto_intancia = atribusto_intancia


#programa principal
if __name__ == '__main__':
    print("*** Atribusto de Clase ***")
    print(Persona.atribusto_clase)
    Persona.atribusto_clase = 10
    print(Persona.atribusto_clase)

    print('Persona 1 ')
    persona1 = Persona(15)
    print(persona1.atribusto_clase)
    print(persona1.atribusto_intancia)

    persona2 = Persona(25)
    print('Persona2')
    print(persona2.atribusto_clase)
    print(persona2.atribusto_intancia)

