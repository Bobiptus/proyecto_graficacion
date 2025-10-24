import pygame.mixer

def cargar_sonido(ruta, volumen=1.0):
    sonido = pygame.mixer.Sound(ruta)
    sonido.set_volume(volumen)
    return sonido

def reproducir_sonido(sonido):
    sonido.play()

def reproducir_sonido_en_canal(sonido, canal_id):
    canal = pygame.mixer.Channel(canal_id)
    canal.play(sonido)