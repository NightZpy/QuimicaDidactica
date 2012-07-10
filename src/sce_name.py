'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
from name import Name
import pygame
from sce_winner import Sce_Winner
from config import NAME_SCENE

class Sce_Name(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)        
        self.name = Name()
        self.scene_winner =  Sce_Winner(director, 'winner', NAME_SCENE)
        self.c_fails = 0
        self.name.generate_table()
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True
            
            
    def on_update(self):
        self.time = self.director.time 
        
        if not self.is_failed:
            self.update()
            for key, option in self.name.options_names.iteritems():
                if option.is_release:
                    if option.rect.colliderect(self.name.text_field_rect):
                        if key == self.name.current_exercise_key:
                            option.move(self.name.text_field_rect.center)
                            option.is_correct = True   
                        else:
                            self.c_fails += 1
                            if self.c_fails >= 2:
                                self.c_fails = 0
                                self.is_failed = True 
                            option.move_to_firts_pos()  
                    else:                         
                        option.move_to_firts_pos()                                            
                    
                if option.is_pressed:
                    if not option.is_correct:
                        option.move(pygame.mouse.get_pos())
                               
            self.is_complete = self.name.check_complete()

    def on_event(self, event):
        self.event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()
            
            for option in self.name.options_names.itervalues():
                option.pressed(mouse_pos)
                
        elif event.type == pygame.MOUSEBUTTONUP:            
            for option in self.name.options_names.itervalues():
                option.release()


    def on_draw(self, screen):
        self.draw(screen)
        self.name.draw(screen)
        if self.is_failed:
            screen.blit(self.failed_img, self.failed_rect) 
            
        