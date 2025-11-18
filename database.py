import sqlite3
import pygame
import time
from datetime import datetime

def crear_tablas():
    """Crea las tablas necesarias en la base de datos SQLite."""
    conexion = None
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()

        # Crear tabla de canciones
        sql_crear_tabla_canciones = """
            CREATE TABLE IF NOT EXISTS canciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
        );
            """
        cursor.execute(sql_crear_tabla_canciones)

        sql_crear_tabla_notas = """
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cancion_id INTEGER NOT NULL,
                fila INTEGER NOT NULL,
                columna INTEGER NOT NULL,
                FOREIGN KEY (cancion_id) REFERENCES canciones(id)
            );
            """
        cursor.execute(sql_crear_tabla_notas)

        conexion.commit()
        print("Tablas creadas exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al crear las tablas: {e}")

    finally:
        if conexion:
            conexion.close()

def guardar_cancion(grid):
    """Guarda la canción actual en la base de datos."""
    conexion = None
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()

        # Insertar nueva canción
        timestamp = int(time.time())  # ej: 1701234567
        cursor.execute("INSERT INTO canciones (nombre) VALUES (?)", (f"Canción {timestamp}",))
        cancion_id = cursor.lastrowid

        # Insertar notas
        for fila in range(len(grid)):
            for columna in range(len(grid[fila])):
                if grid[fila][columna] is not None:
                    cursor.execute(
                        "INSERT INTO notas (cancion_id, fila, columna) VALUES (?, ?, ?)",
                        (cancion_id, fila, columna)
                    )

        conexion.commit()
        print("Canción guardada exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al guardar la canción: {e}")

    finally:
        if conexion:
            conexion.close()

def cargar_cancion(cancion_id):
    """Carga una canción desde la base de datos."""
    conexion = None
    grid = None
    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()

        # Obtener notas de la canción
        cursor.execute("SELECT fila, columna FROM notas WHERE cancion_id = ?", (cancion_id,))
        notas = cursor.fetchall()

        # Inicializar grid vacío
        FILAS = 7
        COLUMNAS = 16
        grid = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

        # Llenar grid con las notas obtenidas
        for fila, columna in notas:
            grid[fila][columna] = {'fila': fila, 'bounce':0}

        print("Canción cargada exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al cargar la canción: {e}")

    finally:
        if conexion:
            conexion.close()
    
    return grid