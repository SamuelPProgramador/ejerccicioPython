from Sistema_concecionario_autos.Autos import Auto
from Sistema_concecionario_autos.Concecionario import Concecionario

concecionaroA = Concecionario('Dealer ABC')
auto1 = Auto('Mercedez','AMG', 'YWZ-123', 'NEGRA')
concecionaroA.agregarAuto(auto1)
concecionaroA.mostrarTodosLosAutos()

marca = 'Mercedez'
concecionaroA.mostrarAutosMarca(marca)