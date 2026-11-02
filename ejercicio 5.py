# Hugo Alvarez
# Ingeniería en Sistemas
"""
Carné: 0909-26-12678
Nombre del curso: Algoritmos
Nombre del catedrático: M.A. Ing. Amilcar Josimar Sagastume Diaz
Fecha: 31/10/2026
"""

# EJERCICIO 5: Composición y Relación entre Clases

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_stock: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def actualizar_stock(self, cantidad: int):
        # Resta o suma a la cantidad disponible
        self.cantidad_stock += cantidad

class CarritoCompras:
    def __init__(self):
        # Lista vacía que almacenará los artículos agregados
        self.productos = []

    def agregar_producto(self, producto: Producto, cantidad: int):
        # Valida que haya suficiente stock en el objeto Producto
        if cantidad <= producto.cantidad_stock:
            self.productos.append({'producto': producto, 'cantidad': cantidad})
            producto.actualizar_stock(-cantidad)  # Reduce el stock del producto original
            print(f"Agregado con éxito: {cantidad}x {producto.nombre}")
        else:
            print(f"Error: Stock insuficiente de {producto.nombre}. Disponible: {producto.cantidad_stock}")

    def calcular_total(self) -> float:
        total = 0.0
        for item in self.productos:
            total += item['producto'].precio * item['cantidad']
        return total

    def mostrar_resumen(self):
        print("\n--- RESUMEN DE COMPRA ---")
        for item in self.productos:
            prod = item['producto']
            cant = item['cantidad']
            subtotal = prod.precio * cant
            print(f"- {cant}x {prod.nombre} | Precio unitario: Q{prod.precio:.2f} | Subtotal: Q{subtotal:.2f}")
        print(f"TOTAL A PAGAR: Q{self.calcular_total():.2f}")

print("--- RESULTADOS DEL EJERCICIO 5 ---")

# tres objetos Producto diferentes
laptop = Producto(nombre="Laptop HP", precio=5500.0, cantidad_stock=4)
mouse = Producto(nombre="Mouse Gamer", precio=250.0, cantidad_stock=10)
teclado = Producto(nombre="Teclado Mecánico", precio=400.0, cantidad_stock=2)

mi_carrito = CarritoCompras()

mi_carrito.agregar_producto(laptop, 1)
mi_carrito.agregar_producto(mouse, 2)
mi_carrito.agregar_producto(teclado, 5)  

mi_carrito.mostrar_resumen()

print("\n--- STOCK RESTANTE EN INVENTARIO ---")
print(f"Stock restante de {laptop.nombre}: {laptop.cantidad_stock}")
print(f"Stock restante de {mouse.nombre}: {mouse.cantidad_stock}")
print(f"Stock restante de {teclado.nombre}: {teclado.cantidad_stock}")