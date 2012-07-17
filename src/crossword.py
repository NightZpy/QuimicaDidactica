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

WIDTH = 287 - 262
HEIGTH = 374 - 348

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
        self.is_complete = False
        
        self.chars = {}
        
        self.words_rect = {
                            VERT_1: Rect((104, 216), (WIDTH, HEIGTH)),
                            VERT_2: Rect((184, 402), (WIDTH, HEIGTH)),
                            VERT_3: Rect((210, 269), (WIDTH, HEIGTH)),
                            VERT_4: Rect((369, 322), (WIDTH, HEIGTH)),
                            HORZ_1: Rect((25, 217), (WIDTH, HEIGTH)),
                            HORZ_2: Rect((104, 296), (WIDTH, HEIGTH)),
                            HORZ_3: Rect((157, 349), (WIDTH, HEIGTH)),
                            HORZ_4: Rect((104, 429), (WIDTH, HEIGTH))                             
                           }        
        
        self.words = [
                        'alcano',
                        'urea',
                        'hidroxilo',
                        'formico',
                        'metano',
                        'alquino',
                        'carboxilo',
                        'nitrilo'                       
                      ]
        
        self.buttoms = {
                        VERT_1: Buttom((117, 202), config.cross_b_size, 'cross_'+VERT_1+'_pressed'+PNG_EXT, 'cross_'+VERT_1+'_release'+PNG_EXT, True),
                        VERT_2: Buttom((194, 389), config.cross_b_size, 'cross_'+VERT_2+'_pressed'+PNG_EXT, 'cross_'+VERT_2+'_release'+PNG_EXT, True),
                        VERT_3: Buttom((221, 252), config.cross_b_size, 'cross_'+VERT_3+'_pressed'+PNG_EXT, 'cross_'+VERT_3+'_release'+PNG_EXT, True),
                        VERT_4: Buttom((381, 306), config.cross_b_size, 'cross_'+VERT_4+'_pressed'+PNG_EXT, 'cross_'+VERT_4+'_release'+PNG_EXT, True),
                        HORZ_1: Buttom((11, 228), config.cross_b_size, 'cross_'+HORZ_1+'_pressed'+PNG_EXT, 'cross_'+HORZ_1+'_release'+PNG_EXT, True),
                        HORZ_2: Buttom((91, 308), config.cross_b_size, 'cross_'+HORZ_2+'_pressed'+PNG_EXT, 'cross_'+HORZ_2+'_release'+PNG_EXT, True),
                        HORZ_3: Buttom((141, 360), config.cross_b_size, 'cross_'+HORZ_3+'_pressed'+PNG_EXT, 'cross_'+HORZ_3+'_release'+PNG_EXT, True),
                        HORZ_4: Buttom((90, 443), config.cross_b_size, 'cross_'+HORZ_4+'_pressed'+PNG_EXT, 'cross_'+HORZ_4+'_release'+PNG_EXT, True)                        
                       }
        
        self.load_chars()                

    def draw(self, screen):
        for key, buttom in self.buttoms.iteritems():
            buttom.draw(screen)            
            if buttom.is_active and buttom.is_pressed and len(self.typeds) > 0:             
                self.draw_word(screen, self.get_word_typed(), key)
        self.draw_complete_words(screen)
                            
    def draw_complete_words(self, screen):
        for word in self.exposed:
            self.draw_word(screen, word, word)               
     
    def draw_word(self, screen, word, key):
        i = 0        
        rect = self.words_rect[key]
        
        for c in range(len(word)):
            char = word[c]
            if i < len(key):
                img = self.chars[char]
                (x_init, y_init), size = (rect.left, rect.top), rect.size
                if i==0: x, y = x_init, y_init
                else:
                    if key in self.words[0:4]: y = y_init + (rect.height * i) + 1
                    else: x = x_init + (rect.width * i) + 1                    
                 
                screen.blit(img, Rect((x, y), size))
                i += 1          
    
    def update(self):
        self.is_complete = len(self.exposed) == len(self.words)
        for buttom in self.buttoms.itervalues():
            buttom.updater()
           
    def put_char(self, char):        
        self.typeds.append(char) 
        
    def get_word_typed(self):
        return ''.join(self.typeds)
    
    def word_greater(self):
        for key, buttom in self.buttoms.iteritems():
            if buttom.is_pressed:
                return len(self.get_word_typed()) > len(key)
        return False
        
    def check_word(self):
        for key, buttom in self.buttoms.iteritems():
            if buttom.is_pressed:
                word = self.get_word_typed()
                if len(word)>len(key): word = word[0:len(key)] 
                if key==word: 
                    self.exposed.append(key)
                    buttom.is_active = False
                    return True
                else:
                    buttom.is_pressed = False
        self.typeds = []                
        return False
                    
    def load_chars(self):
        list_chars = []
        for i in range(len(config.chars)):
            char = config.chars[i]
            list_chars.append((char, load_image(config.cross_chars_imgs+char+PNG_EXT, True)))
        self.chars = dict(list_chars)