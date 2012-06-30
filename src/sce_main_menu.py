'''
Created on 26/06/2012

@author: nightzpy
'''
from scene import Scene
from graphics import load_image
import config
import pygame
from buttom import Buttom

class Sce_Main_Menu(Scene):
    '''
    classdocs
    '''
    def __init__(self, director):
        '''
        Constructor
        '''        
        Scene.__init__(self, director)
        self.background = load_image(config.backgrounds+"main_menu_small.png")
        self.buttoms = [
                        Buttom(200, 100, "buttom_1_pressed.png", "buttom_1_release.png", True), 
                        Buttom(550, 100, "buttom_2_pressed.png", "buttom_2_release.png", True),  
                        Buttom(200, 250, "buttom_3_pressed.png", "buttom_3_release.png", True),  
                        Buttom(550, 250, "buttom_4_pressed.png", "buttom_4_release.png", True), 
                        Buttom(200, 400, "buttom_5_pressed.png", "buttom_5_release.png", True),  
                        Buttom(550, 400, "buttom_6_pressed.png", "buttom_6_release.png", True)
                        ]
        
        
    def locate_buttoms(self):
        pass
    
    def on_update(self):
        self.time = self.director.time   
        for buttom in self.buttoms:
            buttom.actualizar()
            

    def on_event(self, event):
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print "Tecla: Izquierda"
        if keys[pygame.K_RIGHT]:
            print "Tecla: Derecha"
        """
        
        mouse_pos = pygame.mouse.get_pos()
        for buttom in self.buttoms:
            buttom.mouse_over(mouse_pos)
        
        if event.type == pygame.MOUSEBUTTONUP: 
            #print "MOUSEBUTTONUP"
            #mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            for buttom in self.buttoms:
                buttom.pressed(mouse_pos)

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        for buttom in self.buttoms:
            buttom.dibujar(screen)
    
    
        
        
        