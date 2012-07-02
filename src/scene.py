#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphics import load_image
import config
from config import SMALL, PNG_EXT

# ---------------------------------------------------------------------
# Modulos
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Clases
# ---------------------------------------------------------------------

class Scene:
    """Representa un escena abstracta del videojuego.
    Una escena es una parte visible del juego, como una pantalla de presentaci�n o men� de opciones.
    Tiene que crear un objeto derivado de esta clase para crear una escena utilizable."""

    def __init__(self, director, background_name):
        self.director = director
        self.background = load_image(config.backgrounds+background_name+SMALL+PNG_EXT) 
        self.go_scene = False
        self.exit = False

    def on_update(self):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método on_update.")

    def on_event(self, event):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método on_event.")

    def on_draw(self, screen):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método on_draw.")

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------