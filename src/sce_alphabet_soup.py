'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
import pygame
from pygame.rect import Rect
from config import END, ALPHABET_SOUP_SCENE, BLACK, PNG_EXT
from sce_winner import Sce_Winner
from graphics import load_image
import config
from alphabet_soup import Alphabet_Soup

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
        
        for buttom in self.common_buttoms.itervalues():
            buttom.move_at(60)    
            buttom.is_visible = True  
        
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
        self.update()
                        
    def on_event(self, event):
        self.event(event)               
        

    def on_draw(self, screen):
        self.draw(screen)
        self.alphabet_soup.draw(screen)
            
        