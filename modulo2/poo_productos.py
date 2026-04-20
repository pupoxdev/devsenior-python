"""
Mini proyecto: Sistema de gestión de productos
Objetivo

Crear un programa orientado a objetos que permita:

Crear productos
Mostrar productos
Buscar productos
Actualizar precio y stock
Vender productos
Eliminar productos
Conceptos que se trabajan
Clases y objetos
Constructor
Encapsulamiento
Getters y setters
Métodos
Listas de objetos
"""

class Producto:
    def __init__ (self, codigo, nombre, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        
#Getters

    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio    
    
    def get_stock(self):
        return self.__stock
    
#Setters
    def set_codgo(self, codigo):
        self.__codigo = codigo
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_precio(self, precio):
        self.__precio = precio
        
    def set_stock(self, stock):
        self.__stock = stock
        
#Metodo mostrar producto
    def mostrar_producto(self):
        print(f"Codigo: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Stock: {self.__stock}")
        print("-" * 20)
        
#Clase principal para gestionar los productos
def main():
    