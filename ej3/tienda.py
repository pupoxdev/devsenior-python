# Datos iniciales de prueba 
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

def menu():
    
    print("\n===== TIENDA DE VIDEOJUEGOS =====")
    print("1. Agregar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego por código")
    print("4. Actualizar precio")
    print("5. Registrar venta")
    print("6. Mostrar estadísticas")
    print("7. Eliminar videojuego")
    print("8. Salir")
    
    opcion = input("Seleccione una opción (1-8): ")
    return opcion

def agregar_videojuego(videojuegos):
    print("\n================ AGREGAR VIDEOJUEGO ================")
    codigo = input("Ingrese el código del videojuego (ej. VG004): ").strip().upper()
    
    # Validación 1: Código repetido
    if codigo in videojuegos:
        print(f"\n[Error] El código {codigo} ya está registrado en el inventario.")
        return

    nombre = input("Ingrese el nombre del videojuego: ").strip()
    plataforma = input("Ingrese la plataforma (PC, PlayStation, Xbox, Nintendo): ").strip()

    # Validación 2: Precio (debe ser numérico y mayor que cero)
    try:
        precio = int(input("Ingrese el precio unitario: "))
        if precio <= 0:
            print("\n[Error] El precio debe ser un número mayor a cero.")
            return
    except ValueError:
        print("\n[Error] Entrada no válida. El precio debe ser un número entero.")
        return

    # Validación 3: Cantidad (debe ser numérico y mayor que cero)
    try:
        cantidad = int(input("Ingrese la cantidad inicial en inventario: "))
        if cantidad <= 0:
            print("\n[Error] La cantidad debe ser un número mayor a cero.")
            return
    except ValueError:
        print("\n[Error] Entrada no válida. La cantidad debe ser un número entero.")
        return

    # Si pasa todas las validaciones, se agrega
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"\n[Éxito] Videojuego '{nombre}' agregado correctamente con el código {codigo}.")


def mostrar_inventario(videojuegos):
   
    if not videojuegos:
        print("\nEl inventario está vacío.")
        return
    
    print("\n================ INVENTARIO ================")
    for codigo, datos in videojuegos.items():
        print(f"Código: {codigo}")
        print(f"  Nombre: {datos['nombre']}")
        print(f"  Plataforma: {datos['plataforma']}")
        print(f"  Precio: ${datos['precio']:,}")  
        print(f"  Cantidad disponible: {datos['cantidad']}")
        print("-" * 44)

def buscar_videojuego(videojuegos):
    codigo = input("\nIngrese el código del videojuego a buscar (ej. VG001): ").strip().upper()
    
    if codigo in videojuegos:
        juego = videojuegos[codigo]
        print(f"\n================ JUEGO ENCONTRADO ================")
        print(f"Código: {codigo}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Plataforma: {juego['plataforma']}")
        print(f"Precio: ${juego['precio']:,}")
        print(f"Cantidad en Inventario: {juego['cantidad']}")
        print("==================================================")
    else:
        print(f"\n[Error] El videojuego con código {codigo} no existe en el inventario.")


def actualizar_precio(videojuegos):
    print("\n================ ACTUALIZAR PRECIO ================")
    codigo = input("Ingrese el código del videojuego (ej. VG001): ").strip().upper()
    
    # Verificar si existe el videojuego
    if codigo not in videojuegos:
        print(f"\n[Error] El videojuego con código {codigo} no existe.")
        return
        
    juego = videojuegos[codigo]
    print(f"Videojuego: {juego['nombre']}")
    print(f"Precio actual: ${juego['precio']:,}")
    
    # Solicitar y validar el nuevo precio
    try:
        nuevo_precio = int(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("\n[Error] El precio debe ser mayor a cero.")
            return
    except ValueError:
        print("\n[Error] Entrada no válida. El precio debe ser un número entero.")
        return
        
    # Actualizar el precio en el diccionario
    juego["precio"] = nuevo_precio
    print(f"\n[Éxito] El precio del videojuego '{juego['nombre']}' se ha actualizado a ${nuevo_precio:,}.")


def registrar_venta(videojuegos):
    print("\n================ REGISTRAR VENTA ================")
    codigo = input("Ingrese el código del videojuego: ").strip().upper()
    
    # 1. Validar existencia
    if codigo not in videojuegos:
        print(f"\n[Error] El videojuego con código {codigo} no existe.")
        return
        
    juego = videojuegos[codigo]
    
    # 2. Validar cantidad a vender (mayor a cero)
    try:
        cantidad_vender = int(input(f"Ingrese la cantidad a vender (Disponibles: {juego['cantidad']}): "))
        if cantidad_vender <= 0:
            print("\n[Error] La cantidad a vender debe ser mayor a cero.")
            return
    except ValueError:
        print("\n[Error] Entrada no válida. La cantidad debe ser un número entero.")
        return
        
    # 3. Validar inventario suficiente
    if cantidad_vender > juego["cantidad"]:
        print(f"\n[Error] No hay stock suficiente. Solo quedan {juego['cantidad']} unidades disponibles.")
        return
        
    # 4. Procesar la venta
    juego["cantidad"] -= cantidad_vender
    total = cantidad_vender * juego["precio"]
    
    # 5. Mostrar Factura
    print("\nFactura")
    print("-------")
    print(f"Juego: {juego['nombre']}")
    print(f"Precio unitario: ${juego['precio']}")
    print(f"Cantidad: {cantidad_vender}")
    print(f"Total: ${total}")
    print("-------------------------------------------------")


def mostrar_estadisticas(videojuegos):
    print("\n================ ESTADÍSTICAS ================")
    
    total_juegos = len(videojuegos)
    if total_juegos == 0:
        print("No hay videojuegos registrados para generar estadísticas.")
        return
        
    valor_total_inventario = 0
    suma_precios = 0
    
    
    juego_mas_costoso = ""
    precio_maximo = -1
    
   
    juego_mas_cantidad = ""
    cantidad_maxima = -1
    
    # Recorrido para calcular acumulados y máximos
    for codigo, datos in videojuegos.items():
        nombre = datos["nombre"]
        precio = datos["precio"]
        cantidad = datos["cantidad"]
        
        # 1. Acumular el valor total de inventario
        valor_total_inventario += precio * cantidad
        
        # 2. Acumular los precios para el promedio
        suma_precios += precio
        
        # 3. Evaluar si es el más costoso
        if precio > precio_maximo:
            precio_maximo = precio
            juego_mas_costoso = nombre
            
        # 4. Evaluar si tiene la mayor cantidad disponible
        if cantidad > cantidad_maxima:
            cantidad_maxima = cantidad
            juego_mas_cantidad = nombre
            
    promedio_precios = suma_precios / total_juegos
    
    # Mostrar resultados
    print(f"Total de videojuegos registrados: {total_juegos}")
    print(f"Valor total del inventario:       ${valor_total_inventario:,}")
    print(f"Videojuego más costoso:           {juego_mas_costoso} (${precio_maximo:,})")
    print(f"Mayor cantidad disponible:        {juego_mas_cantidad} ({cantidad_maxima} unidades)")
    print(f"Promedio de precios:              ${promedio_precios:,.2f}")
    print("==============================================")


def eliminar_videojuego(videojuegos):
    print("\n================ ELIMINAR VIDEOJUEGO ================")
    codigo = input("Ingrese el código del videojuego a eliminar: ").strip().upper()
    
    # Verificar si existe antes de intentar eliminarlo
    if codigo in videojuegos:
        nombre_juego = videojuegos[codigo]["nombre"]
        
        # Eliminar el elemento del diccionario
        del videojuegos[codigo]
        
        print(f"\n[Éxito] El videojuego '{nombre_juego}' con código {codigo} ha sido eliminado del inventario.")
    else:
        print(f"\n[Error] El videojuego con código {codigo} no existe en el inventario.")


def main():
   
    while True:
        opcion = menu()
        
        if opcion == "1":
            agregar_videojuego(videojuegos)
        elif opcion == "2":
            mostrar_inventario(videojuegos)
        elif opcion == "3":
            buscar_videojuego(videojuegos)
        elif opcion == "4":
            actualizar_precio(videojuegos)
        elif opcion == "5":
            registrar_venta(videojuegos)
        elif opcion == "6":
            mostrar_estadisticas(videojuegos)
        elif opcion == "7":
            eliminar_videojuego(videojuegos)
        elif opcion == "8":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
