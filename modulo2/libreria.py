"""
ejericicio sistema de biblioteca
clase libro
atributos:
    
titulo(str)
autor (str)
paginas(int)
prestado(bool) incialmente en False
metodos:
prestar(): cambia el estado de prestado a True y muestra un mensaje indicando 
que el libro ha sido prestado.
devolver(): cambia el estado de prestado a False y muestra un mensaje indicando 
que el libro ha sido devuelto.
resumen():imprime titulo, autor y paginas
estado(): muestra si el libro está prestado o disponible"""

class Libro:
    def __init__(self, titulo: str, autor: str, paginas: int, prestado: bool = False):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.prestado = prestado

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def resumen(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

    def estado(self):
        if self.prestado:
            print(f"El libro '{self.titulo}' está prestado.")
        else:
            print(f"El libro '{self.titulo}' está disponible.")
            
'''
class biblioteca
atributo: nombre : str
self.libros: list[Libro]=[]
métodos:  agregar_libro, buscar_por_titulo, mostrar_libros
'''
            
  
libro1 = Libro("Arenas del desierto", "Dante Gebel", 500)
libro1.resumen()    
libro1.estado()
libro1.prestar()
libro1.estado()
libro1.devolver()
libro1.estado()



 