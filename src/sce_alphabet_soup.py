'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
import pygame
from config import ALPHABET_SOUP_SCENE, PNG_EXT, EXIT,\
    MAIN_MENU_SCENE
from sce_winner import Sce_Winner
import config
from alphabet_soup import Alphabet_Soup
from buttom import Buttom

WIDTH_WORD = 25
HEIGTH_WORD = 27

HEIGTH_VALID_WORD = 31

CHAR_SIZE = (23, 24)

# Elements
ETERMETILICO = 'etermetilico'
BUTIRAMIDA = 'butiramida'
ALQUINO = 'alquino'
HEXANOL = 'hexanol'
FORMALDEHIDO = 'formaldehido'
CIANOGENO = 'cianogeno'
ETANODIOL = 'etanodiol'
BENCENO = 'benceno'
PENTANOICO = 'pentanoico'
ACETONA = 'acetona'
METANO = 'metano'
ACETALDEHIDO = 'acetaldehido'
FENOLES = 'fenoles'

class Sce_Alphabet_Soup(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)
        self.scene_winner =  Sce_Winner(director, 'winner', ALPHABET_SOUP_SCENE)
        self.btn_correct = Buttom(config.alphabet_soup_btn_correct_pos, config.alphabet_soup_btn_correct_size, "correct_pressed"+PNG_EXT, "correct_release"+PNG_EXT, True)
        
        for buttom in self.common_buttoms.itervalues():
            buttom.move_at(60)    
            buttom.is_visible = True  
        
        self.common_buttoms[MAIN_MENU_SCENE].move_at(15)
        self.common_buttoms[EXIT].move_at(60)
        
        self.valid_words_img = {}
            
        self.words_rect = {}
        self.words_img = {}
        
        self.motion_points = []
        self.word_complete = False
        self.complete_words = []
        self.is_pressed = False
        self.is_release = False
        self.alphabet_soup = Alphabet_Soup()
                    
            
    def check_word(self):        
        n_pos = len(self.motion_points)
        c_collitions = 0
        point = False
        greater = False
        for key, word in self.crux_words_rect.iteritems():
            if self.complete_words.count(key) == 0:
                n_chars = len (word)
                #print "N_chars: "+str(n_chars)
                #print "Word: "+str(key)
                if n_chars == n_pos:
                    for char in word:
                        for point in self.motion_points:
                            if char.collidepoint(point):                                
                                c_collitions +=1
                                #print "colitions: "+str(c_collitions)
                                #print "n_pos: "+str(n_pos)
                                #print "C_col: "+str(c_collitions)
                    if c_collitions == n_pos:
                        self.motion_points = [] 
                        return key
                    else: c_collitions = 0
                    greater = False
                greater = n_pos > n_chars           
        
        if greater:
            self.is_failed = True 
            self.motion_points = []
        return False
    
    def on_update(self):
        self.time = self.director.time
        if not self.is_failed:
            self.btn_correct.updater()
            self.update()
            self.alphabet_soup.update()
            self.is_complete = self.alphabet_soup.is_complete
                        
    def on_event(self, event):        
        if not self.is_failed:
            self.event(event)            
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self.alphabet_soup.check_collide_with_char(mouse_pos) 
                if self.btn_correct.pressed(mouse_pos):
                    self.alphabet_soup.check_word()
                    self.is_failed = self.alphabet_soup.is_failed
                    self.btn_correct.is_pressed = False
                      
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                self.btn_correct.mouse_over(mouse_pos)
            #elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:                                                        
        else: 
            if event.type == pygame.KEYUP and event.key == pygame.K_RETURN: self.is_failed = False
            

    def on_draw(self, screen):
        self.draw(screen)
        self.btn_correct.draw(screen)
        self.alphabet_soup.draw(screen)
        if self.is_failed: screen.blit(self.failed_img, self.failed_rect)
            
            
        