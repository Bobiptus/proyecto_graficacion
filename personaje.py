import pygame
import math

def cargar_sprite_prota(ruta):
    sprite = pygame.image.load(ruta)
    sprite = pygame.transform.scale(sprite, (30, 30))
    return sprite

def dibujar_prota(screen, columna_actual, config_grid, grid, sprite):
    inicio_x = config_grid['inicio_x']
    inicio_y = config_grid['inicio_y']
    ancho_celda = config_grid['ancho_celda']
    alto_celda = config_grid['alto_celda']
    filas = config_grid['filas']
    
    x = inicio_x + columna_actual * ancho_celda + ancho_celda // 2
    y_base = inicio_y - 30

    # Verificar si hay alguna nota en la columna actual
    hay_nota = False
    bounce_time = 0
    for fila in range(filas):
        nota = grid[fila][columna_actual]
        if nota is not None:
            hay_nota = True
            bounce_time = nota.get('bounce', 0)
            break

    y = y_base
    if hay_nota:
        current_time = pygame.time.get_ticks()
        elapsed = (current_time - bounce_time) / 1000.0
        if elapsed < 0.3:
            bounce_offset = math.sin(elapsed * 20) * math.exp(-elapsed * 8) * 12
            y = y_base - bounce_offset

    # Dibujar siempre (fuera del if)
    ancho = sprite.get_width()
    alto = sprite.get_height()
    screen.blit(sprite, (int(x - ancho // 2), int(y - alto // 2)))