#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphics import load_image, resize
import config
from config import SMALL, PNG_EXT, EXIT, MAIN_MENU_SCENE
from buttom import Buttom
import pygame
from pygame import rect

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

    def __init__(self, director, background_name=False, page_number=False):
        self.director = director
        self.is_failed = False
        self.page = False
        self.is_move = False
        if not page_number and background_name:
            self.background = resize(load_image(config.backgrounds+background_name+SMALL+PNG_EXT), (800, 600))
        else:
            directorie = config.definition_pages+page_number+PNG_EXT
            print "Directorie: "+directorie
            self.background = load_image(directorie)
        
        self.failed_rect = rect.Rect((0, 0), (0, 0))                    
        self.failed_img = load_image(config.titles+'failed'+PNG_EXT, True)
        self.failed_rect.topleft = (0, 0)
        self.failed_rect.size = self.failed_img.get_rect().size        
        
        self.common_buttoms = {
                               EXIT: Buttom(config.exit_btn_pos, config.exit_btn_size, 'exit_pressed'+PNG_EXT, 'exit_release'+PNG_EXT),
                               MAIN_MENU_SCENE: Buttom(config.main_menu_btn_pos, config.main_menu_btn_size, 'main_menu_pressed'+PNG_EXT, 'main_menu_release'+PNG_EXT)
                                }     
        
        self.pages = False
        self.go_scene = False
        self.exit = False
        self.is_complete = False
        
    def draw(self, screen):        
        screen.blit(self.background, (0, 0))
        if self.is_failed:
            screen.blit(self.failed_img, self.failed_rect)                 
        for buttom in self.common_buttoms.itervalues():
            buttom.draw(screen)       
            
    def update(self):                    
        for key, buttom in self.common_buttoms.iteritems():
            buttom.updater()
            if buttom.is_pressed: self.go_scene = key 
            
    def event(self, event):     
        if event.type == pygame.MOUSEBUTTONDOWN:
            print str(pygame.mouse.get_pos())
        
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            for buttom in self.common_buttoms.itervalues():
                buttom.mouse_over(mouse_pos)        
                
        if event.type == pygame.MOUSEBUTTONUP: 
            mouse_pos = pygame.mouse.get_pos()
            for buttom in self.common_buttoms.itervalues():
                buttom.pressed(mouse_pos)   

        if event.type == pygame.KEYDOWN and self.is_failed:
            self.is_failed = False

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