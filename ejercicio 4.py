# Hugo Alvarez
# Ingeniería en Sistemas
"""
Carné: 0909-26-12678
Nombre del curso: Algoritmos
Nombre del catedrático: M.A. Ing. Amilcar Josimar Sagastume Diaz
Fecha: 31/10/2026
"""

# EJERCICIO 4: Polimorfismo y Arreglos de Objetos

class Empleado:
    def __init__(self, nombre: str, dpi: str):
        self.nombre = nombre
        self.dpi = dpi

    def calcular_salario(self) -> float:
        # Método que retorna 0 por defecto en la clase base
        return 0.0

class EmpleadoFijo(Empleado):
    def __init__(self, nombre: str, dpi: str, sueldo_base: float):
        super().__init__(nombre, dpi)
        self.sueldo_base = sueldo_base

    def calcular_salario(self) -> float:
        # Retorna el sueldo fijo
        return self.sueldo_base

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre: str, dpi: str, tarifa_por_hora: float, horas_trabajadas: float):
        super().__init__(nombre, dpi)
        self.tarifa_por_hora = tarifa_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self) -> float:
        # Retorna multiplicación de tarifa por horas
        return self.tarifa_por_hora * self.horas_trabajadas

# PRUEBAS DEL EJERCICIO 4

print("--- RESULTADOS DEL EJERCICIO 4 ---")

# Lista que contiene diferentes tipos de empleados (Arreglo de Objetos)
lista_empleados = [
    EmpleadoFijo(nombre="Hugo Alvarez", dpi="1234567890101", sueldo_base=4500.0),
    EmpleadoPorHora(nombre="Carlos Ruiz", dpi="9876543210101", tarifa_por_hora=30.0, horas_trabajadas=160),
    EmpleadoFijo(nombre="María López", dpi="5554443330101", sueldo_base=5200.0)
]

# Recorrer la lista con un ciclo for y aplicar Polimorfismo
for emp in lista_empleados:
    print(f"Empleado: {emp.nombre} (DPI: {emp.dpi}) | Salario Final: Q{emp.calcular_salario():.2f}")