'''
Created on 09/07/2012

@author: nightzpy
'''
from scene import Scene
from config import PREV_BTN, NEXT_BTN, GO_SCHEME, PNG_EXT, DEFINITIONS_SCENE
from buttom import Buttom
import config
import pygame

class Page(Scene):
    '''
    classdocs
    '''


    def __init__(self, director, page_number = False, previous = False, follow = False):
        '''
        Constructor
        '''
        Scene.__init__(self, director, False, page_number)
        self.previous = previous
        self.follow = follow
        self.prev_init = False          
        self.buttoms = {}
        self.buttoms[GO_SCHEME] = Buttom(config.page_btn_go_scheme_pos, config.page_btn_size, 'go_scheme_pressed'+PNG_EXT, 'go_scheme_release'+PNG_EXT, True)
        
                      
    def check_buttoms(self):
        if self.previous:
            self.buttoms[PREV_BTN] = Buttom(config.page_btn_prev_pos, config.page_btn_size, 'previous_pressed'+PNG_EXT, 'previous_release'+PNG_EXT, True)
            self.buttoms[PREV_BTN].is_visible = False
            self.buttoms[PREV_BTN].is_active = False
            self.prev_init = self.previous
        if self.follow:
            self.buttoms[NEXT_BTN] = Buttom(config.page_btn_next_pos, config.page_btn_size, 'next_pressed'+PNG_EXT, 'next_release'+PNG_EXT, True)     
        
    def on_update(self):
        self.time = self.director.time 
        self.update()
        for scene, buttom in self.buttoms.iteritems():
            if buttom.is_active:
                buttom.updater() 
                if buttom.is_pressed:
                               
                    if scene==PREV_BTN: 
                        self.is_move=True
                        buttom.is_pressed = False
                        self.page = self.prev_init
                    elif scene==NEXT_BTN: 
                        self.is_move=True
                        self.page = self.follow
                        buttom.is_pressed = False
                    elif scene==GO_SCHEME: 
                        self.go_scene = DEFINITIONS_SCENE
                        self.pages = False
                
                 

    def on_event(self, event):
        self.event(event)
        
        if event.type == pygame.MOUSEMOTION:        
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
        self.draw(screen)
        for buttom in self.buttoms.itervalues():
            buttom.draw(screen)
            
