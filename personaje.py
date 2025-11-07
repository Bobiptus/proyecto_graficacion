import pygame

def dibujar_prota(screen, columna_actual, config_grid, grid, color=(255, 0, 0)):
    inicio_x = config_grid['inicio_x']
    inicio_y = config_grid['inicio_y']
    ancho_celda = config_grid['ancho_celda']
    alto_celda = config_grid['alto_celda']
    filas = config_grid['filas']
    
    x = inicio_x + columna_actual * ancho_celda + ancho_celda // 2
    y_base = inicio_y - 30
    y = y_base

    tamaño = 20
    pygame.draw.rect(screen, color, (x - tamaño // 2, y - tamaño // 2, tamaño, tamaño))
    pygame.draw.rect(screen, (0, 0, 0), (x - tamaño // 2, y - tamaño // 2, tamaño, tamaño), 2)
    

