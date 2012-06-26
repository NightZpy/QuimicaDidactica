#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Modulos
# ---------------------------------------------------------------------

import sys
import pygame

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
        self.pantalla = pygame.display.set_mode((640, 480))
        self.pantalla = pygame.display.set_caption("Plantilla Escenas")
        self.escena = None
        self.isSalir = False
        self.reloj = pygame.time.Clock()

    def bucle(self):
        "Inicia el juego: Loop/Ciclo/Bucle principal"
        while not self.isSalir:
            tiempo = self.reloj.tick(60)
            #Eventos de salida
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.salir()
                if evento.type == pygame.KEYDOWN:
                    if evento.key  == pygame.K_ESCAPE:
                        self.salir()

            #Detecta los eventos
            self.escena.onEvent()

            #Actualiza la escena
            self.escena.onUpdate()

            #Dibuja en pantalla
            self.escena.onDraw(self.pantalla)
            pygame.display.flip()

    def cambiarEscena(self, escena):
        "Altera la escena actual."
        self.escena = escena

    def salir(self):
        self.isSalir = True

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------