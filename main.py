"""
Proyecto final para la materia de Graficación por computadora del Instituto Tecnológico de Ensenada (ITE)
Autor: Armando Roberto Pérez Banda
Matrícula: 24760228
Descripción: Secuenciador musical básico que permite al usuario crear patrones rítmicos y melódicos interactuando con una cuadrícula visual.

Programa realizado en Python 3.10 para mas información revisar el archivo README.md
"""

import pygame
from grid import inicializar_grid, dibujar_grid, mouse_a_grid, toggle_nota
from orquesta import cargar_sonido, reproducir_sonido_en_canal
from botones import crear_boton, dibujar_boton, mouse_sobre_boton
from personaje import dibujar_prota, cargar_sprite_prota
from database import crear_tablas, cargar_cancion, guardar_cancion
from canciones import cargar_deck_the_halls_robotico, cargar_escala_de_prueba, cargar_cancion_lenta, cargar_cancion_rapida

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(16) 
pygame.font.init()
fuente_botones = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((1800, 600))
pygame.display.set_caption("Secuenciador Musical")
clock = pygame.time.Clock()

SPRITE_NOTAS = [
    pygame.transform.scale(pygame.image.load("imagenes/beep.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("imagenes/mouse.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("imagenes/coin.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("imagenes/drop.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("imagenes/organ.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("imagenes/ghost.png"), (30, 30)),
    pygame.transform.scale(pygame.image.load("imagenes/drum.png"), (30, 30))
]

# Se declaran los sonidos utilizados
sonidos = [
    cargar_sonido("sounds/sq_agudo2.wav", 1),
    cargar_sonido("sounds/sq_alto2.wav", 1),
    cargar_sonido("sounds/sq_medio2.wav", 1),
    cargar_sonido("sounds/tri_agudo2.wav", 1),
    cargar_sonido("sounds/tri_medio2.wav", 1),
    cargar_sonido("sounds/tri_grave2.wav", 1),
    cargar_sonido("sounds/noise_snare2.wav", 1)
]
sprite_prota = cargar_sprite_prota("imagenes/MAESTRO.png")

# CONFIGURACIÓN DEL GRID
GRID_FILAS = 7
GRID_COLUMNAS = 32
CELDA_ANCHO = 50
CELDA_ALTO = 60
GRID_INICIO_X = 100
GRID_INICIO_Y = 150

# COLORES DE BOTONES
COLOR_VERDE = (100, 255, 100)
COLOR_NEGRO = (50, 50, 50)
COLOR_BLANCO = (255, 255, 255)

# INICIALIZAR GRID
grid = inicializar_grid(GRID_FILAS, GRID_COLUMNAS)
config_grid = {
    'inicio_x': GRID_INICIO_X,
    'inicio_y': GRID_INICIO_Y,
    'ancho_celda': CELDA_ANCHO,
    'alto_celda': CELDA_ALTO,
    'filas': GRID_FILAS,
    'columnas': GRID_COLUMNAS,
    'grid': grid
}

# ESTADO DE REPRODUCCIÓN
reproduciendo = False
columna_actual = 0
tiempo_por_beat = 0.20
tiempo_acumulado = 0

# CREAR BOTONES
botones = [
    crear_boton(100, 2, 40, 40, "Play", (0, 150, 0), (0, 200, 0), "play", "imagenes/PLAY.png"),
    crear_boton(180, 2, 40, 40, "Stop", (150, 0, 0), (200, 0, 0), "stop", "imagenes/STOP.png"),
    crear_boton(260, 2, 40, 40, "Clear", (0, 0, 150), (0, 0, 200), "clear", "imagenes/ERASER.png"),
    crear_boton(340, 2, 40, 40, "Guardar", (150, 150, 0), (200, 200, 0), "guardar", "imagenes/SAVE.png"),
    crear_boton(420, 2, 40, 40, "Cargar", (0, 150, 150), (0, 200, 200), "cargar", "imagenes/LOAD.png"),
    crear_boton(500, 2, 40, 40, "Salir", (200, 0, 0), (255, 50, 50), "salir", "imagenes/EXIT.png"),

    crear_boton(600, 2, 200, 50, "Deck The Halls", COLOR_NEGRO, COLOR_VERDE, 'cargar_deck_the_halls', None),
    crear_boton(820, 2, 200, 50, "Prueba", COLOR_NEGRO, COLOR_VERDE, 'cargar_escala_prueba', None),
    crear_boton(1040, 2, 200, 50, "Canción lenta", COLOR_NEGRO, COLOR_VERDE, 'cargar_cancion_lenta', None),
    crear_boton(1260, 2, 200, 50, "Canción rápida", COLOR_NEGRO, COLOR_VERDE, 'cargar_cancion_rapida', None)
]

# CREAR TABLAS EN LA BASE DE DATOS
crear_tablas()

# COMIENZA EL BUCLE PRINCIPAL
running = True
dt = 0

while running:
    # EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Verificar si dio click en algún botón
            click_en_boton = False
            for boton in botones:
                if mouse_sobre_boton(mouse_x, mouse_y, boton):
                    click_en_boton = True
                    
                    if boton['accion'] == "play":
                        reproduciendo = True
                        columna_actual = 0
                        tiempo_acumulado = 0
                    
                    elif boton['accion'] == "stop":
                        reproduciendo = False
                        pygame.mixer.stop()
                        columna_actual = 0
                    
                    elif boton['accion'] == "clear":
                        grid = inicializar_grid(GRID_FILAS, GRID_COLUMNAS)
                        config_grid['grid'] = grid

                    elif boton['accion'] == "guardar":
                        guardar_cancion(grid)

                    elif boton['accion'] == "salir":
                        quit()
                    
                    elif boton['accion'] == "cargar":
                        grid_cargado = cargar_cancion(1)
                        if grid_cargado is not None:
                            grid = grid_cargado
                            config_grid['grid'] = grid
                    
                    elif boton['accion'] == 'cargar_db':
                        nuevo_grid = cargar_cancion(1)
                        if nuevo_grid is not None:
                            grid = nuevo_grid
                            config_grid['grid'] = grid
                            print("Canción cargada desde la base de datos.")
                        columna_actual = 0
                        reproduciendo = False
                        
                    elif boton['accion'] == 'cargar_deck_the_halls':
                        grid, nuevo_tiempo = cargar_deck_the_halls_robotico(grid)
                        config_grid['grid'] = grid
                        tiempo_por_beat = nuevo_tiempo
                        print(f"Canción 'Deck The Halls' cargada. Nuevo tiempo por beat: {tiempo_por_beat}")
                        columna_actual = 0
                        reproduciendo = False

                    elif boton['accion'] == 'cargar_escala_prueba':
                        grid, nuevo_tiempo = cargar_escala_de_prueba(grid)
                        config_grid['grid'] = grid
                        tiempo_por_beat = nuevo_tiempo 
                        print(f"Canción 'Escala de Prueba' cargada. Nuevo tiempo por beat: {tiempo_por_beat}")
                        columna_actual = 0
                        reproduciendo = False

                    elif boton['accion'] == 'cargar_cancion_lenta':
                        grid, nuevo_tiempo = cargar_cancion_lenta(grid)
                        config_grid['grid'] = grid
                        tiempo_por_beat = nuevo_tiempo 
                        print(f"Canción 'We Wish You a Merry Christmas' cargada. Nuevo tiempo por beat: {tiempo_por_beat}")
                        columna_actual = 0
                        reproduciendo = False
                    
                    elif boton['accion'] == 'cargar_cancion_rapida':
                        grid, nuevo_tiempo = cargar_cancion_rapida(grid)
                        config_grid['grid'] = grid
                        tiempo_por_beat = nuevo_tiempo 
                        print(f"Canción 'Mega Man' cargada. Nuevo tiempo por beat: {tiempo_por_beat}")
                        columna_actual = 0
                        reproduciendo = False
                    break
            
            # Solo si NO dio click en botón, verificar el grid
            if not click_en_boton:
                resultado = mouse_a_grid(mouse_x, mouse_y, config_grid)
                if resultado is not None:
                    fila, columna = resultado
                    toggle_nota(grid, fila, columna)
    
    # LÓGICA DE REPRODUCCIÓN
    if reproduciendo:
        tiempo_acumulado += dt
        if tiempo_acumulado >= tiempo_por_beat:
            tiempo_acumulado = 0
            columna_actual += 1
            if columna_actual >= GRID_COLUMNAS:
                pygame.mixer.stop()
                tiempo_acumulado = -0.1
                columna_actual = 0
            for fila in range(GRID_FILAS):
                nota = grid[fila][columna_actual]
                if nota is not None:
                    reproducir_sonido_en_canal(sonidos[fila], fila)
                    nota['bounce'] = pygame.time.get_ticks()
            
    
    # DIBUJAR
    screen.fill(COLOR_BLANCO)
    dibujar_grid(screen, config_grid, SPRITE_NOTAS)
    
    # DIBUJAR PLAYHEAD
    if reproduciendo or columna_actual > 0:
        dibujar_prota(screen, columna_actual, config_grid, grid, sprite_prota)
    
    # DIBUJAR BOTONES
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for boton in botones:
        dibujar_boton(screen, boton, fuente_botones, mouse_x, mouse_y)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000.0

pygame.quit()