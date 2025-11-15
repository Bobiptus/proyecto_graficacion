import sqlite3
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
                id INTEGER PRIMARY KEY AUTOINCREMENT
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