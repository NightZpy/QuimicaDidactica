'''
Created on 06/07/2012

@author: nightzpy
'''
from config import PNG_EXT, TEXT_FIELD, MATCH_PAIRS
from random import randint
import config
from option import Option
from graphics import load_image, resize

class Hangman:
    '''
    classdocs
    '''

    def __init__(self):
        self.text_field_img = resize(load_image(config.name_items+TEXT_FIELD+PNG_EXT, True), config.name_text_field_size)
        self.text_field_rect = self.text_field_img.get_rect()
        self.text_field_rect.center = config.name_text_field_pos
        
        self.is_complete = False
        self.tracks = []
        self.words = []
        
        self.load_words()            
        self.generate_table()
           
    def generate_table(self):
        pass      

    def load_words(self):
        f = open(config.hangman+'words.txt', "r")
        lines = f.readlines()
        t_lines = len(lines)
        c_lines = 0
        while c_lines < t_lines:
            self.tracks.append(lines[c_lines])
            self.words.append(lines[c_lines+1])
            c_lines += 2
            
            
    def check_complete(self):
        if len(self.functions) > 0 and len(self.elements) > 0: 
            c_corrects = 0
            for function in self.functions.itervalues():
                if function.is_correct: c_corrects += 1
                if c_corrects == MATCH_PAIRS: 
                    self.is_complete = True
                    break
            
        return self.is_complete

    def draw(self, screen):
        pass
        
            
            
            
            