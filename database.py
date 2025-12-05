import sqlite3

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
    """
    Guarda la canción actual en la base de datos, ELIMINANDO la canción 
    anterior y re-insertando la nueva como ID=1 para mantener la referencia 
    de carga del botón 'Cargar DB (ID 1)'.
    """
    conexion = None
    CANCION_ID_GUARDADA = 1 

    try:
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()

        print(f"Eliminando notas y canción anterior con ID={CANCION_ID_GUARDADA}...")
        cursor.execute("DELETE FROM notas WHERE cancion_id = ?", (CANCION_ID_GUARDADA,))
        cursor.execute("DELETE FROM canciones WHERE id = ?", (CANCION_ID_GUARDADA,))
        
        cursor.execute("PRAGMA foreign_keys = OFF") 
        
        timestamp = int(1)
        nombre_cancion = f"Canción Guardada ({timestamp})"
        
        cursor.execute("INSERT INTO canciones (id, nombre) VALUES (?, ?)", (CANCION_ID_GUARDADA, nombre_cancion))
        
        cursor.execute("PRAGMA foreign_keys = ON")
        
        cancion_id = CANCION_ID_GUARDADA

        for fila in range(len(grid)):
            for columna in range(len(grid[fila])):
                if grid[fila][columna] is not None:
                    cursor.execute(
                        "INSERT INTO notas (cancion_id, fila, columna) VALUES (?, ?, ?)",
                        (cancion_id, fila, columna)
                    )

        conexion.commit()
        print(f"Canción ID={CANCION_ID_GUARDADA} sobreescrita exitosamente.")

    except sqlite3.Error as e:
        print(f"Error al guardar la canción: {e}")

    finally:
        if conexion:
            conexion.close()
            
# ... (el resto del código de database.py)

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
        COLUMNAS = 32
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
