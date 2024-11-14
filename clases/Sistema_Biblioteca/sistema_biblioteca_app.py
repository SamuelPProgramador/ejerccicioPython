from Sistema_Biblioteca.Biblioteca import Biblioteca
from Sistema_Biblioteca.Libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional Domincana')
print(f'Bienvenido a la {bibliotecaNacional.nombre}')

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
libro2 = Libro("1984", "George Orwell", "Distopía")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")
libro4 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula")
libro5 = Libro("Orgullo y prejuicio", "Jane Austen", "Romance")

#agregamos los libro
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

genero = 'Romance'
bibliotecaNacional.buscar_libro_por_genero(genero)


bibliotecaNacional.mostrar_todos_los_libro()
