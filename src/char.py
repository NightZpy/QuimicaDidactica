'''
Created on 11/07/2012

@author: nightzpy
'''
import config
from config import PNG_EXT
from graphics import load_image

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
        self.release_img = load_image(config.alphabet_soup_char_list+char+'_release'+PNG_EXT, True)
        self.pressed_img = load_image(config.alphabet_soup_char_list+char+'_pressed'+PNG_EXT, True)
        self.correct_img = load_image(config.alphabet_soup_char_list+char+'_correct'+PNG_EXT, True)
        
        self.state = self.release_img
        
        self.is_pressed = False
        self.is_release = False
        self.is_correct = False
        self.is_mark = False
    
    
    
    def collide_point(self, point):
        if self.rect.collidepoint(point):
            self.is_mark = True
            self.is_pressed = True
            self.is_release = False
            return True
        return False
        
    def collide_rect(self, rect):
        return self.rect.colliderect(rect)
        
    def pressed(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos): 
            self.is_pressed = True
            self.is_release = False
        
    def release(self):
        if self.is_pressed or self.is_mark:
            self.is_release = True
            self.is_pressed = self.is_mark = False
            
    def updater(self):
        if self.is_pressed or self.is_mark: self.state = self.pressed_img
        elif self.is_correct: self.state = self.correct_img
        else: self.state = self.release_img
            
    def draw(self, screen):
        screen.blit(self.state, self.rect)                            