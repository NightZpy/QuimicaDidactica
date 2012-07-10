'''
Created on 26/06/2012

@author: nightzpy
'''
from scene import Scene
from graphics import load_image
import config
import pygame
from buttom import Buttom
from config import PNG_EXT, HANGMAN_SCENE, COTIDIAN_FUNCTION_SCENE, NAME_SCENE, MATCH_SCENE, CRUCIGRAMA_SCENE, DEFINITIONS_SCENE,\
    ALPHABET_SOUP_SCENE

class Sce_Main_Menu(Scene):
    '''
    classdocs
    '''
    def __init__(self, director, background_name):
        '''
        Constructor
        '''        
        Scene.__init__(self, director, background_name)
        self.title_img = load_image(config.titles+'functional_groups'+PNG_EXT, True)
        self.title_img = pygame.transform.scale(self.title_img, (450, 150))
        self.title_rect = self.title_img.get_rect()
        self.title_rect.centerx = config.width / 2
        self.title_rect.centery = 80
        
        self.buttoms = {
                        DEFINITIONS_SCENE: Buttom((230, 180), config.b_size, "buttom_1_pressed"+PNG_EXT, "buttom_1_release"+PNG_EXT, True),                                                    
                        NAME_SCENE: Buttom((580, 180), config.b_size, "buttom_2_pressed"+PNG_EXT, "buttom_2_release"+PNG_EXT, True), 
                        COTIDIAN_FUNCTION_SCENE: Buttom((230, 300), config.b_size, "buttom_3_pressed"+PNG_EXT, "buttom_3_release"+PNG_EXT, True),
                        MATCH_SCENE: Buttom((580, 300), config.b_size, "buttom_4_pressed"+PNG_EXT, "buttom_4_release"+PNG_EXT, True),
                        ALPHABET_SOUP_SCENE: Buttom((230, 440), config.b_size, "buttom_5_pressed"+PNG_EXT, "buttom_5_release"+PNG_EXT, True),  
                        CRUCIGRAMA_SCENE: Buttom((580, 440), config.b_size, "buttom_6_pressed"+PNG_EXT, "buttom_6_release"+PNG_EXT, True),                        
                        HANGMAN_SCENE: Buttom((config.width / 2, 530), config.b_size, "buttom_7_pressed"+PNG_EXT, "buttom_7_release"+PNG_EXT, True)
                        }
    
    def on_update(self):
        self.time = self.director.time   
        for scene, buttom in self.buttoms.iteritems():
            buttom.updater()
            if buttom.is_pressed: self.go_scene = scene
            

    def on_event(self, event):
        
        if event.type == pygame.MOUSEMOTION:                    
            for buttom in self.buttoms.itervalues():
                mouse_pos = pygame.mouse.get_pos()
                buttom.mouse_over(mouse_pos)
        
        if event.type == pygame.MOUSEBUTTONUP:             
            for buttom in self.buttoms.itervalues():
                mouse_pos = pygame.mouse.get_pos()
                buttom.pressed(mouse_pos)

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.title_img, self.title_rect)
        for buttom in self.buttoms.itervalues():
            buttom.draw(screen)
    
    
        
        
        