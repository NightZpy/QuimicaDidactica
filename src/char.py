'''
Created on 11/07/2012

@author: nightzpy
'''
import config
from config import PNG_EXT
from graphics import load_image, resize

class Char:
    '''
    classdocs
    '''

    def __init__(self, char, rect):
        '''
        Constructor
        '''
        self.char = char
        self.rect = rect
        self.release_img = resize(load_image(config.alphabet_soup_char_list+char+'_release'+PNG_EXT, True), self.rect.size)
        self.pressed_img = resize(load_image(config.alphabet_soup_char_list+char+'_pressed'+PNG_EXT, True), self.rect.size)
        
        self.state = self.release_img
        
        self.is_pressed = False
        self.is_release = False
        self.is_correct = False
        self.is_mark = False
        
    def pressed(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos): 
            self.is_pressed = True
            self.is_release = False
        
    def release(self):
        if self.is_pressed:
            self.is_release = True
            self.is_pressed = False
            
    def updater(self):
        if self.is_pressed: self.state = self.pressed_img
        elif self.is_over: self.state = self.pressed_img
        else: self.state = self.release_img           
            
    def draw(self, screen):
        screen.blit(self.state, self.rect)                            