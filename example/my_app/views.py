from django.shortcuts import render

# Create your views here.
class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Disponibilidad: {self.disponibilidad} unidades")

    def actualizar_disponibilidad(self, cantidad):
        self.disponibilidad -= cantidad

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, disponibilidad, marca, modelo, garantia):
        super().__init__(nombre, precio, disponibilidad)
        self.marca = marca
        self.modelo = modelo
        self.garantia = garantia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Garantía: {self.garantia} meses")

    def registrar_garantia(self):
        print(f"La garantía del {self.nombre} ha sido registrada por {self.garantia} meses")