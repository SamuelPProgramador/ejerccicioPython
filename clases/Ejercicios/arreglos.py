# frutas = ["manzana", "banana", "naranja", "pera", "uva", "mango", "piña", "fresa", "cereza", "kiwi"]
# for fruta in frutas:
#     print(fruta)
#
# for index, fruta in enumerate(frutas):
#     print(f'Fruta [{index + 1}] = {fruta}')


no_elemento = int(input("Cantidad de Carros a agregar: "))
carros = [0] * no_elemento

for index in range(no_elemento):
    valor = input("Elemento: ")
    carros.append(valor)

for index, carro in enumerate(carros):
    print(carro)