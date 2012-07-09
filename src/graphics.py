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

def string_to_image(text, (x, y), color=(0, 0, 0), size=15):
    "Convierte un texto a una imagen que será dibujada."
    font = pygame.font.Font(config.fonts + "DroidSans.ttf", size)
    out = pygame.font.Font.render(font, text, 1, color)
    rect = out.get_rect()
    #rect.center = (x, y)
    rect.center = (x, y)
    return out, rect

def resize(img, size): 
    return pygame.transform.scale(img, size)
    