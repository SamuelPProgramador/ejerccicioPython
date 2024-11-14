from sistema_empelados.empresa import Empresa, Empleado

empresa1 = Empresa('Big Bro Studis')

empresa1.contratar_empleados('Samuel', 'Tecnologia')
empresa1.contratar_empleados('Cristian', 'Tecnologia')
empresa1.contratar_empleados('Tapia', 'Tecnologia')
empresa1.contratar_empleados('Ronny', 'Contabilida')

print(f'Total de empleados:  {Empleado.obtener_contador_total_empleado()}')

print(f'Empelado en el departamento de Tecnologia: '
      f'{empresa1.obtener_numero_empleado_por_departamento("Tecnologia")}')

empresa1.obtener_total_empleado()

