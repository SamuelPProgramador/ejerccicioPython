from mundo_pc.Monitor import Monitor
from mundo_pc.Orden import Orden
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado
from mundo_pc.computadora import Computadora

print('*** Computadoras ***')
# Primer objeto de computadora
teclado2 = Teclado('HP', 'Bluetooth')
monitor2 = Monitor('HP', '24p')
raton2 = Raton('HP', 'Bluetooth')
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

# Segundo objeto de computadora
teclado3 = Teclado('Logitech', 'Inalámbrico')
monitor3 = Monitor('Samsung', '32p')
raton3 = Raton('Logitech', 'Inalámbrico')
computadora3 = Computadora('Ensamblada', monitor3, teclado3, raton3)

# Tercer objeto de computadora
teclado4 = Teclado('Lenovo', 'USB')
monitor4 = Monitor('Lenovo', '21p')
raton4 = Raton('Lenovo', 'USB')
computadora4 = Computadora('Lenovo', monitor4, teclado4, raton4)

# Cuarto objeto de computadora
teclado5 = Teclado('Acer', 'Bluetooth')
monitor5 = Monitor('Acer', '27p')
raton5 = Raton('Acer', 'Bluetooth')
computadora5 = Computadora('Acer', monitor5, teclado5, raton5)

# Quinto objeto de computadora
teclado6 = Teclado('Asus', 'USB')
monitor6 = Monitor('Asus', '29p')
raton6 = Raton('Asus', 'USB')
computadora6 = Computadora('Asus', monitor6, teclado6, raton6)


computadores1 = [computadora2, computadora3]
orden1 = Orden(computadores1)
print(orden1)