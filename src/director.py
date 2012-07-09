#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------
# Modulos
# ---------------------------------------------------------------------

import pygame
import config
from config import EXIT, MAIN_MENU_SCENE,\
    MATCH_SCENE, NAME_SCENE, CRUCIGRAMA_SCENE, SOPA_LETRAS_SCENE,\
    COTIDIAN_FUNCTION_SCENE, HANGMAN_SCENE
from sce_main_menu import Sce_Main_Menu
from sce_hangman import Sce_Hangman
from sce_match import Sce_Match 
from sce_name import Sce_Name
from sce_crucigrama import Sce_Crucigrama
from sce_sopa_letras import Sce_Sopa_Letras
from sce_functional_group import Sce_Functional_Group
import time

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
        self.screen = pygame.display.set_mode((config.width, config.height))
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
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == pygame.KEYDOWN): return EXIT
                
                #Detecta los eventos
                self.scene.on_event(event)

            #Actualiza la scene
            self.scene.on_update()

            #Verifico si hay un cambio de scena
            if self.scene.is_complete:
                time.sleep(1) 
                return self.scene.scene_winner
            
            
            if self.scene.go_scene != EXIT: 
                if self.scene.go_scene == MAIN_MENU_SCENE: return Sce_Main_Menu(self, MAIN_MENU_SCENE)
                if self.scene.go_scene == HANGMAN_SCENE: return Sce_Hangman(self, HANGMAN_SCENE)
                if self.scene.go_scene == MATCH_SCENE: return Sce_Match(self, MATCH_SCENE)
                if self.scene.go_scene == NAME_SCENE: return Sce_Name(self, NAME_SCENE)
                if self.scene.go_scene == CRUCIGRAMA_SCENE: return Sce_Crucigrama(self, CRUCIGRAMA_SCENE)
                if self.scene.go_scene == SOPA_LETRAS_SCENE: return Sce_Sopa_Letras(self, SOPA_LETRAS_SCENE)
                if self.scene.go_scene == COTIDIAN_FUNCTION_SCENE: return Sce_Functional_Group(self, COTIDIAN_FUNCTION_SCENE)
                
            else: return self.scene.go_scene
            
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