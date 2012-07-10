'''
Created on 26/06/2012

@author: nightzpy
'''
from scene import Scene
import pygame
from config import MAIN_MENU_SCENE

class Sce_Main(Scene):
    '''
    classdocs
    '''
    def __init__(self, director, background_name):
        '''
        Constructor
        '''        
        Scene.__init__(self, director, background_name)
        self.event_succes = False
    
    def on_update(self):
        self.time = self.director.time
        
        if self.event_succes:
            self.go_scene = MAIN_MENU_SCENE   
            
            

    def on_event(self, event):
        self.event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.event_succes = True

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
    
    
        
        
        