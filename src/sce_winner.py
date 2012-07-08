'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
from config import PNG_EXT
import config
from buttom import Buttom
from graphics import load_image, resize
import pygame

class Sce_Winner(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name, continue_scene):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True
        
        self.continue_scene = continue_scene
        
        self.winner_img = resize(load_image(config.titles+'winner'+PNG_EXT, True), config.winner_title_size)
        self.winner_rect = self.winner_img.get_rect()     
        self.winner_rect.center = config.winner_title_pos   
        self.next_btn = Buttom((config.width/2, self.winner_rect.bottom + (self.winner_rect.height / 2)), config.b_size, 'continue_pressed'+PNG_EXT, 'continue_release'+PNG_EXT, True) 
                

    def on_update(self):
        self.time = self.director.time 
        self.update()                
        self.next_btn.updater()
        if self.next_btn.is_pressed: self.go_scene = self.continue_scene

    def on_event(self, event):
        self.event(event)

        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            self.next_btn.mouse_over(mouse_pos)
        
        if event.type == pygame.MOUSEBUTTONUP: 
            mouse_pos = pygame.mouse.get_pos()
            self.next_btn.pressed(mouse_pos)        

    def on_draw(self, screen):
        self.draw(screen)
        screen.blit(self.winner_img, self.winner_rect)
        print "winner rect: "+str(self.winner_rect)
        self.next_btn.draw(screen)        
        