import pygame

def crear_boton(x, y, ancho, alto, texto, color, color_hover, accion):
    return {
    'x' : x,
    'y' : y,
    'ancho' : ancho,
    'alto' : alto,
    'texto' : texto,
    'color' : color,
    'color_hover' : color_hover,
    'accion' : accion
}

def mouse_sobre_boton(mouse_x, mouse_y, boton):
    if (boton['x'] <= mouse_x <= boton['x'] + boton['ancho'] and
        boton['y'] <= mouse_y <= boton['y'] + boton['alto']):
        return True
    return False

def dibujar_boton(screen, boton, fuente, mouse_x, mouse_y):
    if mouse_sobre_boton(mouse_x, mouse_y, boton):
        color = boton['color_hover']
    else:
        color = boton['color']
    rect = pygame.Rect(boton['x'], boton['y'], boton['ancho'], boton['alto'])
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    texto_surface = fuente.render(boton['texto'], True, (255, 255, 255))
    texto_rect = texto_surface.get_rect(center=rect.center)
    screen.blit(texto_surface, texto_rect)