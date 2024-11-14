class Animal:
    def puedo_comer(self):
        print('Como muchas veces al dias')

    def puedo_domir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    def puedo_domir(self):
        print('Duermo 15 hora al dias')


print("*** Ejemplo Herencia Pytho ***")
print("Soy un animal")
animal1 = Animal()
animal1.puedo_comer()
animal1.puedo_domir()

print("clase Hija")
perro1 = Perro()
perro1.hacer_sonido()
perro1.puedo_domir()