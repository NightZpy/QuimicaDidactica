'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
import pygame
from config import CROSSWORD_SCENE
from sce_winner import Sce_Winner
from crossword import Crossword
import config



class Sce_Crucigrama(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)
        self.scene_winner =  Sce_Winner(director, 'winner', CROSSWORD_SCENE)
        
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True        
        
        self.crossword = Crossword()
        
        self.is_typing = False
        self.finish_typing = False
        self.typing_in = ''
        self.complete_word = ''
        self.complete_words = []
        

    def on_update(self):
        self.time = self.director.time                
        if not self.is_failed: 
            self.update()
            self.crossword.update()            
            if not self.is_typing:
                for buttom in self.crossword.buttoms.itervalues():
                    if buttom.is_pressed:
                        self.is_typing = True
                        self.finish_typing = False
            self.is_complete = self.crossword.is_complete
                    
    def on_event(self, event):
        self.event(event)
        if not self.is_failed:
            if event.type == pygame.MOUSEMOTION:                    
                for buttom in self.crossword.buttoms.itervalues():
                    mouse_pos = pygame.mouse.get_pos()
                    buttom.mouse_over(mouse_pos)
                    
            if event.type == pygame.MOUSEBUTTONUP:             
                for buttom in self.crossword.buttoms.itervalues():
                    mouse_pos = pygame.mouse.get_pos()
                    if buttom.is_active: 
                        buttom.pressed(mouse_pos)
                        self.crossword.typeds = []  
            
            if self.is_typing:
                if event.type == pygame.KEYDOWN:                        
                    char = event.unicode.lower()
                    if event.unicode.lower() in config.chars:
                        #print "Key: "+event.unicode.lower()
                        self.crossword.put_char(char)
                    elif (event.key == pygame.K_RETURN):                    
                        self.finish_typing = True
                        self.is_typing = False 
                        if not self.crossword.check_word(): self.is_failed = True       
                                                            

    def on_draw(self, screen):
        self.draw(screen)
        self.crossword.draw(screen)
            
        