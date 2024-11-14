class Empleado:
    contador_empleados = 0
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados += 1
        self.id = Empleado.contador_empleados

    @classmethod
    def obtener_contador_total_empleado(cls):
        return cls.contador_empleados
