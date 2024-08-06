import os
import platform

from Desafio3 import (
    TareaSimple,
    TareaRecurrente,
    GestionTareas
)

def limpiar_pantalla():
    # Limpiar la pantalla según el sistema operativo
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  # Linux/Unix/MacOS

def mostrar_menu():
    print("========== Menú de gestión de tareas ===========")
    print('1. Agregar Tarea Simple')
    print('2. Agregar Tarea Recurrente')
    print('3. Mostrar Tarea')
    print('4. Actualizar Tarea')
    print('5. Eliminar Tarea')
    print('6. Salir')

def agregar_tarea(gestion, tipo_tarea):
    try:
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")

        if tipo_tarea == '1':
            tarea = TareaSimple(descripcion, fecha_vencimiento)
        elif tipo_tarea == '2':
            frecuencia = input("Ingrese la frecuencia de la tarea recurrente: ")
            tarea = TareaRecurrente(descripcion, fecha_vencimiento, frecuencia)
        else:
            print("Opción inválida.")
            return

        gestion.crear_tarea(tarea)
        input('Presione Enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f"Error inesperado: {e}")

def buscar_tarea_por_descripcion(gestion):
    descripcion = input("Ingrese la descripción de la tarea a buscar: ")
    gestion.leer_tarea(descripcion)

def actualizar_estado_tarea(gestion):
    descripcion = input("Ingrese la descripción de la tarea a actualizar: ")
    nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
    gestion.actualizar_tarea(descripcion, nuevo_estado)

def eliminar_tarea_por_descripcion(gestion):
    descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
    gestion.eliminar_tarea(descripcion)

if __name__ == "__main__":
    archivo_tareas = 'tareas.json'
    Desafio3 = GestionTareas(archivo_tareas)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_tarea(Desafio3, opcion)
        elif opcion == '3':
            buscar_tarea_por_descripcion(Desafio3)
        elif opcion == '4':
            actualizar_estado_tarea(Desafio3)
        elif opcion == '5':
            eliminar_tarea_por_descripcion(Desafio3)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")
        input('Presione Enter para continuar...')
