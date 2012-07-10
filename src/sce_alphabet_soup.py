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
        self.valid_words_rect = {}
        
        self.valid_words_key = [
                                    METANO,
                                    ALQUINO,
                                    ETANODIOL, 
                                    BENCENO,  
                                    HEXANOL, 
                                    FORMALDEHIDO, 
                                    FENOLES,
                                    ETERMETILICO,
                                    ACETALDEHIDO,
                                    ACETONA,                                     
                                    PENTANOICO,
                                    BUTIRAMIDA,
                                    CIANOGENO                                                             
                                 ]
            
        self.words_rect = {}
        self.words_img = {}

        self.crux_words_rect = { 
                                ACETALDEHIDO: [Rect((199, 169), CHAR_SIZE),
                                              Rect((223, 196), CHAR_SIZE), 
                                              Rect((244, 220), CHAR_SIZE),
                                              Rect((267, 245), CHAR_SIZE),
                                              Rect((295, 270), CHAR_SIZE),
                                              Rect((323, 293), CHAR_SIZE),
                                              Rect((346, 320), CHAR_SIZE),
                                              Rect((367, 344), CHAR_SIZE),
                                              Rect((394, 366), CHAR_SIZE),
                                              Rect((419, 390), CHAR_SIZE),
                                              Rect((440, 415), CHAR_SIZE),
                                              Rect((465, 438), CHAR_SIZE)],
                                FENOLES: [Rect((345, 388), CHAR_SIZE),
                                              Rect((368, 411), CHAR_SIZE), 
                                              Rect((244, 220), CHAR_SIZE),
                                              Rect((392, 436), CHAR_SIZE),
                                              Rect((415, 462), CHAR_SIZE),
                                              Rect((440, 485), CHAR_SIZE),
                                              Rect((465, 510), CHAR_SIZE),
                                              Rect((488, 534), CHAR_SIZE)],
                                METANO: [Rect((102, 267), CHAR_SIZE),
                                              Rect((124, 291), CHAR_SIZE), 
                                              Rect((148, 315), CHAR_SIZE),
                                              Rect((172, 336), CHAR_SIZE),
                                              Rect((196, 365), CHAR_SIZE),
                                              Rect((222, 387), CHAR_SIZE)],
                                ACETONA: [Rect((103, 340), CHAR_SIZE),
                                              Rect((122, 365), CHAR_SIZE), 
                                              Rect((147, 388), CHAR_SIZE),
                                              Rect((172, 412), CHAR_SIZE),
                                              Rect((197, 438), CHAR_SIZE),
                                              Rect((221, 461), CHAR_SIZE),
                                              Rect((247, 485), CHAR_SIZE)],
                                    HEXANOL: [Rect((463, 215), CHAR_SIZE),
                                              Rect((463, 241), CHAR_SIZE), 
                                              Rect((463, 265), CHAR_SIZE),
                                              Rect((463, 288), CHAR_SIZE),
                                              Rect((463, 313), CHAR_SIZE),
                                              Rect((463, 338), CHAR_SIZE),
                                              Rect((463, 363), CHAR_SIZE)],
                                    ALQUINO: [Rect((321, 265), CHAR_SIZE),
                                              Rect((321, 293), CHAR_SIZE), 
                                              Rect((321, 314), CHAR_SIZE),
                                              Rect((321, 340), CHAR_SIZE),
                                              Rect((321, 363), CHAR_SIZE),
                                              Rect((321, 389), CHAR_SIZE),
                                              Rect((321, 411), CHAR_SIZE)],
                                    FORMALDEHIDO: [Rect((103, 169), CHAR_SIZE), 
                                              Rect((131, 167), CHAR_SIZE),
                                              Rect((154, 167), CHAR_SIZE),
                                              Rect((178, 167), CHAR_SIZE),
                                              Rect((204, 168), CHAR_SIZE),
                                              Rect((229, 167), CHAR_SIZE),
                                              Rect((224, 167), CHAR_SIZE),
                                              Rect((251, 167), CHAR_SIZE),
                                              Rect((275, 167), CHAR_SIZE),
                                              Rect((298, 167), CHAR_SIZE),
                                              Rect((324, 168), CHAR_SIZE),
                                              Rect((348, 168), CHAR_SIZE),
                                              Rect((373, 167), CHAR_SIZE)],
                                    CIANOGENO: [Rect((225, 194), CHAR_SIZE), 
                                              Rect((252, 195), CHAR_SIZE),
                                              Rect((275, 195), CHAR_SIZE),
                                              Rect((300, 194), CHAR_SIZE),
                                              Rect((322, 197), CHAR_SIZE),
                                              Rect((347, 195), CHAR_SIZE),
                                              Rect((371, 194), CHAR_SIZE),
                                              Rect((394, 194), CHAR_SIZE),
                                              Rect((420, 193), CHAR_SIZE)],
                                    ETANODIOL: [Rect((129, 290), CHAR_SIZE), 
                                              Rect((152, 290), CHAR_SIZE),
                                              Rect((176, 289), CHAR_SIZE),
                                              Rect((200, 289), CHAR_SIZE),
                                              Rect((224, 289), CHAR_SIZE),
                                              Rect((249, 289), CHAR_SIZE),
                                              Rect((274, 290), CHAR_SIZE),
                                              Rect((297, 290), CHAR_SIZE),
                                              Rect((321, 292), CHAR_SIZE)],
                                    BENCENO: [Rect((79, 485), CHAR_SIZE), 
                                              Rect((102, 484), CHAR_SIZE),
                                              Rect((127, 483), CHAR_SIZE),
                                              Rect((151, 484), CHAR_SIZE),
                                              Rect((177, 483), CHAR_SIZE),
                                              Rect((201, 483), CHAR_SIZE),
                                              Rect((223, 484), CHAR_SIZE),
                                              Rect((248, 485), CHAR_SIZE)],
                                    PENTANOICO: [Rect((52, 533), CHAR_SIZE), 
                                              Rect((78, 533), CHAR_SIZE),
                                              Rect((105, 532), CHAR_SIZE),
                                              Rect((128, 533), CHAR_SIZE),
                                              Rect((151, 532), CHAR_SIZE),
                                              Rect((176, 533), CHAR_SIZE),
                                              Rect((200, 533), CHAR_SIZE),
                                              Rect((225, 533), CHAR_SIZE),
                                              Rect((251, 533), CHAR_SIZE),
                                              Rect((275, 533), CHAR_SIZE)],
                                    ETERMETILICO: [Rect((53, 169), CHAR_SIZE), 
                                              Rect((53, 196), CHAR_SIZE),
                                              Rect((53, 219), CHAR_SIZE),
                                              Rect((53, 243), CHAR_SIZE),
                                              Rect((53, 268), CHAR_SIZE),
                                              Rect((53, 292), CHAR_SIZE),
                                              Rect((53, 316), CHAR_SIZE),
                                              Rect((53, 339), CHAR_SIZE),
                                              Rect((53, 362), CHAR_SIZE),
                                              Rect((53, 389), CHAR_SIZE),
                                              Rect((53, 413), CHAR_SIZE),
                                              Rect((53, 438), CHAR_SIZE)],                        
                                BUTIRAMIDA: [Rect((78, 486), CHAR_SIZE), 
                                              Rect((78, 459), CHAR_SIZE),
                                              Rect((78, 437), CHAR_SIZE),
                                              Rect((78, 413), CHAR_SIZE),
                                              Rect((78, 389), CHAR_SIZE),
                                              Rect((78, 364), CHAR_SIZE),
                                              Rect((78, 341), CHAR_SIZE),
                                              Rect((78, 314), CHAR_SIZE),
                                              Rect((78, 289), CHAR_SIZE),
                                              Rect((78, 265), CHAR_SIZE)]                                                                 
                                }
        
        self.motion_points = []
        self.word_complete = False
        self.complete_words = []
        self.is_pressed = False
        self.is_release = False
        
        self.load_word_list()
        self.load_valid_word_list()
        self.load_word_in_soup()
        self.load_words_in_soup_list()

    def load_valid_word_list(self):
        i = 0
        prev = False
        for word in self.valid_words_key:
            rect = self.valid_words_rect[word]
            if i < 9:
                if i == 0: rect.topleft = (542, 122)
                else: rect.topleft = (542, prev.bottom + 5)                
            else:
                if i == 9: rect.topleft = (659, 122)
                else: rect.topleft = (659, prev.bottom + 5)
            prev = rect
            i += 1
            
    def load_words_in_soup_list(self):
        for key, rect in self.crux_words_rect.iteritems():
            pos = rect[0].topleft
            self.words_rect[key].topleft = pos
                    
            
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

    def load_word_list(self):
        for word in self.valid_words_key:
            self.valid_words_img[word] = load_image(config.alphabet_soup_list+word+PNG_EXT, True)
            self.valid_words_rect[word] = self.valid_words_img[word].get_rect()    
            
    def load_word_in_soup(self):
        for word in self.valid_words_key:
            self.words_img[word] = load_image(config.alphabet_soup+word+PNG_EXT, True)
            self.words_rect[word] = self.words_img[word].get_rect()
    
    def on_update(self):
        self.time = self.director.time
        if not self.is_failed:
            self.update()
            if len(self.motion_points) > 0:
                check_word = self.check_word()
                if check_word:
                    self.complete_words.append(check_word)
                self.is_release = False
            if len(self.complete_words) == len(self.valid_words_key):
                self.is_complete = True
                        
    def on_event(self, event):
        self.event(event)         
        if event.type == pygame.MOUSEBUTTONUP:                                
            mouse_pos = pygame.mouse.get_pos()
            print str(mouse_pos)
            self.motion_points.append(mouse_pos)
            #print str(self.motion_points)                
        

    def on_draw(self, screen):
        self.draw(screen)
        
        for key, img in self.valid_words_img.iteritems():
            rect = self.valid_words_rect[key]
            screen.blit(img, rect)
        
        if self.complete_words:
            for word in self.complete_words:
                pygame.draw.line(screen,BLACK,self.valid_words_rect[word].midleft,self.valid_words_rect[word].midright ,6)
                rect = self.words_rect[word]
                img = self.words_img[word]
                screen.blit(img, rect)
            
        