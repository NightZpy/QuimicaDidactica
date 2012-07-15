'''
Created on 15/07/2012

@author: nightzpy
'''
from graphics import resize, load_image
import config
from config import PNG_EXT
from buttom import Buttom
from pygame.rect import Rect

VERT_1 = 'alcano'
VERT_2 = 'urea'
VERT_3 = 'hidroxilo'
VERT_4 = 'formico'
HORZ_1 = 'metano'
HORZ_2 = 'alquino'
HORZ_3 = 'carboxilo'
HORZ_4 = 'nitrilo'

WIDTH = 40
HEIGTH = 40

class Crossword:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.typeds = []
        self.exposed = []
        self.finish = False
        
        self.chars = {}
        
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
                        VERT_1: resize(load_image(config.cross_words_imgs+VERT_1+PNG_EXT, True), self.words_rect[VERT_1].size),
                        VERT_2: resize(load_image(config.cross_words_imgs+VERT_2+PNG_EXT, True), self.words_rect[VERT_2].size),
                        VERT_3: resize(load_image(config.cross_words_imgs+VERT_3+PNG_EXT, True), self.words_rect[VERT_3].size),
                        VERT_4: resize(load_image(config.cross_words_imgs+VERT_4+PNG_EXT, True), self.words_rect[VERT_4].size),
                        HORZ_1: resize(load_image(config.cross_words_imgs+HORZ_1+PNG_EXT, True), self.words_rect[HORZ_1].size),
                        HORZ_2: resize(load_image(config.cross_words_imgs+HORZ_2+PNG_EXT, True), self.words_rect[HORZ_2].size),
                        HORZ_3: resize(load_image(config.cross_words_imgs+HORZ_3+PNG_EXT, True), self.words_rect[HORZ_3].size),
                        HORZ_4: resize(load_image(config.cross_words_imgs+HORZ_4+PNG_EXT, True), self.words_rect[HORZ_4].size)                       
                      }
        
        self.buttoms = {
                        VERT_1: Buttom((117, 207), config.cross_b_size, 'cross_'+VERT_1+'_pressed'+PNG_EXT, 'cross_'+VERT_1+'_release'+PNG_EXT, True),
                        VERT_2: Buttom((194, 394), config.cross_b_size, 'cross_'+VERT_2+'_pressed'+PNG_EXT, 'cross_'+VERT_2+'_release'+PNG_EXT, True),
                        VERT_3: Buttom((221, 257), config.cross_b_size, 'cross_'+VERT_3+'_pressed'+PNG_EXT, 'cross_'+VERT_3+'_release'+PNG_EXT, True),
                        VERT_4: Buttom((381, 311), config.cross_b_size, 'cross_'+VERT_4+'_pressed'+PNG_EXT, 'cross_'+VERT_4+'_release'+PNG_EXT, True),
                        HORZ_1: Buttom((11, 233), config.cross_b_size, 'cross_'+HORZ_1+'_pressed'+PNG_EXT, 'cross_'+HORZ_1+'_release'+PNG_EXT, True),
                        HORZ_2: Buttom((91, 313), config.cross_b_size, 'cross_'+HORZ_2+'_pressed'+PNG_EXT, 'cross_'+HORZ_2+'_release'+PNG_EXT, True),
                        HORZ_3: Buttom((141, 365), config.cross_b_size, 'cross_'+HORZ_3+'_pressed'+PNG_EXT, 'cross_'+HORZ_3+'_release'+PNG_EXT, True),
                        HORZ_4: Buttom((90, 448), config.cross_b_size, 'cross_'+HORZ_4+'_pressed'+PNG_EXT, 'cross_'+HORZ_4+'_release'+PNG_EXT, True)                        
                       }                
   
    def put_char(self, char):        
        self.exposed.append(char)  
        
    def load_chars(self):
        list_chars = []
        for char in config.chars.split():
            list_chars.append((char, load_image(config.cross_chars_imgs+char+PNG_EXT, True)))
        self.chars = dict(list_chars)