from sistema_empelados.Empleado import Empleado

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleados(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_numero_empleado_por_departamento(self, depatamento):
        contador_empleado_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == depatamento:
                contador_empleado_por_departamento += 1
        return contador_empleado_por_departamento

    def obtener_total_empleado(self):
        print(f'\n Total empleado para la empresa {self.nombre}')
        for empleado in self.empleados:
            print(f'''Empleado: {empleado.id}
            Nombre: {empleado.nombre}
            Departamento: {empleado.departamento}''')
