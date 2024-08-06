'''
##############################

Desafío 3: Sistema de Gestión de Tareas
Objetivo: Desarrollar un sistema para organizar y administrar tareas personales o de equipo.

Requisitos:

    Crear una clase base Tarea con atributos como descripción, fecha de vencimiento, estado 
    (pendiente, en progreso, completada), etc.

    Definir al menos 2 clases derivadas para diferentes tipos de tareas 
    (por ejemplo, TareaSimple, TareaRecurrente) con atributos y métodos específicos.

    Implementar operaciones CRUD para gestionar las tareas.

    Manejar errores con bloques try-except para validar entradas y gestionar excepciones.

    Persistir los datos en archivo JSON.

##############################
'''
import json
from datetime import datetime

class Tarea:
    def __init__(self, descripcion, fecha_vencimiento, estado='pendiente'):
        self.descripcion = descripcion
        self.fecha_vencimiento = self.validar_fecha(fecha_vencimiento)
        self.estado = estado

    def validar_fecha(self, fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
            return fecha
        except ValueError:
            raise ValueError("Formato de fecha incorrecto, debe ser YYYY-MM-DD")

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "fecha_vencimiento": self.fecha_vencimiento.strftime('%Y-%m-%d'),
            "estado": self.estado
        }

    def __str__(self):
        return f"{self.descripcion} (Vence: {self.fecha_vencimiento.strftime('%Y-%m-%d')}) - Estado: {self.estado}"

class TareaSimple(Tarea):
    def __init__(self, descripcion, fecha_vencimiento, estado='pendiente'):
        super().__init__(descripcion, fecha_vencimiento, estado)

class TareaRecurrente(Tarea):
    def __init__(self, descripcion, fecha_vencimiento, frecuencia, estado='pendiente'):
        super().__init__(descripcion, fecha_vencimiento, estado)
        self.frecuencia = frecuencia

    def to_dict(self):
        data = super().to_dict()
        data["frecuencia"] = self.frecuencia
        return data

    def __str__(self):
        return f"{super().__str__()} - Frecuencia: {self.frecuencia}"

class GestionTareas:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_tarea(self, tarea):
        try:
            datos = self.leer_datos()
            descripcion = tarea.descripcion
            if descripcion not in datos:
                datos[descripcion] = tarea.to_dict()
                self.guardar_datos(datos)
                print(f'Tarea guardada exitosamente')
            else:
                print(f'La tarea con descripción "{descripcion}" ya existe')
        except Exception as error:
            print(f'Error inesperado al crear tarea: {error}')

    def leer_tarea(self, descripcion):
        try:
            datos = self.leer_datos()
            tarea = datos.get(descripcion)
            if tarea:
                print(f"Tarea encontrada: {tarea}")
            else:
                print(f"No se encontró la tarea con descripción: {descripcion}")
        except Exception as error:
            print(f'Error al leer la tarea: {error}')

    def actualizar_tarea(self, descripcion, nuevo_estado):
        try:
            datos = self.leer_datos()
            if descripcion in datos:
                datos[descripcion]['estado'] = nuevo_estado
                self.guardar_datos(datos)
                print(f'Tarea actualizada exitosamente')
            else:
                print(f'No se encontró la tarea con descripción: {descripcion}')
        except Exception as error:
            print(f'Error al actualizar la tarea: {error}')

    def eliminar_tarea(self, descripcion):
        try:
            datos = self.leer_datos()
            if descripcion in datos:
                del datos[descripcion]
                self.guardar_datos(datos)
                print(f'Tarea eliminada exitosamente')
            else:
                print(f'No se encontró la tarea con descripción: {descripcion}')
        except Exception as error:
            print(f'Error al eliminar la tarea: {error}')
