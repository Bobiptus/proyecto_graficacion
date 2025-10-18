import pygame

def inicializar_grid(filas, columnas):
    grid = []
    for y in range(filas):
        fila = []
        for x in range(columnas):
            fila.append(False)
        grid.append(fila)
    return grid

def dibujar_grid(screen, config, colores_notas):
    inicio_x = config['inicio_x']
    inicio_y = config['inicio_y']
    ancho_celda = config['ancho_celda']
    alto_celda = config['alto_celda']
    filas = config['filas']
    columnas = config['columnas']
    grid = config['grid']
    
    COLOR_LINEA = (100, 100, 100)
    
    for i in range(filas + 1):
        y = inicio_y + i * alto_celda
        pygame.draw.line(screen, COLOR_LINEA, 
                        (inicio_x, y), 
                        (inicio_x + columnas * ancho_celda, y), 
                        2)
    for i in range(columnas + 1):
        x = inicio_x + i * ancho_celda
        pygame.draw.line(screen, COLOR_LINEA,
                        (x, inicio_y),
                        (x, inicio_y + filas * alto_celda),
                        1)
    for fila in range(filas):
        for col in range(columnas):
            if grid[fila][col]:
                centro_x = inicio_x + col * ancho_celda + ancho_celda // 2
                centro_y = inicio_y + fila * alto_celda + alto_celda // 2
                pygame.draw.circle(screen, colores_notas[fila], (centro_x, centro_y), 15)

def mouse_a_grid(mouse_x, mouse_y, config):
    inicio_x = config['inicio_x']
    inicio_y = config['inicio_y']
    ancho_celda = config['ancho_celda']
    alto_celda = config['alto_celda']
    columnas = config['columnas']
    filas = config['filas']

    if (mouse_x < inicio_x or mouse_x >= inicio_x + columnas * ancho_celda or
        mouse_y < inicio_y or mouse_y >= inicio_y + filas * alto_celda):
        return None

    columna = (mouse_x - inicio_x) // ancho_celda
    fila = (mouse_y - inicio_y) // alto_celda

    return (fila, columna)

def toggle_nota(grid, fila, columna):
    grid[fila][columna] = not grid[fila][columna]