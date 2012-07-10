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

VERT_1 = 'alcano'
VERT_2 = 'urea'
VERT_3 = 'hidroxilo'
VERT_4 = 'formico'
HORZ_1 = 'metano'
HORZ_2 = 'alquino'
HORZ_3 = 'carboxilo'
HORZ_4 = 'nitrilo'

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
        
        self.buttoms = {
                        VERT_1: Buttom((117, 207), config.crux_b_size, 'crux_'+VERT_1+'_pressed'+PNG_EXT, 'crux_'+VERT_1+'_release'+PNG_EXT, True),
                        VERT_2: Buttom((194, 394), config.crux_b_size, 'crux_'+VERT_2+'_pressed'+PNG_EXT, 'crux_'+VERT_2+'_release'+PNG_EXT, True),
                        VERT_3: Buttom((221, 257), config.crux_b_size, 'crux_'+VERT_3+'_pressed'+PNG_EXT, 'crux_'+VERT_3+'_release'+PNG_EXT, True),
                        VERT_4: Buttom((381, 311), config.crux_b_size, 'crux_'+VERT_4+'_pressed'+PNG_EXT, 'crux_'+VERT_4+'_release'+PNG_EXT, True),
                        HORZ_1: Buttom((11, 233), config.crux_b_size, 'crux_'+HORZ_1+'_pressed'+PNG_EXT, 'crux_'+HORZ_1+'_release'+PNG_EXT, True),
                        HORZ_2: Buttom((91, 313), config.crux_b_size, 'crux_'+HORZ_2+'_pressed'+PNG_EXT, 'crux_'+HORZ_2+'_release'+PNG_EXT, True),
                        HORZ_3: Buttom((141, 365), config.crux_b_size, 'crux_'+HORZ_3+'_pressed'+PNG_EXT, 'crux_'+HORZ_3+'_release'+PNG_EXT, True),
                        HORZ_4: Buttom((90, 448), config.crux_b_size, 'crux_'+HORZ_4+'_pressed'+PNG_EXT, 'crux_'+HORZ_4+'_release'+PNG_EXT, True)                        
                       }
            
        self.words_rect = {
                            VERT_1: Rect((102, 218), (131-102, 382-218)),
                            VERT_2: Rect((181, 406), (131-102, 516-406)),
                            VERT_3: Rect((208, 272), (131-102, 517-272)),
                            VERT_4: Rect((366, 326), (131-102, 516-326)),
                            HORZ_1: Rect((22, 219), (179-22, 382-354)),
                            HORZ_2: Rect((103, 300), (289-103, 382-354)),
                            HORZ_3: Rect((155, 353), (395-155, 382-354)),
                            HORZ_4: Rect((102, 434), (289-102, 382-354))                             
                           }
        
        self.words = {
                        VERT_1: resize(load_image(config.crux_words_imgs+VERT_1+PNG_EXT, True), self.words_rect[VERT_1].size),
                        VERT_2: resize(load_image(config.crux_words_imgs+VERT_2+PNG_EXT, True), self.words_rect[VERT_2].size),
                        VERT_3: resize(load_image(config.crux_words_imgs+VERT_3+PNG_EXT, True), self.words_rect[VERT_3].size),
                        VERT_4: resize(load_image(config.crux_words_imgs+VERT_4+PNG_EXT, True), self.words_rect[VERT_4].size),
                        HORZ_1: resize(load_image(config.crux_words_imgs+HORZ_1+PNG_EXT, True), self.words_rect[HORZ_1].size),
                        HORZ_2: resize(load_image(config.crux_words_imgs+HORZ_2+PNG_EXT, True), self.words_rect[HORZ_2].size),
                        HORZ_3: resize(load_image(config.crux_words_imgs+HORZ_3+PNG_EXT, True), self.words_rect[HORZ_3].size),
                        HORZ_4: resize(load_image(config.crux_words_imgs+HORZ_4+PNG_EXT, True), self.words_rect[HORZ_4].size)                       
                      }
        
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
            
        