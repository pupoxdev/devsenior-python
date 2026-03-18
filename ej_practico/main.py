# 1️⃣ Registrar estudiantes
# 2️⃣ Calcular el promedio de tres notas
# 3️⃣ Determinar el estado del estudiante
# 4️⃣ Permitir registrar varios estudiantes usando un menú
# 5️⃣ Mostrar un resumen final


def pedir_edad_valida():
    while True:

        edad = int(input("Ingrese la edad: "))
        if edad > 0:
            return edad
        print("Edad inválida. Debe ser mayor que 0.")


def pedir_nota_valida(numero_nota):

    while True:

        nota = float(input(f"Ingrese nota {numero_nota}: "))
        if 0 <= nota <= 5:
            return nota
        print("Nota inválida. Debe estar entre 0 y 5.")


def registrar_estudiante():
    name = input("Ingresa tu nombre : ")
    age = pedir_edad_valida()
    note1 = pedir_nota_valida(1)
    note2 = pedir_nota_valida(2)
    note3 = pedir_nota_valida(3)
    return name, age, note1, note2, note3


def calcular_promedio(note1, note2, note3):
    prom = (note1 + note2 + note3) / 3
    return prom


def evaluar_estado(prom):

    if prom >= 4.0:
        return "Aprobado"
    if prom >= 3.0:
        return "En recuperación"
    return "Reprobado"


def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Registrar estudiante")
    print("2. Salir ")

estudiantes = []
while True:
    
    mostrar_menu()
    opcion = int(input("Selecciona una opción (1 o 2)): "))

    if opcion == 1:

        name, age, note1, note2, note3 = registrar_estudiante()
        promedio = calcular_promedio(note1, note2, note3)
        estado = evaluar_estado(promedio)

        estudiantes.append(
            {
                "nombre": name,
                "edad": age,
                "promedio": promedio,
                "estado": estado,
            }
        )

        print(f"\nPromedio del estudiante: {promedio:.2f}")
        print(f"Estado académico: {estado}")

    elif opcion == 2:
        print("\n===== RESUMEN FINAL =====")
        total = len(estudiantes)
        print(f"Total de estudiantes registrados: {total}")

        promedio_general = 0

        if total > 0:
            suma_promedios = 0
            for estudiante in estudiantes:
                suma_promedios += estudiante["promedio"]
            promedio_general = suma_promedios / total
        else:
            promedio_general = 0.0

        print(f"Promedio general del grupo: {promedio_general:.2f}")
        print("Saliendo del programa... ¡Adiós!")

        print("\nSaliendo del programa... ¡Adiós!")
        break
    else:
        print("\nOpción inválida, intenta de nuevo.")
