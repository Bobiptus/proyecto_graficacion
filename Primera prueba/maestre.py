import pygame

def dibujar_pixel(screen, x, y, color):
    pygame.draw.circle(screen, color, (x, y), 5)

def actualizar_pixel(posicion_actual, velocidad, dt, limite_inicio, limite_final):
    nueva_posicion = posicion_actual + velocidad * dt
    llego_al_limite = False
    if nueva_posicion >= limite_final:
        nueva_posicion = limite_final
        llego_al_limite = True
    return nueva_posicion, velocidad, llego_al_limite

def detectar_alineacion (maestre_x, circulo_x, radio):
    return abs(maestre_x - circulo_x) <= radio

def dibujar_circulo(screen, x, y, radio, color):
    pygame.draw.circle(screen, color, (x, y), radio)

def actualizar_salto(maestro_y, velocidad_y, gravedad, dt, altura_base):
    velocidad_y += gravedad * dt
    maestro_y += velocidad_y * dt
    en_suelo = False
    if maestro_y >= altura_base:
        maestro_y = altura_base
        velocidad_y = 0
        en_suelo = True
    return maestro_y, velocidad_y, en_suelo