import pygame
from grid import inicializar_grid, dibujar_grid, mouse_a_grid, toggle_nota
from orquesta import cargar_sonido, reproducir_sonido

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Secuenciador Musical")
clock = pygame.time.Clock()

# COLORES
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

# CARGAR SONIDOS
sonidos = [
    cargar_sonido("sounds/note-do.mp3", 1),
    cargar_sonido("sounds/note-re.mp3", 1),
    cargar_sonido("sounds/note-mi.mp3", 1),
    cargar_sonido("sounds/note-fa.mp3", 1),
    cargar_sonido("sounds/note-sol.mp3", 1),
    cargar_sonido("sounds/note-la.mp3", 1),
    cargar_sonido("sounds/note-si.mp3", 1)
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

# COMIENZA EL BUCLE PRINCIPAL

running = True
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
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
    if reproduciendo:
        tiempo_acumulado += dt
        if tiempo_acumulado >= tiempo_por_beat:
            tiempo_acumulado = 0
            for fila in range(GRID_FILAS):
                if grid[fila][columna_actual]:
                    reproducir_sonido(sonidos[fila])
            
            columna_actual += 1
            if columna_actual >= GRID_COLUMNAS:
                columna_actual = 0
            
    screen.fill(WHITE)
    dibujar_grid(screen, config_grid, COLORES_NOTAS)

if reproduciendo or columna_actual > 0:
        x_playhead = GRID_INICIO_X + columna_actual * CELDA_ANCHO
        pygame.draw.line(screen, RED,
                        (x_playhead, GRID_INICIO_Y),
                        (x_playhead, GRID_INICIO_Y + GRID_FILAS * CELDA_ALTO),
                        3)

pygame.display.flip()
dt = clock.tick(60) / 1000
pygame.quit()