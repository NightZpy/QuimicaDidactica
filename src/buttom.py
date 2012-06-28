'''
Created on 01/02/2012

@author: nightzpy
'''
import config

from pygame.sprite import Sprite
from graphics import load_image
import pygame

class Buttom(Sprite):
    '''
    classdocs
    ''' 


    def __init__(self, x, y, img_pressed_path, img_release_path, visible = False):
        '''
        Constructor
        '''
        Sprite.__init__(self)
        self.pressedImg = load_image(config.buttoms_png+img_pressed_path, True, (0,0))
        self.pressedImg = pygame.transform.scale(self.pressedImg, (270, 140))
        self.pressedRect = self.pressedImg.get_rect() 
        self.released = load_image(config.buttoms_png+img_release_path, True, (0,0))
        self.released = pygame.transform.scale(self.released, (270, 140))
        self.releasedRect = self.released.get_rect()
        self.pressedRect.centerx = x
        self.pressedRect.centery = y
        self.releasedRect.centerx = x
        self.releasedRect.centery = y
        self.isPressed = False
        
        self.state = self.released
        self.stateRect = self.releasedRect
        
        self.isVisible = visible
        
    def pressed(self, (x, y)):
        if (not self.isPressed) and self.pressedRect.collidepoint(x, y): self.isPressed = True
        else: self.isPressed = False
        
    def actualizar(self):
        if self.isPressed: 
            self.state = self.pressedImg
            self.stateRect = self.pressedRect
        else:
            self.state = self.released
            self.stateRect = self.releasedRect 
            
    def dibujar(self, pantalla):
        if self.isVisible: pantalla.blit(self.state, self.stateRect)
                       
        