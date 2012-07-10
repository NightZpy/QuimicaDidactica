'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
from definitions import Definitions
import pygame


class Sce_Definitions(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_match):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_match)        
        self.definitions = Definitions()
        
        
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True

    def on_update(self):
        self.time = self.director.time 
        self.update()
        for key, option in self.definitions.options.iteritems():
            if option.is_pressed:
                self.definitions.load_pages(key, self.director)
                
        self.pages = self.definitions.pages_listed
        if self.pages: self.page = self.definitions.current_page

    def on_event(self, event):
        self.event(event)        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for option in self.definitions.options.itervalues():
                mouse_pos = pygame.mouse.get_pos()
                option.pressed(mouse_pos)
                        

    def on_draw(self, screen):
        self.draw(screen)
        #self.definitions.draw(screen)
        
        