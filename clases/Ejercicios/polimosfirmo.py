class Animal:
    def hacer_sonido(self):
        print('Puedo hacer un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

def hacer_sonido_animal(animal):
    animal.hacer_sonido()

print("Clase Padre")
animal = Animal()
animal.hacer_sonido()

print('\n')
print('Clase Hija Perro')
perro1 = Perro()
hacer_sonido_animal(perro1)

print('\n')
print('clase Hija Gato')
gato1 = Gato()
hacer_sonido_animal(gato1)
