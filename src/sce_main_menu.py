'''
Created on 26/06/2012

@author: nightzpy
'''
from scene import Scene
from graphics import load_image
import config
import pygame
from buttom import Buttom
from config import PNG_EXT, SMALL, DEFINITIONS_SCENE, COTIDIAN_FUNCTION_SCENE,\
    SOPA_LETRAS_SCENE, NOMBRAR_SCENE, PAREO_SCENE, CRUCIGRAMA_SCENE

class Sce_Main_Menu(Scene):
    '''
    classdocs
    '''
    def __init__(self, director, background_name):
        '''
        Constructor
        '''        
        Scene.__init__(self, director, background_name)
        
        self.buttoms = {
                        DEFINITIONS_SCENE: Buttom(200, 100, "buttom_1_pressed"+PNG_EXT, "buttom_1_release"+PNG_EXT, True), 
                        COTIDIAN_FUNCTION_SCENE: Buttom(550, 100, "buttom_2_pressed"+PNG_EXT, "buttom_2_release"+PNG_EXT, True),  
                        SOPA_LETRAS_SCENE: Buttom(200, 250, "buttom_3_pressed"+PNG_EXT, "buttom_3_release"+PNG_EXT, True),  
                        NOMBRAR_SCENE: Buttom(550, 250, "buttom_4_pressed"+PNG_EXT, "buttom_4_release"+PNG_EXT, True), 
                        PAREO_SCENE: Buttom(200, 400, "buttom_5_pressed"+PNG_EXT, "buttom_5_release"+PNG_EXT, True),  
                        CRUCIGRAMA_SCENE: Buttom(550, 400, "buttom_6_pressed"+PNG_EXT, "buttom_6_release"+PNG_EXT, True)
                        }
        
        
    def locate_buttoms(self):
        pass
    
    def on_update(self):
        self.time = self.director.time   
        for scene, buttom in self.buttoms.iteritems():
            buttom.updater()
            if buttom.is_pressed: self.go_scene = scene
            #else: self.go_scene = False
            

    def on_event(self, event):
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print "Tecla: Izquierda"
        if keys[pygame.K_RIGHT]:
            print "Tecla: Derecha"
        """
        
        mouse_pos = pygame.mouse.get_pos()
        for buttom in self.buttoms.itervalues():
            buttom.mouse_over(mouse_pos)
        
        if event.type == pygame.MOUSEBUTTONUP: 
            #print "MOUSEBUTTONUP"
            #mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for buttom in self.buttoms.itervalues():
                buttom.pressed(mouse_pos)

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        for buttom in self.buttoms.itervalues():
            buttom.dibujar(screen)
    
    
        
        
        