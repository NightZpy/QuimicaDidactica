'''
Created on 01/02/2012

@author: nightzpy
'''
import config

from pygame.sprite import Sprite
from graphics import load_image
import pygame
import time

class Buttom(Sprite):
    '''
    classdocs
    ''' 


    def __init__(self, x, y, img_pressed_path, img_release_path, visible = False):
        '''
        Constructor
        '''
        Sprite.__init__(self)
        self.pressed_img = load_image(config.buttoms_png+img_pressed_path, True, (0,0))
        self.pressed_img = pygame.transform.scale(self.pressed_img, (270, 140))
        self.pressed_rect = self.pressed_img.get_rect() 
        self.release_img = load_image(config.buttoms_png+img_release_path, True, (0,0))
        self.release_img = pygame.transform.scale(self.release_img, (270, 140))
        self.release_rect = self.release_img.get_rect()
        self.pressed_rect.centerx = x
        self.pressed_rect.centery = y
        self.release_rect.centerx = x
        self.release_rect.centery = y
        self.is_pressed = False
        self.is_over = False
        self.beep = pygame.mixer.Sound('beep1.ogg')

        self.state = self.release_img
        self.state_rect = self.release_rect
        
        self.is_visible = visible
        
    def pressed(self, (x, y)):
        if (not self.is_pressed) and self.pressed_rect.collidepoint(x, y): 
            self.is_pressed = True
            print "Pressed in pos: "+str((x, y))
        else: 
            self.is_pressed = False
        
    def mouse_over(self, (x, y)): 
        if (not self.is_pressed) and self.pressed_rect.collidepoint(x, y): self.is_over = True
        else: self.is_over = False
    
    def updater(self):
        if self.is_pressed: 
            #self.beep.play()
            #time.sleep(1)
            #self.beep.stop()
            self.state = self.pressed_img
            self.state_rect = self.pressed_rect
        elif self.is_over:
            self.state = self.pressed_img
            self.state_rect = self.pressed_rect
        else:
            self.state = self.release_img
            self.state_rect = self.release_rect 
            
    def dibujar(self, pantalla):
        if self.is_visible: pantalla.blit(self.state, self.state_rect)
                       
        