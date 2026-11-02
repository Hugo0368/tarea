# Hugo Alvarez
# Ingeniería en Sistemas
"""
Carné: 0909-26-12678
Nombre del curso: Algoritmos
Nombre del catedrático: M.A. Ing. Amilcar Josimar Sagastume Diaz
Fecha: 31/10/2026
"""

# EJERCICIO 2: Encapsulamiento y Validaciones

class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        # Atributo privado __saldo (no se puede modificar directamente desde afuera)
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0.0

    def depositar(self, cantidad: float):
        # Valida que la cantidad a depositar sea mayor a 0
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso de Q{cantidad:.2f} a la cuenta de {self.titular}.")
        else:
            print("Error: La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad: float):
        # Valida que la cantidad sea mayor a 0 y que haya saldo suficiente
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser mayor a 0.")
        elif cantidad > self.__saldo:
            print(f"Error: Fondos insuficientes en la cuenta de {self.titular}. Saldo actual: Q{self.__saldo:.2f}")
        else:
            self.__saldo -= cantidad
            print(f"Retiro exitoso de Q{cantidad:.2f} de la cuenta de {self.titular}.")

    def consultar_saldo(self) -> float:
        # Método de acceso para obtener el saldo privado de forma segura
        return self.__saldo

# Instanciando dos objetos (cuentas) diferentes

print("\n--- RESULTADOS DEL EJERCICIO 2 ---")

# Objeto 1: Cuenta de Hugo Alvarez
cuenta1 = CuentaBancaria(titular="Hugo Alvarez", saldo_inicial=500.0)
cuenta1.depositar(200.0)      # Depósito válido
cuenta1.retirar(1000.0)      # Intento de retiro mayor al saldo (debe mostrar mensaje de error)
print(f"Saldo final de {cuenta1.titular}: Q{cuenta1.consultar_saldo():.2f}\n")

# Objeto 2: Cuenta de María López
cuenta2 = CuentaBancaria(titular="María López", saldo_inicial=100.0)
cuenta2.retirar(50.0)         # Retiro válido
print(f"Saldo final de {cuenta2.titular}: Q{cuenta2.consultar_saldo():.2f}")