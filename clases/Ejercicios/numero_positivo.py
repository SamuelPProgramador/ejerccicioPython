# contador, repeticiones = 1 ,5
# while contador <= repeticiones:
#     print(f'Buenos dias{contador}')
#     contador += 1
# else:
#     print('Fin del ciclo')

#contador, maximo = 1, 5
#while contador <= maximo:
   # print(contador)
   # contador += 1

# contador = 10
# while contador >= 1:
#     print(contador)
#     contador -= 1
#
# palabras = 'Hola Mundo'
# for palabra in palabras :
#     print(palabra, end='-')
# print('')
# for numero in range(1,10, 3):
#     print(numero)

for numero in range(1,11, 3):
    print(numero, end=' ')
print()
for numero in range(10, 0, -3):
    print(numero, end=' ')

print()
# acumulador = 0
# numeros = range(1, 6)
# for numero in numeros:
#     print(f'{acumulador} + {numero}')
#     acumulador += numero
#     print(f'Acumulador: {acumulador}')
# print(f'Resultado final: {acumulador}')

acumulador = 0
while numero <= 5:
    print(f'{acumulador} + {numero}')
    acumulador += numero
    print(acumulador)
    numero+=1
print(f'Resultado {acumulador}')