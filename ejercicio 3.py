# Hugo Alvarez
# Ingeniería en Sistemas
"""
Carné: 0909-26-12678
Nombre del curso: Algoritmos
Nombre del catedrático: M.A. Ing. Amilcar Josimar Sagastume Diaz
Fecha: 31/10/2026
"""

# EJERCICIO 3: Herencia

class Material:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion}")


class Libro(Material):
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_paginas: int):
        # Hereda atributos de la clase base Material usando super()
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        # Sobrescribe el método para incluir las páginas
        print(f"[LIBRO] Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion} | Páginas: {self.numero_paginas}")


class Revista(Material):
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, numero_edicion: int):
        # Hereda atributos de la clase base Material usando super()
        super().__init__(titulo, autor, anio_publicacion)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        # Sobrescribe el método para incluir el número de edición
        print(f"[REVISTA] Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion} | Edición: #{self.numero_edicion}")

# Instanciando dos objetos (un Libro y una Revista)

print("--- RESULTADOS DEL EJERCICIO 3 ---")

libro1 = Libro(titulo="Cien Años de Soledad", autor="Gabriel García Márquez", anio_publicacion=1967, numero_paginas=471)
revista1 = Revista(titulo="National Geographic", autor="Varios Autores", anio_publicacion=2023, numero_edicion=150)

# Ejecutar el método mostrar_informacion en ambos objetos
libro1.mostrar_informacion()
revista1.mostrar_informacion()