# -*- coding: utf-8 -*-

"""Modulo para implementar el manejo de graficos y superficies"""

# M�dulos
import pygame
import config

# Carga una imagen, la trasnparencia para la imagen y el color de la transparencia son opcionales
def load_image(filename, transparent=False, pixel=(0,0)):
    "Convertimos la imagen al fomrato interno de Pygame"
    try: image = pygame.image.load(filename)
    except pygame.error, message:
            raise SystemExit, message
    #image = image.convert()
    if transparent:
            #color = image.get_at(pixel)
            #image.set_colorkey(color, pygame.SRCALPHA)
            #image = image.convert()
            image = image.convert_alpha()
    return image

def string_to_image(texto, posx, posy, color=(0, 0, 0), tam=15):
    "Convierte un texto a una imagen que será dibujada."
    fuente = pygame.font.Font(config.fuentes + "DroidSans.ttf", tam)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def resize(img, size): 
    return pygame.transform.scale(img, size)
    