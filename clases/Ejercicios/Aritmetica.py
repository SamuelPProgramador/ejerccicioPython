class Arimetica:
    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def oprendo2(self, operando2):
        self._operando2 = operando2
    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'La suma es {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'La resta es: {resultado}')

    def multplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'La multiplicacion es: {resultado}')

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f'La division es: {resultado}')

if __name__ == '__main__':
    arimetica1 = Arimetica(5, 7)
    print(f'Valor del operando1 {arimetica1.operando1}')
    print(f'Valor del operenaod2 {arimetica1.operando2}')
    arimetica1.sumar()
    arimetica1.restar()

    aritmetica2 = Arimetica(10, 5)
    print(f'Valor del operando2 {aritmetica2.operando1}')
    print(f'Valor del operando2 {aritmetica2.operando2}')
    aritmetica2.dividir()
    aritmetica2.multplicar()
