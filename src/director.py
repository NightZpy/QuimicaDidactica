#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Modulos
# ---------------------------------------------------------------------

import pygame
import config

# ---------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------
# Clases
# ---------------------------------------------------------------------

class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((config.width, config.hight))
        pygame.display.set_caption(config.NAME)
        print "Screen: "+str(self.screen)
        self.scene = None
        self.go_away = False
        self.time_keeper = pygame.time.Clock()

    def loop(self):
        "Inicia el juego: Loop/Ciclo/Bucle principal"
        while not self.go_away:
            self.time = self.time_keeper.tick(60)
            #Eventos de salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key  == pygame.K_ESCAPE:
                        self.exit()

                #Detecta los eventos
                self.scene.on_event(event)

            #Actualiza la scene
            self.scene.on_update()

            #Dibuja en screen
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, escena):
        "Altera la scene actual."
        self.scene = escena

    def exit(self):
        self.go_away = True

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------