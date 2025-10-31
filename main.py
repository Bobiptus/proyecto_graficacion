"""
Proyecto final para la materia de Graficación por computadora del Instituto Tecnológico de Ensenada (ITE)
Autor: Armando Roberto Pérez Banda
Matrícula: 24760228
Descripción: Secuenciador musical básico que permite al usuario crear patrones rítmicos y melódicos interactuando con una cuadrícula visual.

Programa realizado en Python 3.10 para mas información revisar el archivo README.md
"""

import pygame
from grid import inicializar_grid, dibujar_grid, mouse_a_grid, toggle_nota
from orquesta import cargar_sonido, reproducir_sonido, reproducir_sonido_en_canal
from botones import crear_boton, dibujar_boton, mouse_sobre_boton

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(16) 
pygame.font.init()
fuente_botones = pygame.font.Font(None, 32)
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Secuenciador Musical")
clock = pygame.time.Clock()

# Se declaran los colores que se van a utilizar al rededor de todo el programa
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

COLORES_NOTAS = [
    (255, 100, 100),
    (255, 150, 100),
    (255, 200, 100),
    (200, 255, 100),
    (100, 255, 100),
    (100, 200, 255),
    (150, 100, 255)
]

# Se declaran los sonidos utilizados
sonidos = [
    cargar_sonido("sounds/beep.wav", 1),
    cargar_sonido("sounds/gota.wav", 1),
    cargar_sonido("sounds/mouse.wav", 1),
    cargar_sonido("sounds/organ.wav", 1),
    cargar_sonido("sounds/plato.wav", 1),
    cargar_sonido("sounds/organo.wav", 1),
    cargar_sonido("sounds/drum.wav", 1)
]

# CONFIGURACIÓN DEL GRID
GRID_FILAS = 7
GRID_COLUMNAS = 16
CELDA_ANCHO = 50
CELDA_ALTO = 60
GRID_INICIO_X = 100
GRID_INICIO_Y = 150

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
tiempo_por_beat = 0.25
tiempo_acumulado = 0

# CREAR BOTONES
botones = [
    crear_boton(100, 50, 100, 40, "Play", (0, 150, 0), (0, 200, 0), "play"),
    crear_boton(220, 50, 100, 40, "Stop", (150, 0, 0), (200, 0, 0), "stop"),
    crear_boton(340, 50, 100, 40, "Clear", (0, 0, 150), (0, 0, 200), "clear")
]

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
                        columna_actual = 0
                    
                    elif boton['accion'] == "clear":
                        grid = inicializar_grid(GRID_FILAS, GRID_COLUMNAS)
                        config_grid['grid'] = grid
                    
                    break
            
            # Solo si NO dio click en botón, verificar el grid
            if not click_en_boton:
                resultado = mouse_a_grid(mouse_x, mouse_y, config_grid)
                if resultado is not None:
                    fila, columna = resultado
                    toggle_nota(grid, fila, columna)
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reproduciendo = not reproduciendo
                if reproduciendo:
                    columna_actual = 0
                    tiempo_acumulado = 0
    
    # LÓGICA DE REPRODUCCIÓN
    if reproduciendo:
        tiempo_acumulado += dt
        if tiempo_acumulado >= tiempo_por_beat:
            tiempo_acumulado = 0
            columna_actual += 1
            if columna_actual >= GRID_COLUMNAS:
                columna_actual = 0
            for fila in range(GRID_FILAS):
                if grid[fila][columna_actual]:
                    reproducir_sonido_en_canal(sonidos[fila], fila)
            
    
    # DIBUJAR
    screen.fill(WHITE)
    dibujar_grid(screen, config_grid, COLORES_NOTAS)
    
    # DIBUJAR PLAYHEAD
    if reproduciendo or columna_actual > 0:
        x_playhead = GRID_INICIO_X + columna_actual * CELDA_ANCHO
        pygame.draw.line(screen, RED,
                        (x_playhead, GRID_INICIO_Y),
                        (x_playhead, GRID_INICIO_Y + GRID_FILAS * CELDA_ALTO),
                        3)
    
    # DIBUJAR BOTONES
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for boton in botones:
        dibujar_boton(screen, boton, fuente_botones, mouse_x, mouse_y)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()