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

class Scene:
    """Representa un escena abstracta del videojuego.
    Una escena es una parte visible del juego, como una pantalla de presentaci�n o men� de opciones.
    Tiene que crear un objeto derivado de esta clase para crear una escena utilizable."""

    def __init__(self, director):
        self.director = director
        self.go_main_menu = False
        self.go_ahorcado = False
        self.go_nombrar = False
        self.go_sopa_letras = False
        self.go_crucigrama = False
        self.go_pareo = False
        self.go_funcion_cotidiana = False
        self.is_paused = False
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