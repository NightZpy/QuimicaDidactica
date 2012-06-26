#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Modulos
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Clases
# ---------------------------------------------------------------------

class Escena:
    """Representa un escena abstracta del videojuego.
    Una escena es una parte visible del juego, como una pantalla de presentaci�n o men� de opciones.
    Tiene que crear un objeto derivado de esta clase para crear una escena utilizable."""

    def __init__(self, director):
        self.director = director

    def onUpdate(self):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método onUpdate.")

    def onEvent(self, evento):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método onEvent.")

    def onDraw(self, pantalla):
        "Actualización lógica que se llama automáticamente desde el director."
        raise NotImplemented("Tiene que implementar el método onDraw.")

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------