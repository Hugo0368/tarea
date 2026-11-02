# Hugo Alvarez
# Ingeniería en Sistemas
"""
Carné: 0909-26-12678
Nombre del curso: Algoritmos
Nombre del catedrático: M.A. Ing. Amilcar Josimar Sagastume Diaz
Fecha: 31/10/2026
"""


# EJERCICIO 1: Clases, Objetos y Métodos Básicos


class Rectangulo:
    def __init__(self, base: float, altura: float):
        # Atributos inicializados en el constructor
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        # Calcula y retorna el área (base * altura)
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        # Calcula y retorna el perímetro (2*base + 2*altura)
        return (2 * self.base) + (2 * self.altura)

    def es_cuadrado(self) -> bool:
        # Evalúa si base y altura son iguales
        return self.base == self.altura

rectangulo1 = Rectangulo(base=10, altura=5)
rectangulo2 = Rectangulo(base=4, altura=4)

print("--- RESULTADOS DEL EJERCICIO 1 ---")

# Probar objeto 1
print("Rectángulo 1 (10x5):")
print(f"  - Área: {rectangulo1.calcular_area()}")
print(f"  - Perímetro: {rectangulo1.calcular_perimetro()}")
print(f"  - ¿Es cuadrado?: {rectangulo1.es_cuadrado()}\n")

# Probar objeto 2
print("Rectángulo 2 (4x4):")
print(f"  - Área: {rectangulo2.calcular_area()}")
print(f"  - Perímetro: {rectangulo2.calcular_perimetro()}")
print(f"  - ¿Es cuadrado?: {rectangulo2.es_cuadrado()}")