import pygame
from maestre import dibujar_pixel, actualizar_pixel, dibujar_circulo, detectar_alineacion, actualizar_salto
from orquesta import cargar_sonido, reproducir_sonido


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mi Proyecto Pygame")

# BLOQUE PARA INICIALIZAR VARIABLES GLOBALES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pixel_x = 100
velocidad = 200  # píxeles por segundo
dt = 0

circulo_x = 400
circulo_y = 300
radio = 15
BLUE = (0, 0, 255)
# ////////////////////////////////////////////

# VARIABLES DEL MAESTRE
maestre_y = 280
velocidad_y = 0
gravedad = 2500
fuerza_salto = -200
en_suelo = False
altura_base = 280
# ////////////////////////////////////////////


# BLOQUE PARA INICIALIZAR OBJETOS

pygame.mixer.init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=512
)
# ////////////////////////////////////////////

sonido_beep = cargar_sonido("sounds/dagger.wav", volumen=0.7)
sonido_reproducido = False

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.line(screen, RED, (100, 300), (700, 300), 3)
    dibujar_circulo(screen, circulo_x, circulo_y, radio, BLUE)
    pixel_x, velocidad, llego = actualizar_pixel(pixel_x, velocidad, dt, 100, 700)
    
    # Actualizar física del salto
    maestre_y, velocidad_y, en_suelo = actualizar_salto(
        maestre_y, velocidad_y, gravedad, dt, altura_base
    )
    
    alineado = detectar_alineacion(pixel_x, circulo_x, radio)

    if alineado and en_suelo:
        velocidad_y = fuerza_salto
        if not sonido_reproducido:
            reproducir_sonido(sonido_beep)
            sonido_reproducido = True
    elif not alineado:
        sonido_reproducido = False

    if llego:
        running = False
    
    dibujar_pixel(screen, int(pixel_x), int(maestre_y), BLACK)    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()