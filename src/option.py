'''
Created on 06/07/2012

@author: nightzpy
'''
import pygame
from graphics import load_image
from pygame.sprite import Sprite
from line import Line

class Option(Sprite):   
   
    def __init__(self, path = False, size = False):
        if path:
            self.img = load_image(path, True)
            #self.img = pygame.transform.scale(self.img, (size[0] - 20, size[1] - 20))
            self.rect = self.img.get_rect()
            self.image_exist = True
        else:
            self.image_exist = path
        self.init_pos = (0, 0)
        
        
        self.is_pressed = False
        self.is_release = False
        self.is_correct = False
        self.is_mark = False
        
        self.line = ''
    
    def set_rect(self, rect):
        self.rect = rect
    
    def pressed(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos): 
            self.is_pressed = True
            self.is_release = False
        
    def release(self):
        if self.is_pressed:
            self.is_release = True
            self.is_pressed = False
        
    def updater(self, grid_rect):
        if self.is_pressed and not self.is_correct:
            mouse_pos = pygame.mouse.get_pos()
            self.move(mouse_pos)
        else:
            if self.rect.colliderect(grid_rect) and self.is_correct: 
                self.move(grid_rect.center)
            else:
                if not self.is_correct: 
                    self.move_to_firts_pos()
    
    def draw(self, screen):
        if self.image_exist: screen.blit(self.img, self.rect)
    
    def resize(self, size):
        if self.image_exist: 
            self.img = pygame.transform.scale(self.img, size)
            self.rect = self.img.get_rect()
    
    def move(self, (x, y)):
        self.rect.centerx = x
        self.rect.centery = y
        
    def firts_pos(self, (x, y)):
        self.rect.left = x
        self.rect.top = y
        self.init_pos = self.rect.topleft
        point_init = self.rect.midright
        self.line = Line(point_init)
        
    def move_to_firts_pos(self):
        self.rect.left = self.init_pos[0]
        self.rect.top = self.init_pos[1]        