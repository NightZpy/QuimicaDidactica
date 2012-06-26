# -*- coding: utf-8 -*-

"""Modulo para implementar el manejo de graficos y superficies"""

# M�dulos
import pygame
import config

# Carga una imagen, la trasnparencia para la imagen y el color de la transparencia son opcionales
def cargarImagen(filename, transparent=False, pixel=(0,0)):
    "Convertimos la imagen al fomrato interno de Pygame"
    try: image = pygame.image.load(filename)
    except pygame.error, message:
            raise SystemExit, message
    image = image.convert()
    if transparent:
            color = image.get_at(pixel)
            image.set_colorkey(color, pygame.RLEACCEL)
    return image

def textoAImagen(texto, posx, posy, color=(0, 0, 0), tam=15):
    "Convierte un texto a una imagen que será dibujada."
    fuente = pygame.font.Font(config.fuentes + "DroidSans.ttf", tam)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect