
def limpiar_grid(grid):
    """Limpia todo el contenido de la cuadrícula."""
    # Asume que el grid tiene 7 filas.
    for f in range(len(grid)):
        for c in range(len(grid[f])):
            grid[f][c] = None
    return grid

def cargar_escala_de_prueba(grid):
    """Carga una escala sencilla para probar la funcionalidad del sistema."""
    grid = limpiar_grid(grid)
    print("Cargando: Escala de Prueba Súper Sencilla con Bounce...")
    bounce_init = 0
    
    # 1. Ascendente (Columnas 0, 2, 4, 6)
    grid[3][0] = {'fila': 3, 'bounce': bounce_init} # C3
    grid[2][2] = {'fila': 2, 'bounce': bounce_init} # E4
    grid[1][4] = {'fila': 1, 'bounce': bounce_init} # G#4
    grid[0][6] = {'fila': 0, 'bounce': bounce_init} # C5
    
    # 2. Descendente (Columnas 8, 10, 12, 14)
    grid[1][8] = {'fila': 1, 'bounce': bounce_init}  # G#4
    grid[2][10] = {'fila': 2, 'bounce': bounce_init} # E4
    grid[3][12] = {'fila': 3, 'bounce': bounce_init} # C3
    grid[5][14] = {'fila': 5, 'bounce': bounce_init} # E2

    # RITMO/PULSO (Fila 6: C1)
    for col in range(0, 16, 4):
        grid[6][col] = {'fila': 6, 'bounce': bounce_init}
    
    return grid, 0.20

def cargar_deck_the_halls_robotico(grid):
    """Carga la versión robótica de Deck the Halls (32 columnas)."""
    grid = limpiar_grid(grid)
    print("Cargando: Deck the Halls (Robótico)...")
    bounce_init = 0
    
    # MELODÍA (Fila 3: C3, Fila 2: E4)
    # Frase 1: C-E-C-E | C-E-C
    grid[3][0] = {'fila': 3, 'bounce': bounce_init} 
    grid[2][2] = {'fila': 2, 'bounce': bounce_init} 
    grid[3][4] = {'fila': 3, 'bounce': bounce_init} 
    grid[2][6] = {'fila': 2, 'bounce': bounce_init} 
    
    grid[3][8] = {'fila': 3, 'bounce': bounce_init} 
    grid[2][10] = {'fila': 2, 'bounce': bounce_init}
    grid[3][12] = {'fila': 3, 'bounce': bounce_init}
    
    # Final de la Frase (Saltos Robóticos)
    grid[0][14] = {'fila': 0, 'bounce': bounce_init} # C5 
    grid[3][15] = {'fila': 3, 'bounce': bounce_init} # C3 

    # Repetición de la Frase 
    grid[3][16] = {'fila': 3, 'bounce': bounce_init} 
    grid[2][18] = {'fila': 2, 'bounce': bounce_init} 
    grid[3][20] = {'fila': 3, 'bounce': bounce_init}
    grid[2][22] = {'fila': 2, 'bounce': bounce_init}
    
    grid[3][24] = {'fila': 3, 'bounce': bounce_init}
    grid[2][26] = {'fila': 2, 'bounce': bounce_init}
    
    # Cierre de 4 Tiempos
    grid[3][28] = {'fila': 3, 'bounce': bounce_init}
    grid[2][29] = {'fila': 2, 'bounce': bounce_init}
    grid[1][30] = {'fila': 1, 'bounce': bounce_init} # G#4 
    grid[3][31] = {'fila': 3, 'bounce': bounce_init}

    # BAJO Y CONTRATIEMPO
    # Fila 6 (C1): Pulso de bajo constante 
    for col in range(0, 32, 4):
        grid[6][col] = {'fila': 6, 'bounce': bounce_init}
        
    # Fila 5 (E2): Contratiempo 
    for col in range(2, 32, 4):
        grid[5][col] = {'fila': 5, 'bounce': bounce_init}

    return grid, 0.18

# EN canciones.py

def cargar_cancion_lenta(grid):
    """
    Carga una cancion lenta de prueba.
    Patrón basado en C y E.
    """
    grid = limpiar_grid(grid)
    print("Cargando: We Wish You a Merry Christmas (Robótico)...")
    bounce_init = 0
    
    # --- MELODÍA (Fila 3: C3, Fila 2: E4, Fila 0: C5) ---
    # Patrón: C-E-C-E (We wish you a...)
    
    # Frase 1 (C3-E4-C3-E4)
    grid[3][0] = {'fila': 3, 'bounce': bounce_init} # C3
    grid[2][2] = {'fila': 2, 'bounce': bounce_init} # E4
    grid[3][4] = {'fila': 3, 'bounce': bounce_init} # C3
    grid[2][6] = {'fila': 2, 'bounce': bounce_init} # E4
    
    # Frase 2 (C5-G#4-E4-C3) Cierre con G#
    grid[0][8] = {'fila': 0, 'bounce': bounce_init}  # C5 (Salto de octava)
    grid[1][10] = {'fila': 1, 'bounce': bounce_init} # G#4 (Armonía)
    grid[2][12] = {'fila': 2, 'bounce': bounce_init} # E4
    grid[3][14] = {'fila': 3, 'bounce': bounce_init} # C3
    
    # Repetición de la Frase 1 (x2)
    for offset in [16, 24]:
        grid[3][offset + 0] = {'fila': 3, 'bounce': bounce_init} 
        grid[2][offset + 2] = {'fila': 2, 'bounce': bounce_init} 
        grid[3][offset + 4] = {'fila': 3, 'bounce': bounce_init} 
        grid[2][offset + 6] = {'fila': 2, 'bounce': bounce_init}

    # --- BAJO Y PULSO (Fila 6: C1, Fila 5: E2) ---
    # Ritmo binario robótico
    for col in range(0, 32, 2):
        if col % 4 == 0:
            # Bajo pesado C1
            grid[6][col] = {'fila': 6, 'bounce': bounce_init} 
        else:
            # Bajo ligero E2 (contratiempo)
            grid[5][col] = {'fila': 5, 'bounce': bounce_init} 
            
    return grid, 0.20

# EN canciones.py

def cargar_cancion_rapida(grid):
    """
    Carga una cancion rapida de prueba.
    Utiliza el arpegio C-E-G# para un efecto de chiptune agresivo.
    """
    grid = limpiar_grid(grid)
    print("Cargando: Wily's Castle (Megaman II) - 8-bit Robótico...")
    bounce_init = 0
    
    # --- Secuencia principal (Arpegio C5 - G#4 - E4 - C5/C3) ---
    
    # El patrón de 8 beats es: C5, G#4, E4, C5, E4, G#4, C5, C3 (Rápido y tenso)
    # Filas: 0, 1, 2, 0, 2, 1, 0, 3
    pattern_notes = [0, 1, 2, 0, 2, 1, 0, 3] 
    
    for beat in range(0, 32, 8):
        # Aplicamos el patrón en bloques de 8 columnas
        for i in range(8):
            grid[pattern_notes[i]][beat + i] = {'fila': pattern_notes[i], 'bounce': bounce_init}
        

    # --- BAJO PULSANTE (Fila 6: C1, Fila 4: G#2) ---
    # Bajo estable y agresivo, utilizando la nota G#2 (Fila 4) para la tensión
    for col in range(0, 32, 4):
        # Bajo pesado C1 (Tiempos fuertes)
        grid[6][col] = {'fila': 6, 'bounce': bounce_init} 
    
    # Bajo armónico G#2 (Tiempos débiles/tensión)
    for col in range(2, 32, 4):
        grid[4][col] = {'fila': 4, 'bounce': bounce_init} 
        
    return grid, 0.12 # Devuelve el grid y el tiempo por beat (MUY RÁPIDO)