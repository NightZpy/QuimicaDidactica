'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
import pygame
from pygame.rect import Rect
from buttom import Buttom
import config
from config import PNG_EXT, CRUCIGRAMA_SCENE
from graphics import load_image, resize
from sce_winner import Sce_Winner



class Sce_Crucigrama(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)
        self.scene_winner =  Sce_Winner(director, 'winner', CRUCIGRAMA_SCENE)
        
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True        
            

        

        
        self.is_typing = False
        self.typing_in = ''
        self.complete_word = ''
        self.complete_words = []
        self.finish_typing = False

    def on_update(self):
        self.time = self.director.time                
        if not self.is_failed: 
            self.update()
            for key, buttom in self.buttoms.iteritems():
                buttom.updater()
                if buttom.is_active:
                    if buttom.is_pressed:
                        if not self.is_typing: 
                            self.is_typing = True
                            self.typing_in = key
    
                        if self.finish_typing:
                            if self.typing_in == self.complete_word:
                                buttom.is_active = False
                                buttom.is_pressed=True
                                self.complete_words.append(self.typing_in)
                            else:                        
                                buttom.is_active = True
                                buttom.is_pressed=False                   
                                self.is_failed = True                                                         
                            self.finish_typing = False
                            self.complete_word = ''
                            self.is_typing = False
                
            self.is_complete = (len(self.words) == len(self.complete_words))


    def on_event(self, event):
        self.event(event)
        
        if event.type == pygame.MOUSEMOTION:                    
            for buttom in self.buttoms.itervalues():
                mouse_pos = pygame.mouse.get_pos()
                buttom.mouse_over(mouse_pos)
                
        if event.type == pygame.MOUSEBUTTONUP:             
            for buttom in self.buttoms.itervalues():
                mouse_pos = pygame.mouse.get_pos()
                buttom.pressed(mouse_pos)  
                
        if event.type == pygame.KEYDOWN:            
            if self.is_typing:
                if event.unicode.lower() in ("abcdefghijklmnopqrstuvwxyz"):
                    print "Key: "+event.unicode.lower()
                    self.complete_word += event.unicode.lower()
                elif (event.key == pygame.K_RETURN):                    
                    self.finish_typing = True        
                                                            

    def on_draw(self, screen):
        self.draw(screen)
        for buttom in self.buttoms.itervalues():
            buttom.draw(screen)
        
        for word in self.complete_words:
            screen.blit(self.words[word], self.words_rect[word])
            
        if self.is_failed:
            screen.blit(self.failed_img, self.failed_rect)
            
        