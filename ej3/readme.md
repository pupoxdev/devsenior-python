Ejercicio Integrador en Python
Sistema de Gestión de una Tienda de Videojuegos
1. Objetivo
Desarrollar un programa en Python que permita administrar el inventario y las ventas de una tienda de videojuegos aplicando:

Variables

Condicionales (if, elif, else)

Ciclos (while, for)

Funciones

Colecciones (diccionarios y listas)

2. Enunciado
Una tienda de videojuegos requiere un sistema para controlar sus productos y ventas.

Cada videojuego almacenará los siguientes datos:

Campo Descripción Código Identificador único Nombre Nombre del videojuego Plataforma PC, PlayStation, Xbox o Nintendo Precio Valor unitario Cantidad Unidades en inventario

Estructura de datos
La información se almacena en un diccionario anidado:

python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    }
}
3. Menú Principal
El programa debe mostrar el siguiente menú de forma repetida hasta que el usuario seleccione salir:

javascript
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
4. Requisitos Funcionales
4.1 Agregar videojuego
Solicitar los datos del videojuego y agregarlo al diccionario.

Validaciones:

El código no puede estar repetido.

El precio y la cantidad deben ser mayores que cero.

4.2 Mostrar inventario
Recorrer el diccionario e imprimir todos los videojuegos registrados.

4.3 Buscar videojuego por código
Solicitar un código y mostrar la información completa del videojuego si existe.

4.4 Actualizar precio
Permitir modificar el precio de un videojuego existente.

4.5 Registrar venta
Entradas:

Código del videojuego

Cantidad a vender

Validaciones:

El videojuego debe existir.

Debe haber inventario suficiente.

Acciones:

Descontar la cantidad del inventario.

Calcular el valor total de la venta.

Mostrar la factura.

4.6 Mostrar estadísticas
Mostrar:

Total de videojuegos registrados.

Valor total del inventario.

Videojuego más costoso.

Videojuego con mayor cantidad disponible.

Promedio de precios.

4.7 Eliminar videojuego
Eliminar un videojuego por su código.

4.8 Salir
Finalizar el programa.

5. Requisitos Técnicos
Funciones obligatorias
python
def agregar_videojuego(videojuegos):
    ...

def mostrar_inventario(videojuegos):
    ...

def buscar_videojuego(videojuegos):
    ...

def actualizar_precio(videojuegos):
    ...

def registrar_venta(videojuegos):
    ...

def mostrar_estadisticas(videojuegos):
    ...

def eliminar_videojuego(videojuegos):
    ...

def menu():
    ...
6. Datos Iniciales de Prueba
python
videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}
7. Ejemplo de Venta
Entrada:

javascript
Ingrese código del videojuego: VG001
Ingrese cantidad a vender: 2
Salida esperada:

javascript
Factura
-------
Juego: FIFA 26
Precio unitario: $250000
Cantidad: 2
Total: $500000
8. Retos Adicionales (Opcionales)